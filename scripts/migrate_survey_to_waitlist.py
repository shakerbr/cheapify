#!/usr/bin/env python3
"""Migrate survey responses from market-validation-survey-oct2026.csv into the Cheapify waitlist database."""
import csv
import json
import os
import re
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SURVEY_FILE = os.path.join(ROOT_DIR, 'entrepreneurship/assets/evidence/market-validation-survey-oct2026.csv')
OUTPUT_JSON = os.path.join(ROOT_DIR, 'website/api/data/waitlist.json')
OUTPUT_CSV = os.path.join(ROOT_DIR, 'website/api/data/waitlist.csv')

negative_patterns = [
    'no', 'none', 'لا', 'نەخێر', 'لا شكرا', 'لا شكراً', 'nope', '-', 'na', 'n/a', 'nothing',
    'good doing bro keep achieving', 'بةردوام به برا', 'leave whatsapp', 'غير مرة أن شاء الله',
    'نعم', 'yes', 'جيد استمرّ'
]

def parse_survey_timestamp(ts_str):
    try:
        # Format: 9/22/2026 21:29:36
        dt = datetime.strptime(ts_str.strip(), '%m/%d/%Y %H:%M:%S')
        return dt.isoformat() + 'Z'
    except Exception:
        return datetime.utcnow().isoformat() + 'Z'

def main():
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    
    entries = []
    seen = set()

    with open(SURVEY_FILE, encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        
        for row_idx, row in enumerate(reader, start=2):
            raw_ts = row[0]
            iso_ts = parse_survey_timestamp(raw_ts)

            # 1. Shopper check (columns 7, 17, 27)
            for c in [7, 17, 27]:
                if c < len(row):
                    val = row[c].strip()
                    if val and val.lower() not in negative_patterns and len(val) >= 3:
                        if not any(x in val.lower() for x in ['good doing', 'بةردوام']):
                            norm = val.lower().replace(' ', '').replace('-', '').replace('‏', '')
                            if norm not in seen:
                                seen.add(norm)
                                entry_id = f'mig_s_{row_idx}_{len(entries)+1}'
                                entries.append({
                                    'id': entry_id,
                                    'timestamp': iso_ts,
                                    'role': 'shopper',
                                    'contact': val,
                                    'item': 'Early Beta Access',
                                    'ip': 'survey_migration',
                                    'userAgent': 'Google Forms Survey'
                                })

            # 2. Merchant check (columns 11, 21, 31)
            for c in [11, 21, 31]:
                if c < len(row):
                    val = row[c].strip()
                    if val and val.lower() not in negative_patterns and len(val) >= 3:
                        if not any(x in val.lower() for x in ['good doing', 'بةردوام']):
                            norm = val.lower().replace(' ', '').replace('-', '').replace('‏', '')
                            if norm not in seen:
                                seen.add(norm)
                                entry_id = f'mig_m_{row_idx}_{len(entries)+1}'
                                entries.append({
                                    'id': entry_id,
                                    'timestamp': iso_ts,
                                    'role': 'merchant',
                                    'contact': val,
                                    'item': 'Founding Pilot Store',
                                    'ip': 'survey_migration',
                                    'userAgent': 'Google Forms Survey'
                                })

    # Write to JSON
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)

    # Write to CSV
    with open(OUTPUT_CSV, 'w', encoding='utf-8') as f:
        f.write('id,timestamp,role,contact,item,ip,user_agent\n')
        for e in entries:
            contact_esc = e['contact'].replace('"', '""')
            item_esc = (e['item'] or '').replace('"', '""')
            f.write(f'"{e["id"]}","{e["timestamp"]}","{e["role"]}","{contact_esc}","{item_esc}","{e["ip"]}","{e["userAgent"]}"\n')

    shoppers = [e for e in entries if e['role'] == 'shopper']
    merchants = [e for e in entries if e['role'] == 'merchant']
    print(f'Successfully migrated {len(entries)} entries:')
    print(f'  Shoppers:  {len(shoppers)}')
    print(f'  Merchants: {len(merchants)}')
    print(f'Output written to:\n  {OUTPUT_JSON}\n  {OUTPUT_CSV}')

if __name__ == '__main__':
    main()
