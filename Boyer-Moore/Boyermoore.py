'''
Implementation by: Spencer McNamara
'''

def Boyermoore(pattern, text):
    pattern_occurances = [] # list of indexes where the pattern occurs in the text
    search_index = len(pattern) - 1 # current index of the start of the right to left search in the text
    bcm = bad_character_matrix(pattern)
    gsa = good_suffix_array(pattern)
    mpa = matched_prefix_array(pattern)
    gallil_shift = 0 # for gallil's optimization

    while search_index < len(text): # search until the end of the text
        suffix_length = 0 + gallil_shift 

        while pattern[len(pattern) - 1 - suffix_length] == text[search_index - suffix_length] and suffix_length < len(pattern): # search right to left
            suffix_length += 1

        if suffix_length == len(pattern): # the pattern was found
            pattern_occurances.append(search_index - suffix_length + 1)

            # shifting using matched prefix array
            search_index += len(pattern) - mpa[1]
            gallil_shift = mpa[1]
        else:
            # calculating bad character shift
            bad_character = text[search_index - suffix_length]
            bc_shift = len(pattern) - bcm[ord(bad_character) - 33][len(pattern) - 1 - suffix_length] # 33 is the first printable ascii character

            # calculating good suffix shift
            gs_shift = gsa[len(pattern) - suffix_length]
            if gs_shift == 0 and suffix_length != 0:
                gs_shift = mpa[len(pattern) - suffix_length]
                suffix_length = gs_shift

            # determining which shift to use
            if bc_shift > gs_shift:
                search_index += bc_shift
                gallil_shift = 0
            else:
                search_index += gs_shift
                gallil_shift = suffix_length

    return pattern_occurances


def bad_character_matrix(pattern):
    bad_character_matrix = [[0 for _ in range(0, len(pattern))] for _ in range(0, 94)] # 94 is the number of printable ascii characters
    
    for i in range(0, len(pattern)):
        bad_character_matrix[ord(pattern[i].lower()) - 33][i:] = [i + 1 for k in range(i, len(pattern))] # 33 is the first printable ascii character
    
    return bad_character_matrix


def z_algorithm(text) -> list:
    z_values = [0 for _ in range(len(text))]
    left = 0
    right = 0
    for index in range(1, len(text)):
        if index > right: # index is past the rightmost z box
            if text[index] == text[0]:
                left = index
                right = index
                search_index = 1
                while index + search_index != len(text): # find the length of the z box and record the new rightmost point
                    if text[index + search_index] != text[search_index]:
                        break
                    right = index + search_index
                    search_index += 1
                z_values[index] = right - index + 1
        else: # index is within the rightmost z box
            known_value = z_values[index - left]
            if known_value < right - index + 1: # the known sub-z-box ends before the current rightmost z-box
                z_values[index] = known_value
            else: # the known sub-z-box ends at the same place or after as the current rightmost z-box
                if known_value == right - index + 1: # if it ends at the same place
                    search_index = 1
                    while right + search_index < len(text): # find the length of the z box and record the new rightmost point
                        if text[right + search_index] != text[search_index + right - index]:
                            break
                        search_index += 1
                    right = right + search_index - 1
                    if search_index != 1: # there is a new right most z box
                        left = index
                z_values[index] = right - index + 1
    return z_values

def good_suffix_array(pattern):
    good_suffix_array = [0 for _ in range(0, len(pattern) + 1)]
    z_values = z_algorithm(pattern[::-1])
    z_values = z_values[:0:-1] # remove the last element that will be the length of the pattern
    for index, z_value in enumerate(z_values):
        good_suffix_array[len(pattern)-z_value] = index
    return good_suffix_array

def matched_prefix_array(pattern):
    matched_prefix_array = [0 for _ in range(0, len(pattern) + 1)]
    z_values = z_algorithm(pattern[::-1])
    z_values = z_values[::-1] # remove the last element that will be the length of the pattern
    current_max = 0
    for index, z_value in enumerate(z_values):
        if z_value > current_max:
            current_max = z_value
        matched_prefix_array[len(pattern)-index] = current_max
    matched_prefix_array[0] = len(pattern)
    return matched_prefix_array
