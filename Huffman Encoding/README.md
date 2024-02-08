# Huffman Encoding
Huffman encoding is a prefix free encoding method that uses the frequency of the characters in the text to make more frequent characters have shorter codes proportionally to their occurance frequency.

## Complexity
The time complexity is O(nlog(n)) where n is the length of the text

## How it Works
Firstly the algorithm creates a list of ordered pairs that is the length of the domain of printable ascii characters.  Then for each character it finds the number of times it is used in the text.  It then shortens the list to only include characters with at least one character.  The list is then sorted from most used to least used.  A tree is then constructed where the least used characters are combined into one node and then puts that node back into the sorted list using the combined number of occurances.  If there is ever an occurance tie then the shallower node takes priority to decrease the depth of the tree.  Once the tree is constructed, the algorithm does a recursive iteration through the tree to create the codes for all the characters.

## Directions or use
My implementation takes a string input and outputs a list of ordered pairs where the first of each pair is the character and the second is the code, both are stored as strings.