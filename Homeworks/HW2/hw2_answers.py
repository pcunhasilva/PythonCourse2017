from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import urllib2
import re
import csv

# Generate the links to the main.
# There are only 2 pages of petitions. I gen
url1 = ["https://petitions.whitehouse.gov/petitions?page=" + str(i) for i in range(0, 3)]

# Read the pages and collect the petitions' urls.
url2 = []
for i in url1:
    web_address = i
    web_page = urllib2.urlopen(web_address)
    soup = BeautifulSoup(web_page.read(), "html.parser")
    subsoup = soup.find(class_ = "view-content").find_all(class_ = "views-row")
    for i in range(0, len(subsoup)):
        d = subsoup[i].find("h3").find(href = True)['href']
        url2.append("https://petitions.whitehouse.gov" + d)

# Read each of the petitions pages and collect the required information
title = []
issues = []
sign = []
date = []
tags = []

for i in url2:
    web_address = i
    web_page = urllib2.urlopen(web_address)
    soup = BeautifulSoup(web_page.read(), "html.parser")
    title.append(soup.find("h1").text) # Add title
    date.append(soup.find("h4").text) # Add date (it needs to be cleaned)
    sign.append(soup.find("aside").find_all("div")[0].find_all("span")[4].text) # Add Signatures
    issues.append(soup.find("div", class_ = "field-item even").text)
    if len(soup.find("article").find_all("h6")) > 1:
        g = []
        for i in range(0, len(soup.find("article").find_all("h6"))):
            g.append(soup.find("article").find_all("h6")[i].text) # Get tags
        tags.append(g)
    else: tags.append(soup.find("article").find("h6").text)

# Remove special characters from the data:
#re.sub('[^a-zA-Z0-9-_*.]', '', my_string)
#title2 = [text.encode("utf8") for text in title]

# Put everything in a .csv file
with open('data_petitions.csv', 'wb') as f:
  my_writer = csv.DictWriter(f, fieldnames=("Title", "Date",
   "Issues", "Signatures", "Tags", "Url"))
  my_writer.writeheader()
  issues2 = [text.encode("utf8") for text in issues]
  title2 = [text.encode("utf8") for text in title]
  for i in range(0, len(url2)):
    my_writer.writerow({"Title":title2[i], "Date":date[i],
	"Issues":issues2[i], "Signatures":sign[i],
    "Tags":tags[i], "Url": url2[i]})
  print "File Saved"
