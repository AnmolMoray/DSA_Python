class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __str__(self):
        temp_node=self.head
        result=" "
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+='->'
            temp_node=temp_node.next
        return result

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length=self.length+1
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length += 1
    def traverse(self):
        current=self.head
        while current is not None:
            print(current.value)
            current=current.next
    def insert(self,index,value):
        new_node=Node(value)
        if self.head is None:
            self.head=self.tail=new_node
        elif index==0:
            new_node.next=self.head
            self.head=new_node
        else:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node

    def search(self,target):
        current=self.head
        while current is not None:
            if current.value==target:
                return True
            current=current.next
        return False
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node



    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return popped_node


    def remove(self, index):
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == -1 or index == self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

l1=LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.prepend("00")
print(l1)
print(type(l1))
l1.traverse()
l1.insert(0,90)
print(l1)
l2=LinkedList()
l2.insert(2,1)
print(l2)
nas=l1.search(10)
print(nas)
