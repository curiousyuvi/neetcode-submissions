class LinkedListNode:
    def __init__(self,v,p,n):
        self.v=v
        self.p=p
        self.n=n

class MyLinkedList:


    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def printList(self):
        curr=self.head
        l=[]
        while curr is not None:
            l.append(curr.v)
            curr=curr.n
        print(l)

    def get(self, index: int) -> int:

        if index<0 :
            return -1

        if self.head is None:
            return -1
        curr=self.head
        i=0
        while curr is not None and i<=index:
            if i==index:
                return curr.v
            i+=1
            curr=curr.n
        
        return -1

        

    def addAtHead(self, val: int) -> None:
        if self.length==0:
            self.head=LinkedListNode(val,None,None)
            self.tail=self.head
            self.length=1
        else:
            node=LinkedListNode(val,None,self.head)
            self.head.p=node
            self.length+=1
            self.head=node
        print("addAtHead called:")
        self.printList()

        

    def addAtTail(self, val: int) -> None:
        if self.length==0:
            self.head=LinkedListNode(val,None,None)
            self.tail=self.head
            self.length=1
        else:
            node=LinkedListNode(val,self.tail,None)
            self.tail.n=node
            self.length+=1
            self.tail=node
        print("addAtTail called:")
        self.printList()

        

    def addAtIndex(self, index: int, val: int) -> None:
        i=0
        curr=self.head
        while i<index and curr is not None:
            curr=curr.n
            i+=1
        
        if(i!=index):
            return
        else:
            if(curr is None):
                self.addAtTail(val)
            else:
                node=LinkedListNode(val,curr.p,curr)
                if curr.p is not None:
                    curr.p.n=node
                else:
                    self.head=node
                curr.p=node
                self.length+=1
        print(f"addAtIndex {index} called:")
        self.printList()
                
        

        


        

    def deleteAtIndex(self, index: int) -> None:
        i=0
        curr=self.head
        while i<index and curr is not None:
            curr=curr.n
            i+=1
        

        
        if i!=index:
            return
        else:
            if curr is None:
                return
            else:
                if curr.n is not None:
                    curr.n.p=curr.p
                else:
                    self.tail=curr.p

                if curr.p is not None:
                    curr.p.n=curr.n
                else:
                    self.head=curr.n

                self.length-=1
        print(f"deleteAtIndex {index} called:")
        self.printList()

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)