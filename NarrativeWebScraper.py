# Author: Ryan Reyes, github.com/TechProofreader
# Program Name: Narrative Web Scraper
# Version: 1.0

import pandas as pd
import nltk
import requests
from bs4 import BeautifulSoup
from collections import Counter

# The headers section is where we will "mask" our script as a web browser so as not to get insta-blocked by websites.
# You need to have an actual user_agent listed and a referer. The user_agent tells the website how you are accessing
# their website (via the web browser), and the referer tells the website how you got to their website (via google).
headers = {
        'user_agent': 'type your user agent info here',
        'referer': 'https://www.google.com/'
}

# Points program at the website you want to scrape. The timeout tells the program to cancel the request if a server response is not received
# within the specified amount of seconds (this is done to prevent the program from hanging infinitely).
page = requests.get("url goes here", headers=headers, timeout=3.0)

# This block of code checks the content type of the page (HTML, XML, etc)
h = requests.head("url goes here")
header = h.headers
contentType = header.get('content-type')
print(contentType)

soup = BeautifulSoup(page.text, "html.parser") #captures entire webpage's text with markup (html, etc)
x = soup.text # removes the markup and captures only the text

taggedText = nltk.tag.pos_tag(x.split())
filteredText = [word for word, tag in taggedText if tag != 'JJ' and tag != 'JJS' and tag != 'JJR' and tag != 'CC' and tag != 'DT' and tag != 'IN' and tag != 'RB' and tag != 'RBR' and tag != 'RBS' and tag != 'VB' and tag != 'VBD' and tag != 'VBG' and tag != 'VBN' and tag != 'VBP' and tag != 'VBZ' and tag!= 'LS' and tag != 'PDT' and tag != 'SYM' and tag != 'RP' and tag != 'TO' and tag != 'WDT' and tag != 'WP' and tag != 'WRB' and tag != 'WP$' and tag != 'PRP' and tag != 'PRP$' and tag != 'MD']
# Note: filteredText is removing all words associated with the tags found in its list and creating
# a new, filtered version of soup.text, but without the words that we filtered out. This new filtered
# text block is contained in the "filteredText" variable even though it also acts as the filter itself. 

Counter = Counter(filteredText) # wordcount of filteredText
mostOccuring = Counter.most_common(50) # finds the 50 most commonly used words from filteredText; you can choose any number of words, as long as it isn't larger than the number of words in your data set.
commondWordsChart = pd.DataFrame(mostOccuring, columns = ['Word', 'Count']) # converts findings from mostOccurring into a Pandas Chart
print(commondWordsChart)

# This saves the Pandas Dataframe (chart) to a .csv file. Where it says "path/fileName.csv" is where you
# would type where you want to save the file (the "path") and what you want to name it (fileName).
# Always remember to end your file name with ".csv", otherwise this action will fail.
commondWordsChart.to_csv(r'path/fileName.csv', index=False)

Exit
