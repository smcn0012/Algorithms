'''
Implementation by: Spencer McNamara
'''

def BWT_Pattern_Match(bwt, suffix_array, count_matrix, rank_array, pattern):
    patterns = []
    start = 0
    end = len(bwt) - 1
    index = len(pattern) - 1
    while start <= end and index >= 0: # Iterating backwards through the pattern using the bwt to narrow down the location of the pattern
        start = rank_array[ord(pattern[index]) - 33] + count_matrix[ord(pattern[index]) - 33][start]
        end = rank_array[ord(pattern[index]) - 33] + count_matrix[ord(pattern[index]) - 33][end] - 1
        index -= 1
    if start <= end: # If there was an instance of the pattern found add the instances to the patterns array
        patterns = suffix_array[start:(end+1)]
    return patterns
    

def count_matrix_and_rank_array_naive(text, bwt):
    # This function naively gets the count matrix and rank array
    count_matrix = [[0 for _ in range(len(bwt))] for _ in range(0, 95)]
    rank_array = [0 for _ in range(0, 94)]
    count_array = [0 for _ in range(0, 94)]
    for index in range(len(bwt)): 
        if bwt[index] < len(text):
            character = text[bwt[index]]
            char_index = ord(character) - 33
            count_array[char_index] += 1
            count_matrix[char_index][index:] = [(count_matrix[char_index][index] + 1) for i in range(index, len(bwt))]
    rank = 1
    for index, count in enumerate(count_array):
        rank_array[index] = rank
        rank += count
    return count_matrix, rank_array

def bwt_and_suffix_array_naive(text):
    # This function naively gets the bwt and suffix array
    bwt = [len(text)-1]
    suffix_array = [len(text)]
    sorted_sufixes = []
    for i in range(len(text)):
        sorted_sufixes.append(text[i:])
    sorted_sufixes.sort()
    for i in range(len(text)):
        suffix_array.append(len(text) - len(sorted_sufixes[i]))
        bwt.append(len(text) - len(sorted_sufixes[i]) - 1)
    bwt[suffix_array.index(0)] = len(text)
    return bwt, suffix_array

# Example code
text = "googol"
pattern = "go"
bwt, suffix_array = bwt_and_suffix_array_naive(text)
count_matrix, rank_array = count_matrix_and_rank_array_naive(text, bwt)
print(BWT_Pattern_Match(bwt, suffix_array, count_matrix, rank_array, pattern))
