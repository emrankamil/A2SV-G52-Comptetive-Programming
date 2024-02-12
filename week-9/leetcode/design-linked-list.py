class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        currentNode = self.head

        if currentNode == None or index > self.size - 1:
            return -1
        
        i = 0
        while i < index:
            currentNode = currentNode.next
            i += 1
            
        return currentNode.val     
    
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
    
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node 
             
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        
        node = Node(val)
        previousNode = self.head
        if index > self.size:
            return
        else:
            if index == 0:
                return self.addAtHead(val)
            if index == self.size:
                return self.addAtTail(val)
            
            i = 0
            while i < index-1:
                previousNode = previousNode.next
                i += 1
                
            node.next = previousNode.next
            previousNode.next = node
                
        self.size += 1
            
    def deleteAtIndex(self, index: int) -> None:
        if index > self.size - 1 or self.size == 0:
            return 
        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            if index==0:
                self.head=self.head.next
            elif index == self.size - 1:
                previousNode = self.head
                while previousNode.next.next:
                    previousNode = previousNode.next
                previousNode.next = None
                self.tail = previousNode

            else:
                previousNode=self.head
                i=0
                while i < index -1:
                    previousNode=previousNode.next
                    i+=1
                currentNode =previousNode.next
                previousNode.next=currentNode.next
        
        self.size -= 1

