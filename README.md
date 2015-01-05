
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

With the code I made here, by telling it what file you use, and what type of edge you want to make
(either Directed or Undirected. you have to.) you can easily make an edge list. 

So

1. put this python file into the same directory as your target csv file.
2. open Terminal and run the code.
3. follow what the code says by typing the name of the targe csv file, and the type of edges you desire.
4. A new file will be created with the prefix "done_"

done!
Thank you!

