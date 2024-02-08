def huffman(text):
    # Getting the occurances
    occurances = [[0] for _ in range(127)]
    for i, occurance in enumerate(occurances):
        occurance.insert(0, chr(i))
    for char in text:
        occurances[ord(char)][1] += 1
    index = 0

    # Cleaning up the occurance list
    while index < len(occurances):
        if occurances[index][1] == 0:
            del occurances[index]
        else:
            index += 1
    
    # Use this later
    encoded_values = []
    encoded_values_index = []
    for value in occurances:
        encoded_values.append([value[0], value[1]])
        encoded_values_index.append(value[0])

    # Initial sort
    for i, char in enumerate(occurances):
        for j in range(i):
            if char[1] <= occurances[j][1]:
                occurances.insert(j, char)
                del occurances[i + 1]
                break
    
    class Huffman_node:
        def __init__(self, n0, n1):
            self.n0 = n0
            self.n1 = n1

    # Tree construction
    while len(occurances) > 1:
        new_count = occurances[0][1] + occurances[1][1]
        for i, char in enumerate(occurances):
            if char[1] > new_count:
                occurances.insert(i, [Huffman_node(occurances[0][0], occurances[1][0]), new_count])
                del occurances[:2]
                break
            if i == len(occurances) - 1:
                occurances.append([Huffman_node(occurances[0][0], occurances[1][0]), new_count])
                del occurances[:2]
                break
    
    def get_encoded_values_from_tree(node, current_code, encoded_values):
        if type(node.n0) == type('a'):
            encoded_values[encoded_values_index.index(node.n0)][1] = current_code + "0"
        else:
            get_encoded_values_from_tree(node.n0, current_code + "0", encoded_values)
        if type(node.n1) == type('a'):
            encoded_values[encoded_values_index.index(node.n1)][1] = current_code + "1"
        else:
            get_encoded_values_from_tree(node.n1, current_code + "1", encoded_values)

    get_encoded_values_from_tree(occurances[0][0], "", encoded_values)

    return encoded_values
