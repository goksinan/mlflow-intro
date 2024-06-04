import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page with the list of most-viewed articles
url = "https://en.wikipedia.org/wiki/List_of_comedians"

# Send a request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the links on the page
links = soup.find_all("a")

# Extract the comedian names from the links
comedian_names = []
for link in links:
    href = link.get("href")
    if "/wiki/" in href and "Category:" not in href:
        name = link.get_text().strip()
        comedian_names.append(name)

# Print the list of comedian names
print(comedian_names)