import requests
from bs4 import BeautifulSoup

url = "https://www.52pojie.cn/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

boxbg_7rees = soup.find_all("div", class_="boxbg_7ree")
third_boxbg_7ree = boxbg_7rees[2]

titles = []
links = []

for a_tag in third_boxbg_7ree.find_all("a"):
    title = a_tag.get_text(strip=True)
    link = url + a_tag["href"]
    titles.append(title)
    links.append(link)
  

with open("52pojie.txt", "w", encoding="utf-8") as f:
    for i in range(len(titles)):
        f.write(titles[i] + " " + links[i] + "\n")
