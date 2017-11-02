#链表

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next


Listt = Node("a",Node("b",Node("c")))

print(Listt.next.value) # b