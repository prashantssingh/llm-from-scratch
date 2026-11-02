import os
import urllib.request

if not os.path.exists("the-verdict.txt"):
    url = "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/refs/heads/main/ch02/01_main-chapter-code/the-verdict.txt"
    filename = "the-verdict.txt"
    urllib.request.urlretrieve(url, filename)
    