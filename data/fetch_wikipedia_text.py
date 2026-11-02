import os
import urllib.request

if not os.path.exists("the-verdict.txt"):
    url = "https://en.wikipedia.org/wiki/The_Verdict"
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf-8")

    # Extract the main content of the Wikipedia page
    start_index = html.find('<div class="mw-parser-output">')
    end_index = html.find('<div class="printfooter">')
    main_content = html[start_index:end_index]

    # Remove HTML tags
    import re
    text = re.sub(r'<[^>]+>', '', main_content)

    # Save the text to a file
    with open("the-verdict.txt", "w", encoding="utf-8") as f:
        f.write(text)