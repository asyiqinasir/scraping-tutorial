import os
import importlib
import json

def main():
    all_data = []
    script_folder = 'scripts'

    for filename in os.listdir(script_folder):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]  # Remove .py extension
            module_path = f"{script_folder}.{module_name}"

            try:
                print(f"Running {module_name}...")
                mod = importlib.import_module(module_path)
                data = mod.scrape()
                all_data.extend(data)
            except Exception as e:
                print(f"❌ Error in {module_name}: {e}")

    # Save all collected data to output.json
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Done. {len(all_data)} records saved to output.json")

if __name__ == "__main__":
    main()
