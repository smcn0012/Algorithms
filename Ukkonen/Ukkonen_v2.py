class Node:
    def __init__(self, start, end, depth, link = None) -> None:
        self.start = start
        self.end = [end]
        self.children = [None for _ in range(ord('~') - ord('$') + 1)]
        self.link = link
        self.depth = depth

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end[0]

    def getChild(self, char_index):
        return self.children[char_index]
    
    def addChild(self, char_index, child):
        self.children[char_index] = child
    
    def getLink(self):
        return self.link

    def setLink(self, link):
        self.link = link
    
    def becomeBranch(self, end, link):
        self.end = [end]
        self.setLink(link)

    def setGlobalEnd(self, global_end):
        self.end = global_end

    def getLength(self):
        return self.end[0] - self.start + 1

    def getDepth(self):
        return self.depth
    
    def getBWTArray(self, max_depth, global_end):
        suffix_array = []
        if self.getEnd() == global_end[0]:
            suffix_array = [max_depth - self.getDepth() - self.getLength()]
        else:
            for node in self.children:
                if node is not None:
                    suffix_array = suffix_array + node.getBWTArray(max_depth, global_end)
        return suffix_array
    
class SuffixTree:
    def __init__(self, text, explicit: bool = True) -> None:
        self.text = text
        self.explicit = explicit
        if explicit:
            self.text += '$'
        self.global_end = [0]
        self.root = Node(-1, -2, 0)
        self.root.setLink(self.root)
        self.Ukkonen()
        self.bwt = ""

    def char_index(self, text_index_of_char):
        return ord(self.text[text_index_of_char]) - ord('$')
    
    def incriment_global_end(self):
        self.global_end[0] += 1

    def addBranchToLeaf(self, end, link: Node, leaf: Node):
        leaf.becomeBranch(end, link)
        self.addLeafNode(end + 1, leaf.getDepth() + end - leaf.getStart() + 1, leaf)
    
    def addBranchToBranch(self, end, link: Node, branch: Node):
        new_branch = Node(end + 1, branch.getEnd(), branch.getDepth() + end - branch.getStart(), branch.getLink)
        new_branch.children = branch.children
        branch.children = [None for _ in range(ord('~') - ord('$') + 1)]
        branch.end = [end]
        branch.setLink(link)
        branch.addChild(self.char_index(end + 1), new_branch)    

    def addLeafNode(self, start, depth, branch: Node):
        new_leaf = Node(start, 0, depth)
        new_leaf.setGlobalEnd(self.global_end)
        branch.addChild(self.char_index(start), new_leaf)

    def Ukkonen(self):
        phase = 0
        extention = 0
        text_pointer = 0
        current_node = self.root
        jumped = False
        added_branch = False
        previous_branched_node = self.root
        parent = self.root
        
        while phase < len(self.text):

            # skip_counting
            if not jumped:
                parent = self.root
                skip_count = 0
            else:
                skip_count -= 1

            # navigation
            while current_node.getLength() + skip_count <= text_pointer - extention:
                skip_count += current_node.getLength()
                if current_node.getChild(self.char_index(extention + skip_count)) is None:
                    break
                parent = current_node
                current_node = current_node.getChild(self.char_index(extention + skip_count))

            # rule 2 alternate
            if current_node.getChild(self.char_index(text_pointer)) is None and current_node.getLink() is not None:
                self.addLeafNode(text_pointer, skip_count + 1, current_node)
                if added_branch:
                    previous_branched_node.setLink(current_node)
                extention += 1
                previous_branched_node = parent
                current_node = current_node.getLink()
                text_pointer += 1
                added_branch = False
                if text_pointer >= len(self.text):
                    text_pointer = len(self.text) - 1


            # determining if it is rule 2 regular or 3
            else:

                node_progress = text_pointer - skip_count - extention
                count = 0

                while self.text[current_node.getStart() + node_progress] == self.text[extention + skip_count + node_progress] and current_node.getLength() > node_progress:
                    count += 1
                    if text_pointer + node_progress > phase:
                        break
                    node_progress += 1
                    if extention + skip_count + node_progress >= phase:
                        break
                text_pointer += count


                if text_pointer > phase or current_node.getLength() == node_progress : # rule 3
                    if added_branch:
                        previous_branched_node.setLink(parent)
                    phase += 1
                    current_node = self.root
                    added_branch = False
                    jumped = False
                    previous_branched_node = self.root
                    self.incriment_global_end() # rule 1

                else: # rule 2 regular
                    if current_node.getLink() is not None: # If current is a branch
                        self.addBranchToBranch(current_node.getStart() + node_progress - 1, self.root, current_node)
                        current_node = current_node.getChild(self.char_index(current_node.getStart() + node_progress))
                        
                    else: # If current is a leaf
                        self.addBranchToLeaf(current_node.getStart() + node_progress - 1, self.root, current_node)

                    self.addLeafNode(text_pointer, current_node.getDepth() + current_node.getLength(), current_node)
                    if added_branch:
                        previous_branched_node.setLink(current_node)
                    added_branch = True
                    previous_branched_node = current_node
                    current_node = parent.getLink()
                    if current_node is self.root:
                        jumped = False
                    else:
                        jumped = True
                    extention += 1

            if extention > phase:
                phase += 1
                current_node = self.root
                jumped = False
                added_branch = False
                previous_branched_node = self.root
                if phase < len(self.text): # removes the last incriment
                    self.incriment_global_end() # rule 1
    
    def getBWT(self):
        bwt_array = self.root.getBWTArray(len(self.text), self.global_end)
        bwt = ""
        for char_index in bwt_array:
            bwt += self.text[char_index]
        return bwt

a = SuffixTree("abaaba")
print(a.getBWT())