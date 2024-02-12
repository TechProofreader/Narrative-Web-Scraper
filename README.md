# Narrative-Web-Scraper

_Note: This is a Beginner Level program that you can use to further your Python knowledge by first learning how the base program works, and then extending the program with your own additions. Please know, however, that this project can elevate to a Moderate or Hard level depending on how far you take the Natural Language Processing component._

This is a simple script written with Python 3.7.3 that uses nautral language processing to analyze the narrative of a website's home/landing page, to assist in understanding what type of narrative (or not) the website/organization is pushing. 

For example, many people say that most news organizations have agendas and/or narratives that they like to frame their web content with. What those narratives or agendas are can sometimes remain ambiguous or blurred by the choice of layout and/or how they choose to present the text content on their websites. What this script aims to do is to ignore the layout and presentation of said information found on the selected website and instead view the information as one giant block of plain text and highlight the most common keywords presented on the website's home/landing page. 

Here's how it works:

1) We use Beautiful Soup to parse through the webpage's source code and ignore the markup to extract only the text as one giant block.
2) Next, we use the Natural Language Processing Toolkit (NLTK) to separate and tag each word in this text block as their respective type of speech.
3) From here, we ignore most unimportant forms of speech such as stopwords, and instead only focus on important keywords such as nouns and foreign words. What this does is highlight the webpage's focus, by bringing the most commonly used subject words to the forefront.
4) Then, we use Pandas to create a dataframe (chart) of our findings.
5) Lastly, we use Pandas to export our dataframe (chart) to a .csv file for storage and any further analysis. 

Note, that if you're trying to use this script for websites that are either heavy on CSS/Javascript and/or are poorly formatted, you may run into issues where your results appear to be random lines of markup mixed in with some actual words. For such websites, the script will require tweaks to account for that type of website build, which is why I included a few lines of code in my script that will print out what the webpage is built with, so that you can adjust accordingly. Otherwise, the script works wonderfully for most modern webpages and produces quite interesting results. For websites with which some tweaks still do not present the expected results, it is instead recommended to use Selenium to scrape, as it will view the webpage much like a real browser does and will not confuse the markup with the text content. 

For those who are looking to learn about constructing web scrapers, fear not for I have chosen to annote my script with verbose comments so that you can better understand every part of it at every stage of action.

As always with web scrapers, respect the robots.txt file of every website.

Enjoy!
