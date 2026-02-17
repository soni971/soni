import requests
from bs4 import BeautifulSoup
# abc= "https://www.instagram.com"
# abc= "https://edunetfoundation.org/"
# abc= "https://www.youtube.com/"
abc= "https://www.allduniv.ac.in"


respons = requests.get(abc)
if respons.status_code==200:
    print("Sucessfully fetchd webpage.")
else:
    print("Error fetching page")

html_content = respons.text
if html_content:
    soup = BeautifulSoup(html_content, "html.parser")
    title=soup.title.string
    print(title)


# # 1. EXTRACT ALL HEADINGS (H1-H6)
# for i in range(1,7):
#     for heading in soup.find_all(f"h{i}"):
#         print(f"heading{i}{heading.get_text(strip=True)}")

# # EXTRACT ALL CONTENT IN WEBPAGE  
# for paragraph in soup.find_all("p"):
#     print(paragraph.get_text(strip=True))

# # EXTRACT ALL LINKS IN WEBPAGE
# for a in soup.find_all("a"):
#     text=a.get_text(strip=True)
#     href=a["href"]
#     print(text, href)

# # EXTRACT IMAGE
# for img in soup.find_all("img"):
#     src=img["src"]
#     print(src)

url = "http://quotes.toscrape.com/"
respons = requests.get(url)
soup = BeautifulSoup(respons.text, "html.parser")


quotes=soup.findAll("span",class_="text")
authors=soup.find_all("small",class_="author")


print("Quotes from the page:")
for q, a in zip (quotes, authors):
    print(f"{q.get_text()} - {a.get_text()}")

    
