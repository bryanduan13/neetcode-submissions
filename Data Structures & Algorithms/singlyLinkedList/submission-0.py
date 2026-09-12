class Node:
    def __init__(self,value:int ):
        self.val = value
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = Node(None)
        self.size = 0
    
    def get(self, index: int) -> int:
        if  index >= self.size:
            return -1
        else:
            curr = self.head.next
            for t in range(index):
                curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode
        self.size+=1

    def insertTail(self, val: int) -> None:
        dhead = self.head
        curr = dhead
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.size +=1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        dhead = self.head
        curr = dhead
        i =0
        for i in range(index):
            curr = curr.next
        if curr:
            curr.next = curr.next.next
            self.size -=1
        return True

        

    def getValues(self) -> List[int]:
        array=[]
        dhead = self.head
        curr = dhead.next
        while curr:
            array.append(curr.val)
            curr = curr.next
        return array
