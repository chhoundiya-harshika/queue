class Node:
    def __init__(self, value):
        self.data= value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node
        
    def pop (self):
        if self.isempty():
            print("stack is empty:")
        else:
            temp=self.top
            s2=print("Poped Element:",temp.data)
            self.top=self.top.next
            temp=None
        return s2
        
    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("stack contains..")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
class queue:
    def __init__(self):
        self.front=self.rear=None
        
    def isempty(self):
        return self.front is None
    
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue (self):
        temp=self.front
        # print("deleted node:", temp.data)
        dqued_data = temp.data
        self.front=self.front.next
        if self.front==None: #if there is only one node
            print("queue is empty now:")
            self.rear=None
        temp=None
        return dqued_data
    
    def print(self):
        temp=self.front
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print()
def reverse_stack(s1):
    q1=queue()
    while not s1.isempty():
        q1.enqueue(Node(s1.pop()))
    #q1.print()
    while not q1.isempty():
        s1.push(Node(q1.dequeue()))
    s1.print()
        


st=stack()
st1=stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))
st.print()
st1.print()
reverse_stack(st)