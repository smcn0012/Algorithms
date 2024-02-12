def lz77(text, window_size, lookahead_buffer_size):
    window = ""
    lookahead_buffer = text[:lookahead_buffer_size]
    lookahead_buffer_end = lookahead_buffer_size
    lookahead_buffer_start = 0
    code_list = []

    while lookahead_buffer_start < len(text):
        # Pattern search
        current_match = 0
        current_match_index = 0
        max_match = 0
        max_match_index = 0
        index = 0
        while index < len(window) and current_match < len(lookahead_buffer):
            if window[index] == lookahead_buffer[current_match]:
                current_match += 1
                if current_match == 1:
                    current_match_index = index
                if current_match >= max_match:
                    max_match = current_match
                    max_match_index = current_match_index
            else:
                current_match = 0
            if current_match >= len(lookahead_buffer):
                current_match = 0
            index += 1
        
        # Case where the buffer is larger than the window and the largest max may continue into the buffer
        if len(lookahead_buffer) > len(window) and current_match != 0:
            for i in range(len(lookahead_buffer) - len(window)):
                if lookahead_buffer[current_match] == lookahead_buffer[i]:
                    current_match += 1
                    if current_match > max_match:
                        max_match = current_match
                        max_match_index = current_match_index
                else:
                    break
        
        # Add new tuple
        next_char = ''
        if max_match >= len(lookahead_buffer):
            if lookahead_buffer_end < len(text):
                next_char = text[lookahead_buffer_end]

        else:
            next_char = lookahead_buffer[max_match]
        if max_match == 0:
            max_match_index = len(window)
        code_list.append([len(window) - max_match_index, max_match, next_char])


        # Shift the window
        window += lookahead_buffer[:(max_match + 1)]
        if len(window) > window_size:
            window = window[(len(window) - window_size):]

        # Shift the buffer
        lookahead_buffer = lookahead_buffer[(max_match + 1):]
        if lookahead_buffer_end < len(text):
            if max_match >= len(lookahead_buffer):
                window += text[lookahead_buffer_end]
                lookahead_buffer_end += 1
                lookahead_buffer += text[lookahead_buffer_end:(lookahead_buffer_end + max_match + 1)]
                lookahead_buffer_end += max_match
            else:
                lookahead_buffer += text[lookahead_buffer_end:(lookahead_buffer_end + max_match + 1)]
                lookahead_buffer_end += max_match + 1
        lookahead_buffer_start += max_match + 1
        
        
    
    return code_list

