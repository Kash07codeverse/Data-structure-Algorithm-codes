class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def create():
        n=int(input("Enter data to create the node (o to stop):"))
        if n==0:
            return None 
        root = Node(n)
        print (f"enter left of {n}:")
        root.left=create()
        print(f"enter right of {n}:")
        root.right=create()
        return root 

class Stack:
    def __init__(self):
        self.top=-1
        self.ST=[0]*7

    def push(self,x):
        if self.top==6:
            print("Stack is overflow..")
            return
        self.top=self.top+1
        self.ST[self.top]=x

    def pop(self):
        if self.top==-1:
            print("Nothing to print..")
            return
        else:
            y=self.ST[self.top]
            self.top=self.top-1
        return y

def preorder(root):
    s=Stack() #oject creation 
    while root is not None:
        print(root.data)
        s.push(root)
        root=root.left
    while s.top!=-1:
        root =s.pop()
        root=root.right
        while root is not None:
                print(root.data)
                s.push(root)
                root=root.left
def inorder(root):
    s=Stack()
    while root is not None:
        s.push(root)
        root=root.left
    while s.top!=-1:
        root=s.pop()
        print(root.data)
        root = root.right
        while root is not None:
            s.push(root)
            root=root.left
def postorder(root):
    s1=Stack()
    s2=Stack()
    s1.push(root)
    while s1.top!=-1:
        current=s1.pop()
        s2.push(current)
        if current.left!=None:
            s1.push(current.left)
        if current.right!=None:
            s1.push(current.right)
    while s2.top!=-1:
        current2=s2.pop()
        print(current2.data)

      
root=create()
print(preorder)
preorder(root)

print(inorder)
inorder(root)

print (postorder)
postorder(root)