class Node:
    def __init__(self, val):
        self.data=val
        self.next=None
class queue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue (self):
        temp=self.front
        print("deleted node:", temp.data)
        self.front=self.front.next
        if self.front==None: #if there is only one node
            print("queue is empty now:")
            self.rear=None
        temp=None
    
    def print(self):
        temp=self.front
        while temp:
            print(temp.data, end="->")
            temp = temp.next
que=queue()
que.enqueue(Node(20))
que.enqueue(Node(40))
que.enqueue(Node(60))
que.enqueue(Node(80))
que.print()
que.dequeue()
que.print()

        