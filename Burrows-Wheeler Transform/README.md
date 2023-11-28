# Burrows-Wheeler Transform Pattern Matching
 BWT pattern matching is an exact pattern matching algorithm.

## Complexity
Time complexity is O(m) where m is the length of the pattern
*There is some preprocessing that adds time up front*

## How it Works
Firstly the algorithm starts by setting two pointers, the start and end pointers.  These pointers start at the start and end of the BWT respectivly.  The algorithm starts iterating through the pattern in reverse order.  For each character in the iteration the algorithm searches for a set of matching characters between the start and end in the suffix array using the count and rank arrays.  The start and end pointers are then updated to point at the start and end of that set of characters.  This process repeats until either the end of the pattern is reached in which case a set of matches has been found or if the start pointer is ever before the end pointer, which indicates no matches exitst.

## Directions or use
My implementation takes the preprocessed BWT, suffix array, count and rank arrays.  I have put in functions to get them naively but these can be replaced or not used if those are given.  The output of the function is a set of indicies which are the starting indicies of the matches.