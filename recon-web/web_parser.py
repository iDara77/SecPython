from bs4 import BeautifulSoup

FILE = "_ob-s.xyz.html"

with open(FILE) as f:
    soup = BeautifulSoup(f, features="html.parser")

print(soup.title)
print("=" * 64)
print(soup.title.string)
print("=" * 64)
print("=" * 64)
print(soup.prettify())
print("=" * 64)
print(soup.get_text())
for script in soup.find_all("script"):
    print(script.get('src'))
    print("-" * 64)
print("=" * 64)
for cell in soup.find_all("td"):
    print(cell)
    print("-" * 64)
else:
    print("no cell")
    