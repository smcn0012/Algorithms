class Fibonacci_Node:
    marked: bool
    value: int
    child: Fibonacci_Node
    right: Fibonacci_Node
    left: Fibonacci_Node
    parrent: Fibonacci_Node

    def __init__(self, value: int) -> None:
        self.value = value
        self.marked = False

    def setChild(self, child: Fibonacci_Node) -> None:
        self.child = child
    
    def setParrent(self, parrent: Fibonacci_Node) -> None:
        self.parrent = parrent

    def setRight(self, sibling: Fibonacci_Node) -> None:
        self.right = sibling
    
    def setLeft(self, sibling: Fibonacci_Node) -> None:
        self.left = sibling
    
    def setMarked(self, marked: bool) -> None:
        self.marked = marked

    def getValue(self) -> int:
        return self.value

    def getChild(self) -> Fibonacci_Node:
        return self.child
    
    def getParrent(self) -> Fibonacci_Node:
        return self.parrent
    
    def getRight(self) -> Fibonacci_Node:
        return self.right
    
    def getLeft(self) -> Fibonacci_Node:
        return self.left
    
    def getMarked(self) -> bool:
        return self.marked

class Fibonacci_Heap:
        
    h_min: Fibonacci_Node
        
    def __init__(self, first_number: int) -> None:
        self.h_min = Fibonacci_Node(first_number)
        self.h_min.setLeft(self.h_min)
        self.h_min.setRight(self.h_min)


    def getHMin(self) -> Fibonacci_Node:
        return self.h_min
    
    def insert(self, new_number: int) -> None:
        new_node = Fibonacci_Node(new_number)
        self.h_min.getLeft().setRight(new_node)
        self.h_min.setLeft(new_node)

    def delete(self, target_num:int) -> None:
        #TODO: Search for target node
        target_node.getChild().getRight().setLeft(target_node.getLeft())
        target_node.getChild().setRight(target_node.getRight())

    def join(self, new_heap: Fibonacci_Heap) -> None:
        new_heap.getHMin().getLeft().setRight(self.h_min)
        temp = self.h_min.getLeft()
        self.h_min.setLeft(new_heap.getHMin().getLeft())
        new_heap.getHMin().setLeft(self.h_min.getLeft())
        temp.setRight(new_heap.getHMin())
        if self.getHMin().getValue() > new_heap.getHMin().getValue():
            self.h_min = new_heap.getHMin()

    def extract_min(self) -> int:
        old_min = self.getHMin()
        self.h_min = self.h_min.getChild()
        self.consolidate()
        return old_min

    def consolidate(self) -> None:
        pass