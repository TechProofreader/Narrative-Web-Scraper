# Narrative-Web-Scraper
This is a simple script written with Python 3.7.3 that uses nautral language processing to analyze the narrative of a website's home/landing page, notably those of news websites.

Many people say that most news organizations have agendas and/or narratives that they like to instill in the information that they present to their audiences. What those narratives or agendas are can sometimes remain ambiguous, or blurred by the choice of layout and/or presentation of such information on said news organizations' websites. What this script aims to do is to ignore the layout and presentation of said information found on the selected website and instead view the information as one giant block of plain text and highlight the most common keywords presented on the website's home/landing page. 

Here's how it works:

1) We use Beautiful Soup to parse through the webpage's source code and ignore the markup to extract only the text as one giant block.
2) Next, we use the Natural Language Processing Toolkit (NLTK) to separate and tag each word in this text block as their respective type of speech.
3) From here, we ignore most unimportant forms of speech such as stopwords, and instead only focus on important keywords such as nouns and foreign words. What this does is highlight the webpage's focus, by bringing the most commonly used subject words to the forefront.
4) Then, we use Pandas to create a dataframe (chart) of our findings.
5) Lastly, we use Pandas to export our dataframe (chart) to a .csv file for storage and any further analysis. 

In summary, it can be confusing trying to understand what a news organization's aim is by way of how they commonly obfuscate their goal through confusing webpage layouts and organization schemes. By ignoring those things and simply looking at the most commonly used keywords, it becomes much easier to ascertain the news website's goals. It's much easier to look at only words such as nouns and foreign words, and perhaps even look at the adjectives being used to portray those nouns and foreign words, rather than visit a website and read over the entire page trying to piece together the organization's focus. For example, let's say there is a news organization whose website's homepage is littered with articles about vehicles, energy, science, and politics, but by just viewing their homepage alone, you cannot determine what their focus is. With this script, you could possibly extract keywords that may highlight that perhaps the news organization is against combustion vehicles and is trying to push a political agenda in support of electric only vehicle legislation, all by way of deduction through the dataset that the script produced for you. This script helps you arrive at your conclusion within seconds, rather than combing through the homepage and reading through article descriptions. Perhaps you're looking for coverage on a particular topic, but you would like to exclude certain viewpoints. The script could elucidate these viewpoints for you so that you avoid wasting your time on a website that is perhaps not even remotely what you were looking for. This script is not a catch all, but it is definitely a powerful little tool one could add to their toolbag. 

I consider this script mostly finished, but I will continue to test things such as alternative word taggers because as it stands, the NLTK's standard word tagger, Perceptron, still contains some inaccuracies that can get in the way of your data gathering. For example, it frequently tags symbols such as "+, -, {}, /" as nouns, when they are in-fact symbols. These types of issues are mostly related to the fact that the Perceptron tagger isn't trained on a massive model, so it sometimes has hiccups. However, it is mostly accurate, so it's quite easy to simply ignore inaccurately tagged words in your dataset and update the ordering or your acquired dataset. 

As such, I am planning to add some basic Python code that will iterate through the results produced by the NLTK tagged text and manually ignore the symbols that NLTK inaccurately tags, and produce an even more accurate dataset for creating the resulting dataframe. Using other taggers is possible, but they are not native and would require wrapping that may lead to bugs and/or inaccurate results. Also, you could manually tag characters/words/symbols with NLTK tokenizing, but this would then break the natural language processing functions within NLTK itself, so that defeats the purpose, which is why I have chosen not to go that route. NLTK does acknowledge that their taggers still require regular updating, so this behavior is at least expected. Lastly, to compensate for this possible behavior, it is good practice to choose a high word count such as 25 or 50 to produce good results since NLTK may misbehave and inappropriately tag something like "+" as a noun and present it as a heavily used word, thereby wasting a slot of your dataset, which if you choose to be small like say a word count of 10, could reveal nothing about the webpage you're trying to analyze. 

Note, that if you're trying to use this script for websites that are heavy on CSS, Javascript, etc, you may run into issues where your results appear to be random lines of markup. For such websites, the script will require tweaks to account for that type of website build, which is why I included a few lines of code in my script that will print out what the webpage is built with, so that you can adjust accordingly. Otherwise, the script works wonderfully for most modern webpages and produces quite interesting results. 

Finally, you will observe that I chose to be verbose with my filteredText list with the long line of excluded tags. I chose to be explicit with this function because I think it's important to be specific in this type of analysis, so I don't want any possibility of ambiguity by simply writing a line of code that just says "only look at nouns." I want to see what exactly my script is ignoring, so that there is less chance for confusing results. Also, you cannot simply filter out stopwords either because that stopword list is small and only encompasses certain types of words, while allowing other useless forms of speech in relation to the script's goal. 

As always with web scrapers, respect the robots.txt file of every website.

Enjoy!
