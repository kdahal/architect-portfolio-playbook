import csv, sys, re
from collections import Counter

def tokenize(text):
    return re.findall(r"[a-zA-Z0-9\-]+", text.lower())

def analyze(file_path):
    counts, total = Counter(), 0
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            text = (r.get('title','') + ' ' + r.get('description','')).strip()
            counts.update(tokenize(text))
            total += 1
    for token, cnt in counts.most_common(15):
        print(f"{token}: {cnt}")
    print(f"Total tickets analyzed: {total}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_tickets.py tickets.csv")
        sys.exit(1)
    analyze(sys.argv[1])
