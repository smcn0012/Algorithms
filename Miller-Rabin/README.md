# Miller Rabin
 Miller Rabin is a probabilistic primality test that uses repeated squaring to very quickly determine if a number has a factor.

## Complexity
time complexity is O(k*log(n)^3) where k is the number of tests and n is the number being primality tested.

## How it Works
The algorithm first factorises the number n - 1 into 2^s * t, where n is the number it is testing.  s then represents the shift or the number of 0 before the first 1 in the binary representation of the number and t is the significant bit component.  Then a witness is chosen randomly from the range 2 to n - 2.  Then mod(n) of the witness to the power of t is found.  Using this mod value and the repeated square method the algorithm finds the mods of all the numbers w ^ (2^i * t) where w is the witness and i is a number ranging from 1 to s.  During this pattern the algorithm looks for a result that is 1 or n-1.  This would mean that it cannot be said for sure that it isn't prime using that witness.  However if i reaches the value of s and the result is not 1 then the number is definitely composite.  Additionally if the number previous to a 1 is ever not congruent with +/- 1 then the algorithm also returns composite.

## Directions or use
My implementation takes two integers, one being the number to be tested and the other being the accuracy at which it is to be tested.  The algorithm returns True if the number was not determined to be composite and false if it was determined to be composite.