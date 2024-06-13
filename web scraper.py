import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://picoctf.org/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract information from the website
    title = soup.find("title").text
    heading = soup.find("h1")
    if heading:
        heading = heading.text
    else:
        heading = "No h1 heading found"
    paragraphs = soup.find_all("p")
    for paragraph in paragraphs:
        print(paragraph.text)

else:
    print("Error: Unable to access website")
