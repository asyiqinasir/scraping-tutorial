# scraping-tutorial

🕸️ Government Staff Scraper
This is a modular web scraping project for collecting staff directory data (e.g., from mot.gov.my) across multiple .my websites.

Each site has its own script inside the scripts/ folder, and a central main.py runs them all automatically.

### Project Structure
```
scraping-tutorial/
├── main.py                # Master script that runs all scrapers
├── output.json            # Combined output (auto-generated)
├── scripts/               # Folder for per-site scrapers
│   ├── mot.py             # Example scraper for MOT
│   ├── moh.py             # (Add more scripts here)
```

### How to Use

1. Create & activate environment
```
python3.11 -m venv env      
```

```
source env/bin/activate
```

1. Install dependencies
Only uses standard libraries plus requests and lxml
```
pip install requests lxml
```

Or if you use a requirements.txt:
```
pip install -r requirements.txt
```

2. Run all scrapers
```
python main.py
```
- This will automatically find and run every *.py inside scripts/ folder
- Results will be saved to output.json

or, 

3. Run a single scraper (for testing)
Each script (like mot.py) also supports standalone execution:
```
python scripts/mot.py
```
- Scrapes only MOT data
- Saves to mot.json


### How to Add a New Scraper
1. Create a new Python file in scripts/, e.g. scripts/kdn.py
2. Add a scrape() function that returns a list of dictionaries

That’s it — main.py will auto-detect and run it

### Output Format
Each scraper returns structured dictionaries like:
```
{
  "org_id": "MOT",
  "org_name": "KEMENTERIAN PENGANGKUTAN",
  "person_name": "John Doe",
  "person_email": "john@mot.gov.my",
  ...
}
```

