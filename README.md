
This short Python code is made to tranform a list of items into a edge list that can be processed on Gephi.
(This is my first time to upload my code on github, so please bear my misunderstanding on how to use this...
not even sure it's okay to write this on this file?)

anyway.

let's say you have a csv file of items that are bought together (like from a supermarket..)
Apple, Banana, Pear
Pear, Banana
Banana, PineApple

In order for you to put this into Gephi, one of many things you can do is to make possible unique pairs like..
Apple, Banana
Banana, Pear
Pear, Banana
Banana, PineApple

It's faster to do it manually, but if you have more than 30 items on one line, then it's kinda cumbersome.

With the code I made here, by telling it what file you use, you can easily make an edge list. 

So

0. Download "Convert Excel and csv files to networks (including dynamic!)" plugin from Gephi.
1. put this python file into the same directory as your target csv file.
2. open Terminal and run the code.
3. follow what the code says by typing the name of the targe csv file.
4. A new file will be created with the prefix "done_"
5. And SAVE WITH ENCODING > UTF-8.
6. Open Gephi > (with the given open menu) select the csv file that you've just changed.
7. Select the type of edges (Directed or Undirected)
8. Done!

done!
Thank you!

