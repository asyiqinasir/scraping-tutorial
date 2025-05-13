import requests
from lxml import html
import json

START_URLS = [
    'https://www.mot.gov.my/my/directory/staff?bahagian=Pejabat%20Menteri&pagetitle=Pejabat%20Menteri',
    # 'https://www.mot.gov.my/my/directory/staff?bahagian=Pejabat%20Timbalan%20Menteri&pagetitle=Pejabat%20Timbalan%20Menteri',
    # 'https://www.mot.gov.my/my/directory/staff?bahagian=Pejabat%20Ketua%20Setiausaha&pagetitle=Pejabat%20Ketua%20Setiausaha'
]

def scrape():
    all_data = []
    person_sort_order = 0

    for i, url in enumerate(START_URLS, start=1):
        print(f"[MOT] Scraping: {url}")
        response = requests.get(url)
        tree = html.fromstring(response.content)

        container = tree.xpath("(//div[@class='grid-container staff-directory'])[2]")
        if not container:
            continue

        rows = container[0].xpath(".//table[@class='stdirectory unstriped stack']/tbody/tr")

        for row in rows:
            person_sort_order += 1

            person_name = row.xpath(".//td[@data-label='Nama']/span[1]/text()")
            person_position = row.xpath(".//td[@data-label='Nama']/span[2]/text()")

            division_elements = row.xpath(
                ".//td[@data-label='Division']//span/text() | "
                ".//td[@data-label='Division']//br/following-sibling::text()"
            )
            divisions = [d.strip() for d in division_elements if d.strip()]
            division = divisions[0] if len(divisions) > 0 else None
            unit = divisions[1] if len(divisions) > 1 else None

            email_prefix = row.xpath(".//td[@data-label='Email']/span/text()")
            phone = row.xpath(".//td[@data-label='Telefon']/span/text()")

            item = {
                'org_id': 'MOT',
                'org_name': 'KEMENTERIAN PENGANGKUTAN',
                'org_type': 'ministry',
                'division_sort': i,
                'position_sort_order': person_sort_order,
                'division_name': division,
                'subdivision_name': unit,
                'person_name': person_name[0].strip() if person_name else None,
                'position_name': person_position[0].strip() if person_position else None,
                'person_phone': phone[0].strip() if phone else None,
                'person_email': f"{email_prefix[0].strip()}@mot.gov.my" if email_prefix else None,
                'person_fax': None,
            }

            all_data.append(item)

    return all_data

if __name__ == "__main__":
    print(f"Scraping... ")
    data = scrape()
    print(f"Scraped {len(data)} records.")
    with open("mot.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Data saved to mot_test_output.json")
