def elias(number):
    if number == 0:
        return '1'
    bin_num = bin(number + 1)[2:]

    def get_length_component(binary):
        new_lc_segment = bin(len(binary) - 1)[2:]
        if new_lc_segment == '1':
            return "0"
        new_lc_segment = "0" + new_lc_segment[1:]
        return get_length_component(new_lc_segment) + new_lc_segment
    
    return get_length_component(bin_num) + bin_num



