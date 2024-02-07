# Elias (Omega) Encoding
 Elias encoding is a prefix free method of encoding variable length integers.

## Complexity
Time complexity is O(log(b)) where b is the number of digits in the binary representation of the number.

## How it Works
Elias encoding has two parts, the length component and a binary number.  The length component is made up of segments that all start with 0, these segments contain the length of the next segment minus 1 in binary with the first bit flipped to start with 0.  When the first bit is 1 then it is the start of the binary number and the previous segment tells the decoder how many bits are in the binary number.  The algorithm recursively calculates the length component segments then adds the binary to it once the next segment is too small.

## Directions or use
My implementation takes a decimal number and converts it to binary but it could easily be changed to just have the recursive component taking in a binary.