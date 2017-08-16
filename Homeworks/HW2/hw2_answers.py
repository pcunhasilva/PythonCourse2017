from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import urllib2
import re
import csv

# Generate the links to the main.
# There are only 3 pages of petitions.
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

# Clean date
date2 = [date[i].split(" on ")[1] for i in range(0, len(date))]

# Remove special characters from the issues:
# issues2 = [re.sub(r'[^\s\w_]+', '', issues[i]) for i in range(0, len(issues))]
issues2 = [re.sub('[^a-zA-Z0-9\\\/ #]|_', '', \
    issues[i]) for i in range(0, len(issues))]

# Merge mutilple tags into one
tags2 = []
for i in range(0, len(tags)):
    # bc = 'on' if c.page=='blog' else 'off'
    if len(tags[i]) == 1 or len(tags[i]) > 5:
        tags2.append(tags[i])
    else:
        tags2.append(", ".join(str(x) for x in tags[i]))

# Encode titles
title2 = [text.encode("utf8") for text in title]

# Put everything in a .csv file
with open('data_petitions.csv', 'wb') as f:
  my_writer = csv.DictWriter(f, fieldnames=("Title", "Date",
   "Issues", "Signatures", "Tags", "Url"))
  my_writer.writeheader()
  for i in range(0, len(url2)):
    my_writer.writerow({"Title":title2[i], "Date":date2[i],
	"Issues":issues2[i], "Signatures":sign[i],
    "Tags":tags2[i], "Url": url2[i]})
  print "File Saved"
