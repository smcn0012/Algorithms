# LZ77 Encoding
LZ77 Encoding is a method of lossless data compression that uses refrences to past substrings within a window to give information about the next substring.  

## Complexity


## How it Works
The algorithm first looks for the longest substring within window that matches the start of the lookahead buffer.  Once found it records how far back the matching substring started from the current part of the pattern, then it records the length of the substring and finally it records the next character in the lookahead buffer.  It then puts those two numbers and the character in a tuple.  Lastly before creating the next tuple the algorithm moves the window and lookahead buffer to be centred around the character after the character in the previous tupple

## Directions or use
My implementation takes a string input as well as two ints for the window and lookahead buffer.  The ints define the size of the window and buffer respectively.  My implementations returns a list of tupples.  My implementation uses a naive search so can be improved by using z-algorithm or boyer-moore.