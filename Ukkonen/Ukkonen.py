def Ukkonen_v1(text):
    bwt = []                #The output
    root = UkkonenNode()    #Root of the suffix tree
    root.children = [None for _ in range(91)]
    phase = [0]             #The phase (as an array to allow for global updates)
    extention = 0           #The extention
    current_node = root     #The current node being looked at
    pointer = extention     #The index of the character being examined
    link_node = root        #The node that should be linked to when a new rule 2 happens
    jump_node = root        #The node that should be jumped to after a rule 2
    link_jumped = False     #A boolean to represent whether or not the algorithm just jumped using a link
    rule3_count = 0
    rule3 = False

    while phase[0] < len(text):
        if rule3_count > 0 and rule3:
            char_index = ord(text[extention])-36
        else:
            char_index = ord(text[pointer])-36

        if current_node.children[char_index] is None: # rule 2 (adding leaf node)
            new_leaf_node = UkkonenNode()
            new_leaf_node.start = pointer
            new_leaf_node.end = phase # This will be the global end
            current_node.children[char_index] = new_leaf_node
            extention += 1
            current_node = jump_node
            link_jumped = True
            if current_node is root:
                link_jumped = False
            rule3 = False
        
        else:
            if rule3_count > 0 and rule3:
                skipable = phase[0] - extention - remainder
                current_node = current_node.children[ord(text[(phase[0] - (remainder + skipable))])-36]
                while current_node.end[0] -current_node.start <= skipable:
                    skipable -= (current_node.end[0] -current_node.start + 1)
                    current_node = current_node.children[ord(text[(phase[0] - (remainder + skipable))])-36]
                rule3_count -= 1
                    
            else:
                skipable = 0
                current_node = current_node.children[char_index]

            node_length = current_node.end[0] - current_node.start + 1
            
            if link_jumped:
                remainder = phase[0] - new_node_start + 1 # the number of characters before the new node needs to be created
                while remainder > node_length:
                    next_node = current_node.children[ord(text[phase[0]-(remainder - node_length)])-36]
                    if remainder - node_length < next_node.end - next_node.start:
                        jump_node = current_node.link
                        current_node = next_node
                    node_length = current_node.end - current_node.start 
            else:
                remainder = phase[0] - pointer + 1
            
            if node_length >=  remainder: # substring ends in node


                new_node_start = -1
                for i in range(remainder): # determining if it is rule 2 or 3
                    if text[pointer + i] != text[current_node.start + i + (skipable)]:
                        new_node_start = i
                        break
                    else:
                        remainder -= 1
                pointer = phase[0] - remainder + 1
                        
                if new_node_start != -1: # rule 2 (adding internal node)
                    # Instead of breaking links and relinking to the parent node, I will make the leaf node the internal node and replace it with a new leaf
                    replacement_leaf_node = UkkonenNode()
                    replacement_leaf_node.start = current_node.start + new_node_start + 1
                    replacement_leaf_node.end = phase # This will be the global end
                    current_node.end = [current_node.start + new_node_start] 
                    current_node.children = [None for _ in range(91)]
                    current_node.children[ord(text[replacement_leaf_node.start]) - 36] = replacement_leaf_node
                    current_node.link = link_node
                    pointer += new_node_start 
                    link_node = current_node
                    rule3 = False
                    
                else: # Rule 3
                    rule3_count += phase[0] - extention + 1
                    phase[0] += 1
                    link_node = root
                    link_jumped = False
                    current_node = root
                    rule3 = True
                    
                    
            
            else: # substring goes deeper than node
                pointer += node_length 
                jump_node = current_node.link
                link_jumped = False

        
        if extention > phase[0]: # reached the end of a phase
            phase[0] += 1
            link_node = root
            link_jumped = False
            current_node = root



    return bwt
    
class UkkonenNode:
    children = [] #[None for _ in range(91)]
    start = 0
    end = []
    link = None
    parrent = None
        


def Ukkonen_v2(text):
    bwt = []                #The output
    root = UkkonenNode()    #Root of the suffix tree
    root.children = [None for _ in range(91)]
    phase = [0]             #The phase (as an array to allow for global updates)
    extention = 0           #The extention
    current_node = root     #The current node being looked at
    link_node = root        #The node that should be linked to when a new rule 2 happens
    jump_node = root        #The node that should be jumped to after a rule 2
    link_jumped = False     #A boolean to represent whether or not the algorithm just jumped using a link
    remainder = 0
    num_checked = 0
    num_of_comparisons = 0
    checked_index = 0

    while phase[0] < len(text):
        char_index = ord(text[phase[0] - remainder + 1]) - ord('$')

        if num_checked > 0:
            count = num_checked
            while count > node_length:
                jump_node = current_node.link # storing the link from the previous node
                temp = current_node.end - current_node.start + 1
                current_node = current_node.children[ord(text[phase[0] + 1 - remainder]) - ord('$')]  # the next character in the remainder
                remainder -= temp # reducing the remainder by the amount skipped
                count -= temp
                node_length = current_node.end[0] - current_node.start + 1
    
        if current_node.children == []:
            current_node = current_node.parrent
        # rule 2
        if current_node.children[char_index] is None: # rule 2 (adding leaf node)
            new_leaf_node = UkkonenNode()
            new_leaf_node.start = phase[0] - remainder
            new_leaf_node.end = phase # This will be the global end
            new_leaf_node.parrent = current_node
            current_node.children[char_index] = new_leaf_node

            extention += 1
            remainder = phase[0] - extention + 1 #reset remainder for next extention
            
            current_node = jump_node
            if current_node is root:
                link_jumped = False
            else:
                link_jumped = True
            

            if num_checked != 0:
                num_checked -= 1
            
            
        else:
            current_node = current_node.children[char_index]

            node_length = current_node.end[0] - current_node.start + 1
            new_node_start = -1

            if link_jumped: 
                while remainder > node_length:
                    jump_node = current_node.link # storing the link from the previous node
                    temp = current_node.end - current_node.start + 1
                    current_node = current_node.children[ord(text[phase[0] + 1 - remainder]) - ord('$')]  # the next character in the remainder
                    remainder -= temp # reducing the remainder by the amount skipped
                    node_length = current_node.end[0] - current_node.start + 1
                '''
            el
                
                for i in range(remainder - count): # determining if it is rule 2 or 3
                    num_of_comparisons += 1
                    if text[phase[0] + 1 - remainder + count] != text[current_node.start + i + count]:
                        new_node_start = i
                        break
                    else:
                        remainder -= 1
                '''
            else:
                for i in range(remainder - num_checked): # determining if it is rule 2 or 3
                    num_of_comparisons += 1
                    if text[phase[0] + 1 - remainder + num_checked] != text[current_node.start + i + num_checked]:
                        new_node_start = i
                        break
                    else:
                        remainder -= 1
            
            if new_node_start != -1: # rule 2 (adding internal node)
                # Instead of breaking links and relinking to the parent node, I will make the leaf node the internal node and replace it with a new leaf
                replacement_leaf_node = UkkonenNode()
                replacement_leaf_node.start = current_node.start + new_node_start + 1
                replacement_leaf_node.end = phase # This will be the global end
                replacement_leaf_node.parrent = current_node

                current_node.end = [current_node.start + new_node_start] 
                current_node.children = [None for _ in range(91)]
                current_node.children[ord(text[replacement_leaf_node.start]) - ord('$')] = replacement_leaf_node
                current_node.link = link_node

                link_node = current_node
                
            else: # Rule 3
                #num_checked = phase[0] - extention + 1
                phase[0] += 1
                link_node = root
                link_jumped = False
                remainder += 1 # the new letter on the end
                #current_node = root
                    

        if extention > phase[0]: # reached the end of a phase
            phase[0] += 1
            link_node = root
            link_jumped = False
            remainder += 1 # the new letter on the end
            current_node = root

    return bwt
        
    


Ukkonen_v2("aaaba")