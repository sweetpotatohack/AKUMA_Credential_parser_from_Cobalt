import csv
import re

INPUT_FILE = "credentials.tsv"

users = set()
passwords = set()
hashes = set()

def is_hash(s):
    s = s.strip()
    # NTLM/LM: 32 hex-символа или строка вида LM:NTLM
    if re.fullmatch(r"[a-fA-F0-9]{32,}", s):
        return True
    if re.fullmatch(r"[a-fA-F0-9]{32}:[a-fA-F0-9]{32}", s):
        return True
    return False

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        if not row or row[0].startswith("#") or row[0].lower() == "user":
            continue
        user = row[0].strip()
        secret = row[1].strip()
        if user:
            users.add(user)
        if secret:
            if is_hash(secret):
                hashes.add(secret)
            else:
                passwords.add(secret)

with open("users.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(users)))
with open("pass.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(passwords)))
with open("hash.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(hashes)))

print("Готово! AKUMA позаботился о тебе")
