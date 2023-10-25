# Karatsuba's Algorithm
Karatsuba's algorithm is for fast integer multiplication for integers with the same bit length.  

## Complexity
Time complexity is O()

## How it Works
The basic idea of the algorithm is a divide and conquor approach where you split one multiplication
down into three smaller multiplications.  This is done using the following equation:
(2^2D + 2^D)*U1*V1 - 2^D*(U1 - U0)*(V1 - V0) + (2^D + 1)*U0*V0
Where the numbers are both 2D-bit numbers and they are split into two D-bit numbers V and U where V
is the first D bits of a number and U is the last D bits of the number.
The recursion stops at the word size.

## Directions or use
The parameters num1 and num2 must be decimal itegers that have the same number of bits when converted to binary.  That is, 2^(b - 1) <= (num1 and num2) <= 2^b - 1 where b is a positive integer.  The num_of_bits parameter is the number of bits required to represent the number.  With reference to the equation above, b is the number of bits.  Lastly the word_size parameter defines the base case for the recursion, for real use of this algorithm this will be the word size of the OS, but in my implementation I have left it so the word size can be passed in as an argument.