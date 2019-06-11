# Narrative-Web-Scraper
This is a simple script written with Python 3.7.3 that uses language processing to analyze the narrative of a website's home/landing page, notably those of news websites.
Many people say that most news organizations have agendas and/or narratives that they like to instill in the information that they present to their audiences. What those narratives or agendas are can sometimes remain ambiguous, or blurred by the choice of layout and/or presentation of such information on said news organizations' websites. What this script aims to do is to ignore the layout and presentation of said information found on the selected website and instead view the information as one giant block of plain text and highlight the most common keywords presented on the website's home/landing page. 

Here's how it works:

1) We use Beautiful Soup to parse through the webpage's source code and ignore the markup to extract only the text as one giant block.
2) Next, we use the Natural Language Processing Toolkit (NLTK) to separate and tag each word in this text block as their respective type of speech.
3) From here, we ignore most unimportant forms of speech such as stopwords, and instead only focus on important keywords such as nouns and foreign words. What this does is highlight the webpage's focus, by bringing the most commonly used subject words to the forefront.
4) Then, we use Pandas to create a dataframe (chart) of our findings.
5) Lastly, we use Pandas to export our findings to a .csv file for storage and any further analysis. 

In summary, it can be confusing trying to understand what a news organization's aim is by way of how they commonly obfuscate their goal through confusing webpage layouts and organization schemes. By ignoring those things and simply looking at the most commonly used keywords, it becomes much easier to ascertain the news website's goals. 

I consider this script mostly finished, but I will continue to test things such as alternative word taggers because as it stands, the NLTK's standard word tagger, Perceptron, still contains some inaccuracies that can get in the way of your data gathering. For example, it frequently tags symbols such as "+, -, {}, /" as nouns, when they are in-fact symbols. These types of issues are mostly related to the fact that the Perceptron tagger isn't trained on a massive model, so it sometimes has hiccups. However, it is mostly accurate, so it's quite easy to simply ignore inaccurately tagged words in your dataset and update the ordering or your acquired dataset. 

As such, I am planning to add some basic Python code that will iterate through the results produced by the NLTK tagged text and manually ignore the symbols that NLTK inaccurately tags, and produce an even more accurate dataset for creating the resulting dataframe. Using other taggers is possible, but they are not native and would require wrapping that may lead to bugs and/or inaccurate results. Also, you could manually tag characters/words/symbols with NLTK tokenizing, but this would then break the natural language processing functions within NLTK itself, so that defeats the purpose, which is why I have chosen not to go that route. 
