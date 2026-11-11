import os
import urllib.request

if not os.path.exists("the-verdict.txt"):
    url = "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/refs/heads/main/ch02/01_main-chapter-code/the-verdict.txt"
    filename = "the-verdict.txt"
    urllib.request.urlretrieve(url, filename)

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

words = raw_text.split("")
result = [item for item in words if item.strip() != ""]

preprocessed = set(result)
sorted_unique_words = sorted(preprocessed)

