def z_algorithm_pattern_match(substring, text) -> list:
    concat = substring + text
    z_values = z_algorithm(concat)
    match_index_list = []
    for index, z_value in enumerate(z_values):
        if z_value >= len(substring):
            match_index_list.append(index)
    return match_index_list


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
