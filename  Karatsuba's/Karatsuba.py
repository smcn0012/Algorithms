'''
Implementation by: Spencer McNamara
'''

# Function to convert Binary to Decimal
def binToDec(binary):
    total = 0
    for i in range(len(binary)):
        total += int(binary[len(binary) - 1 - i]) * 2 ** i
    return total

def Karatsuba(num1, num2, num_of_bits, word_size):
    # Base case when number of bits is not more than the word size
    if num_of_bits <= word_size:
        return num1 * num2
    
    bin_num1 = bin(num1)[2:]
    bin_num2 = bin(num2)[2:]

    # Check for negatives
    num1_neg = 1
    num2_neg = 1
    if bin_num1[0] == 'b':
        bin_num1 = bin_num1[1:]
        num1_neg = -1
    if bin_num2[0] == 'b':
        bin_num2 = bin_num2[1:]
        num2_neg = -1

    # Pad 0s to make sure number has the correct num of bits
    while len(bin_num1) < num_of_bits:
        bin_num1 = "0" + bin_num1
    while len(bin_num2) < num_of_bits:
        bin_num2 = "0" + bin_num2

    # Pad a 0 if the num of bits is odd
    if num_of_bits % 2 == 1:
        bin_num1 = "0" + bin_num1
        bin_num2 = "0" + bin_num2
        num_of_bits += 1

    # Divide and conquor
    new_num_of_bits = num_of_bits // 2
    u1 = num1_neg * binToDec(bin_num1[:new_num_of_bits])
    u0 = num1_neg * binToDec(bin_num1[new_num_of_bits:])
    v1 = num2_neg * binToDec(bin_num2[:new_num_of_bits])
    v0 = num2_neg * binToDec(bin_num2[new_num_of_bits:])
    u_dif = u1 - u0
    v_dif = v1 - v0
    
    # (2^2D + 2^D)*U1*V1 - 2^D*(U1 - U0)*(V1 - V0) + (2^D + 1)*U0*V0
    return (2 ** num_of_bits + 2 ** new_num_of_bits) * Karatsuba(u1, v1, new_num_of_bits, word_size) - (2 ** new_num_of_bits) * Karatsuba(u_dif, v_dif, new_num_of_bits, word_size) + (2 ** new_num_of_bits + 1) * Karatsuba(u0, v0, new_num_of_bits, word_size)

