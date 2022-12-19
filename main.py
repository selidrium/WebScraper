from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = (response.text)
soup = BeautifulSoup(yc_webpage, "html.parser")

article_tag = soup.find(name="span", class_="titleline")
anchor_tag = article_tag.find(name="a")
article_text = article_tag.get_text()



all_anchor_tags = soup.find_all(name="span", class_="titleline")
all_score = soup.find_all(class_="score")
# print(all_score)

# for tag in all_anchor_tags:
#     print(tag.find(name="a").getText())
#     print(tag.find(name="a").get("href"))
# for score in all_score:
#     print(score.getText())


titles = [n.find(name="a").getText() for n in soup.find_all(class_="titleline")]
links = [n.find(name="a").get("href") for n in soup.find_all(class_="titleline")]
votes = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]

# print(titles)
# print(links)
# print(votes)

largest_number = max(votes)
largest_index = votes.index(largest_number)

print(titles[largest_index])
print(links[largest_index])


# for tag in all_anchor_tags:
#     print(tag)
# #
# article_tag = soup.find(name="span", class_="titleline")
# article_text = article_tag.get_text()
# article_link = article_tag.find(name="href")
# for tag in all_anchor_tags:
#     print(article_link)
#     print(article_text)


# for tag in all_anchor_tags:
#     print(tag.get_text())
#     # print(tag.get("href"))


#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.get_text())
#     print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# h3_heading = soup.find(name="h3", class_="heading")
#
# name = soup.select_one(selector="#name")
# # print(name)
#
# headings = soup.select(".heading")
# print(headings)
