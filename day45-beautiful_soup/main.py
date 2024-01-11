from bs4 import BeautifulSoup

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.a) #gives first anchor tag
# all_anchor_tags = soup.find_all(name = "a")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name = "h1", id = "name").string # search by type h1 and id
# print(heading)
#
# section_heading = soup.find(name = "h3", class_ = "heading")
# print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)

import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

refs = soup.select(selector=".titleline > a")
article_texts = []
article_links = []
for ref in refs:
    article_texts.append(ref.getText())
    article_links.append(ref.get("href"))

scores = soup.find_all(name = "span", class_ = "score")
article_scores = []
for score in scores:
    article_scores.append(score.getText().split()[0])

largest_number = max(article_scores)
largest_index = article_scores.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_texts)
# print(article_links)
# print(article_scores)