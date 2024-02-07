# Gusfield's Z Algorithm
Gusfield's Z algorithm creates a set of values that are how long the substring that matches the prefix of the string is.  It is often used as part of other algorithms in the string preprocessing step. 

## Complexity
Time complexity is O(n) where n is the length of the string

## How it Works
The the algorithm starts by searching through the array for a substring that matches the start of the array.  Once it finds this substring it marks it as the rightmost z box by getting the left and right index of the substring.  Then it populates all the z values within this box to match the start of the string.  As it is doing this, there are few things it does to change these values.  Firstly any z value that ends before the end of the end of the z box is left as it is.  If the value ends beyond the end of the z box then it is changed to end at the end of the z box.  Lastly if the z value ends on the same character as the current z box then the algorithm continues to search for matching characters and changes the rightmost z box to be this new z box.

## Directions or use
My implementation takes in a string and returns a list of z values.  I have also implemented a basic pattern matching algorithm using the z algorithm that runs in O(n + m) where n is the text being searched and m is the pattern.  This takes the text and substring as inputs.