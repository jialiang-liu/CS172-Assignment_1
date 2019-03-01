## Basic Information
Python Version: 3.6
OS:  Mac OS 10.14

## File Directory
├── `README.md`  
├── `data`  
&ensp;&ensp;&ensp;&ensp;&ensp;├── `file01.txt`  
&ensp;&ensp;&ensp;&ensp;&ensp;├── `file02.txt`  
&ensp;&ensp;&ensp;&ensp;&ensp;├── ......  
&ensp;&ensp;&ensp;&ensp;&ensp;├── `file20.txt`    
├── `project.py`  
├── `project_with_stemmer.py`  
├── `stoplist.txt`  

## Code Design
For problems associate with machine learning and crawling, Python is the best choice for coding. But it's "lack" of data structures makes it more complicated to design the structure of index table. But a good outcome is I can design my own structure that is the best fit of our purpose.

The code is basically 4 parts: structure of the index table, reading stopwords and documents while generating the indices, scoring, and the test (output) part.
+ For the data structure, my first idea was to write a class for hashtable, because I'm aware that it's possible. But it's seems complicated and unnecessary, so I started to think about other structures. Array was a choice, but the time complexity is too high for search operations. Then I thought about dictionary. It was designed with hashtable, can search fast, and have "key" and "value". For value, I used linked list, since the figures from lectures look just like it. The linked list contains the postings of those documents have the "key", and the number of documents contains the "key" is kept by property "length" of the list. 
+ For reading documents, I read those lines (words) into a list for each document and stoplist. Then go through the word lists, filter the stop-words, and create or update nodes in the index table based on the terms. The document indices can be easily got from the length of the word lists.
+ For scoring, I write some basic functions in the data structure. With those functions, I can easily search for the frequency of a term in a document, and for the number of documents the term occurred in. The TFIDF uses formula from lectures to calculate weights, and prints them out nicely. When calculating IDF, I check for n_k == 0, instead of using n_k + 1, since the value can be too high, I don't like it. So when the term is not in any document, its TFs, IDFs, TF-IDFs will all be 0.
+ For testing, it just keeps asking for a query, and call TFIDF() to give the answer. Only "QUIT" is case sensitive in my program, so "quit", "Quit", or "qUIt" are all queries as "quit", and "QUIT" is to exit.

## Using Instructions
+ `Q1.pdf` is my answer for Problem 1, it contains all the answers, with citations for the programming problem.
+ `project.py` is my code for this assignment. It satisfies all the requirements, to take a query, and search for the exact term, as "years" is different with "year". The url at the end is regarded as one term, so it won't count even if the term is inside the url.
+ `project_with_stemmer.py` is a small update of my original program. I import NLTK into the code to use Porter Stemmer, so "years" will be considered as "year" in both query and documents.
***PLEASE DO NOT change any file structure. My code will get the path of itself, and find other files based on the current structure.***
1. Use `chmod` to give permission to run the code;
2. Install Python 3, since Python 2 is not able to execute the code for some syntax changes;
3. Run "project.py";
4. Input the term for query. it's NOT case sensitive, as "images" is the same as "ImaGEs", except for "QUIT". "quit" is a query term in my code, while "QUIT" means to exit.
5. Wait for the program to give answers. The documents will be in order of TF-IDFs of the query.
