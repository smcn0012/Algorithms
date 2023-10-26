# Boyer-Moore's Algorithm
 Boyer-Moore's is an exact pattern matching algorithm.

## Complexity
Time complexity is O(n) where n is the length of the text
*There is some preprocessing that adds time up front*

## How it Works
The algorithm goes through the text comparing the pattern to parts of the text starting at the end of the pattern and working towards the start.  The algorithm uses two types of shifts to rapidly skip through the text.  The first type of shift is a bad character shift where the search index shifts to allign the bad character (the character that didn't match the pattern)  with its next occurance in the pattern.  This occurance is found using the bad character matrix which has the next character of each character at each index in the pattern.  The other type of shift is a good suffix shift which lines up the matched part of the pattern with the right most instance of that matched part within the pattern.  Then there is matched prefix array which is a back up if no good suffix instance is found or if an instance of the pattern was found.  In addition to this, galil's optimisation skips characters that have been checked by the good suffix or matched prefix.

## Directions or use
My implementation does the preprocessing of the pattern within the function.  It can be modified easily to take the preprocessed results as parameters.  Otherwise the two parameters are the pattern and the text.  In addition I have used my own implementation of Gusfeild's Z algorithm as part of the preprocessing.