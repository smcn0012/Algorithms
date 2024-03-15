class Fibonacci_Node:
    marked: bool
    value: int
    degree: int
    child: Fibonacci_Node
    right: Fibonacci_Node
    left: Fibonacci_Node
    parrent: Fibonacci_Node

    def __init__(self, value: int) -> None:
        self.value = value
        self.marked = False
        self.degree = 0

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

    def setValue(self, new_value: int) -> None:
        self.value = new_value

    def setDegree(self, new_degree) -> int:
        self.degree = new_degree

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
    
    def getDegree(self) -> int:
        return self.degree

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
        if new_number < self.h_min.getValue():
            self.h_min = new_node

    def delete(self, target_key:int) -> None:
        target_node = self.findNode(target_key)
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
        heap_degrees = []
        current_node = self.h_min
        last_node_checked = None
        skip_to_node = None
        while current_node is not last_node_checked:
            if self.h_min.getDegree() >= len(heap_degrees):
                heap_degrees.extend([None for _ in range(self.h_min.getDegree() - len(heap_degrees) + 1)])
            
            current_degree_node = heap_degrees[self.h_min.getDegree()]
            if current_degree_node is None:
                heap_degrees[self.h_min.getDegree()] = current_node
                last_node_checked = current_node
                if skip_to_node is not None:
                    current_node = skip_to_node
                    skip_to_node = None
                else:
                    current_node = current_node.getRight()
            elif current_degree_node.getValue() < current_node.getValue():
                skip_to_node = current_node.getRight()
                # Setting the left and right of the current node to point at eachother
                current_node.getLeft().setRight(current_node.getLeft())
                current_node.getRight().setLeft(current_node.getRight())
                # Inserting the current node to the left of the child of the current degree node
                current_degree_node.getChild().getLeft().setRight(current_node)
                current_node.setLeft(current_degree_node.getChild().getLeft())
                current_degree_node.getChild().setLeft(current_node)
                current_node.setRight(current_degree_node.getChild())
                current_degree_node.setDegree(current_degree_node.getDegree() + 1)
                current_node = current_degree_node
                
            
                

    def decreaseKey(self, target_key: int, new_value: int) -> None:
        target_node = self.findNode(target_key)
        #case 1: decreasing the node doesn't violate the heap property

    def findNode(self, target_node: int) -> Fibonacci_Node:
