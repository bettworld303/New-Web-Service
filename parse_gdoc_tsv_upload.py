import json

INPUT_FILE = 'gdoc_tsv_upload_records.json'
OUTPUT_FILE = 'gdoc_tsv_upload_parsed.json'

# Load the input JSON file
def load_records(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def parse_tsv(tsv_string):
    rows = tsv_string.strip().split('_y_')
    parsed = [row.split('_x_') for row in rows if row.strip()]
    return parsed

def main():
    records = load_records(INPUT_FILE)
    all_parsed = []
    for rec in records:
        tsv = rec.get('tab_separated_data', '')
        parsed_rows = parse_tsv(tsv)
        all_parsed.append({
            'id': rec.get('id'),
            'parsed_rows': parsed_rows
        })
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_parsed, f, indent=2)
    print(f"Wrote {len(all_parsed)} records to {OUTPUT_FILE}")

if __name__ == '__main__':
    main()