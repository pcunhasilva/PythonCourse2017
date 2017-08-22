import re

# open text file of 2008 NH primary Obama speech
file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()

# compile the regular expression
keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
  if keyword.search(line):
    print line

# TODO: print all lines that DO NOT contain "the "
for line in text:
    if not keyword.search(line):
        print line

# TODO: print lines that contain a word of any length starting with s and ending with e
allwords = re.findall(r"\bs\w*e\b", " ".join(str(x) for x in text))
for line in text:
    for i in range(len(allwords)):
        if str(allwords[i]) in line:
            print line

# date = raw_input("Please enter a date in the format MM.DD.YY: ")
# Print the date input in the following format:
# Month: MM
# Day: DD
# Year: YY
