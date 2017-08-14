#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page

from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import urllib2
import re
import csv

# Open the main website
web_address = 'https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)

# Parse it
soup = BeautifulSoup(web_page.read(), "html.parser")

# Get the names
names = [n.get_text() for n in soup.select(".person-view-primary-field")]

# Get the specializion
spec = []
for i in soup.find_all('h3'):
	for j in i.next_siblings:
		# print j.name
		if j.name == 'h3': break
		if j.name == None: continue
		spec.append(i.text)

# Create the url file with the faculty's webpages
url = ["https://polisci.wustl.edu" + url['href'] for url in soup.findAll('a', href = True, class_ = "person-view-primary-field")]
url[16] = "https://polisci.wustl.edu/matthew_gabel" # Gabel is an exception.
url[32] = "https://polisci.wustl.edu/matthew_gabel" # So, I'm replacing to
													# his old website.
titles = []
emails = []
web = []
for i in url:
	web_address = i
	web_page = urllib2.urlopen(web_address)
	soup = BeautifulSoup(web_page.read(), "html.parser")
	titles.append(soup.find("div", \
	class_ = "field-name-field-person-titles").findChildren()[0].get_text())
	classes = []
	for i in soup.find_all(class_ = True):
    	 classes.extend(i["class"])
	if "field-name-field-person-email" in classes:
		emails.append(soup.find("div", \
		class_ = "field-name-field-person-email").find(\
		class_ = "field-item").get_text())
	else:
		emails.append(None)
	if "field-name-field-person-website" in classes:
		web.append(soup.find(\
		class_ = "field-name-field-person-website").findChildren()[-1]['href'])
	else:
		web.append(None)

# Put everything in a dictionary and save in a .csv file
with open('data_test.csv', 'wb') as f:
  my_writer = csv.DictWriter(f, fieldnames=("Name", "Specialization",
   "Titles", "Webpage", "E-mail"))
  my_writer.writeheader()
  for i in range(1, 42):
    my_writer.writerow({"Name":names[i], "Specialization":spec[i],
	"Titles":titles[i], "Webpage":web[i], "E-mail":emails[i]})
  print "File Saved"
