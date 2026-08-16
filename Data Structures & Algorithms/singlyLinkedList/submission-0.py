class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:

        current = self.head

        #If Empty list
        if self.head is None:
            return -1

        position = 0
        
        #Move to index
        while position < index: 

            #Out of Bounds Check
            if current.nextNode is None:
                return -1

            #Regular Case
            current = current.nextNode
            position += 1
        

        return current.val



    def insertHead(self, val: int) -> None:   
        newHead = Node(val)        
        newHead.nextNode = self.head
        self.head = newHead

        if self.tail is None:
            self.tail = newHead

    def insertTail(self, val: int) -> None:
        newTail = Node(val)        

        if self.head is None:
            self.head = newTail
        else:
            self.tail.nextNode = newTail
        self.tail = newTail

        

    def remove(self, index: int) -> bool:

        current = self.head

        #If Empty list
        if self.head is None:
            return False

        #Remove Head
        if index == 0:
            #One Node to empty List
            self.head = self.head.nextNode
            if self.head is None:
                self.tail = None
            return True
     
        position = 0
       
        #Move to index
        while position < index-1: 

            #Out of Bounds Check
            if current.nextNode is None:
                return False

            #Regular Case
            current = current.nextNode
            position += 1

        #Out of Bounds Check
        if current.nextNode is None:
            return False

        current.nextNode = current.nextNode.nextNode
        if current.nextNode is None:
            self.tail = current
        return True
        


    def getValues(self) -> List[int]:

        array = []

        current = self.head

        while current is not None:
            array.append(current.val)
            current = current.nextNode
            
        return array


        
class Node:
    def __init__(self,val):
        self.val = val
        self.nextNode = None

    


