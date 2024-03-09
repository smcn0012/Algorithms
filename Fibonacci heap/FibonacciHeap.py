class Fibonacci_Heap:
    h_min = None

    class Fibonacci_Node:
        marked = False
        value = -1
        child = None
        right = None
        left = None
        parrent = None

        def __init__(self, value: int) -> None:
            self.value = value

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
        
    def __init__(self) -> None:
        pass

    def getHMin(self) -> Fibonacci_Node:
        return self.h_min