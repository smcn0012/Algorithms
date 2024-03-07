import random

def binToDec(binary):
    total = 0
    for i in range(len(binary)):
        total += int(binary[len(binary) - 1 - i]) * 2 ** i
    return total


def MillerRabin(number, accuracy):
    # check for even
    t = bin(number - 1)
    if t[-1] == 1:
        return False

    # Factorise n - 1 into 2^s * t
    shift = 1
    while t[-1-shift] == "0":
        shift += 1
    t = binToDec(t[2:(len(t) - shift)])


    counter = 1
    while counter <= accuracy:
        # Chose a witness get the first modulo
        witness = random.randint(2, number - 2)
        current_mod_result = (witness ** t) % number
        mod_results = [1 for _ in range(shift + 1)]
        mod_results[0] = current_mod_result

        # Recursively calculate the next modulo using the repeated square method
        for i in range(1, shift + 1):
            current_mod_result = (current_mod_result ** 2) % number
            mod_results[i] = current_mod_result
            if current_mod_result == 1:
                break

        # Case 1: a^{n-1} not congruent to 1 mod(number) 
        if current_mod_result != 1: 
            return False
        

        for i in range(1, shift):
            # Case 2: The previous mod result wasnt congruent to +/-1 mod(number) 
            if mod_results[i] == 1 and mod_results[i-1] != 1 and mod_results[i-1] != number - 1:
                return False
        
        # Case 3/4: Probably Prime
        counter += 1

    return True