# ece-140a-winter-2022-20aszulc
ece-140a-winter-2022-20aszulc created by GitHub Classroom

Name: Amber Szulc
PID: A16241551

Tutorial 1:
Install git ( I use windows). Github (internet) is the remote repository. My local computer is the  local repository
We have to clone the sample repository (this tutorial was directly opied off of ece 16, some of the refrences to ece 16 weren't changed.) 
to our local repo. You can create local repository with the github desktop or the command prompt(a lot more challenging). We have to create a
readme file and put something simple like "hi I am amber, I am a 2nd year engineering major." Add your local repository back onto github. First 
you have to pull from github to ensure the code matches and no merge conflicts (different edits) arise, then you can push your code. I wish they 
explained more how to resolve this confilict manually besides redoing all of it. This file also doesn't explain how to create a file organization system.

Tutorial 2
Download python and anaconda to help. I already have pycharm and atom, but I also have spyder now too. When I installed Jupyter my url had: http://localhost:8888/tree. 
I also saw some of my old coding projects I hadn't seen in years like my 10th grade python projects, and the websites I built with wordpress. My pip command didn't  it 
kept on getting errpr. Thus I checked with pip3

Tutorial 3
This is mainly working in command prompts, but we start with writing code in our spyder editor. Then we play the code in the command prompt using python 3. Next we go 
onto data types: ints, floats, etc... Then adding some unknown words to only c coders - tuples which are lists that are immtable using parentheses.  Python lists are 
in brackets like reptiles = ["snake", "lizard", "dragon"]. Get the length of the list by doing len(reptiles). you append by doing somethhing like
mixed_list.append(60) or del(animals[0]). This is getting us used to lists in a different formating then c programming, where the lack of semicolons seems the most pronounced 
difference when looking at single line commands. Making sublistsis similar to other languages like using reptiles[1:2] to onl take a subset. In python, strings cannot be changed
once its value is set. When I tried, my program  gave me errors. You can split string by certain punctuation of charactersIn looping, the for statements don't use parentheses 
of brakets unlike c, which was a bit strange to get use to. The python function is very strange formatting where a function if __name__ == __main__: since the  file will 
always be main. Also functions are defined differently by adding a def keyword which was differnt then c.

Tutorial 4
Web scraping is extrating data from a website. I have always wanted to learn this skill so I could find and search for things I like, and improve filtering processes to my taste. I didn't know you could also prevent scraping by doing rate limiting to preform a limited number of actions, or detecting unusual activity. This one taught you how to scrape quotes using the tags in the mref link. The first quote that always popped up first was albert Einstein. I added the soup.prettify and the made the strings have not just alphanumeric characters but ' and \n. Find all gets ever occurance of a specific category, for example of span tage in class "text". We have a mod index = index - 1 becausing index starts from 0. We also use the small tag and class autor  in order to find the author for our quote.

ANS1
  Is !DOCTYPE html an HTML tag? What is it doing in an HTML file?
  !DOCTYPE html is NOT an HTML tag. It is an "information" to the browser about what document type to expect. It is telling the browser to expect HTML. 

ANS2
  Change title to your name. Explain what changed in the webpage display on doing this in your README. Write "ANS2" at the beginning of your answer. 
The name of my webpage tab changed to my name.

ANS3
  Notice how we start with one tag and close with another. How does this even work? Explain in your README.md file. Write "ANS3" at the beginning of your answer.
  The heading (aka the first tag) overwrites the 2nd tag. Thus the heading is h2 even if the closing tag is h5.
  
ANS 4.1
Now refresh the page. Do you see any change? Explain what happened. Write "ANS4.1" at the beginning of your answer.
My webpage reverted back to its initial state when I didn't put in the new font or italicize

ANS 4.2
(iv) Make the style changes in the HTML file and now check the webpage. Do you see the changes upon refreshing? Explain. Write "ANS4.2" at the beginning of your answer. -->
 When refreshing, the new font and italics stayed on the webpage.

CHALLENGE 2 Web scraping questions: 
In which year did Barack Obama get the Nobel Peace Prize?
2009

When and for what did Ernest Rutherford win the Nobel Prize?
1908, chemistry

Who got the prize for Physics in 1939?
Ernest Orlando Lawrence

You can see in the code that I scraped the data to get these answers.

