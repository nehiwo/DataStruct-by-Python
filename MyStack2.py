#Stack ver SingleLinkedList

class MyElement:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self, element):
        if self.top != None:
            element.next = self.top
        self.top = element

    def pop(self):
        if self.is_empty():
            return None
        else:
            element = self.top
            self.top = element.next

            element.next = None

            return element

    def to_string(self):
        stringfied_data = "["
        ptr = self.top
        while ptr != None:
            stringfied_data += str(ptr.val) + " "
            ptr = ptr.next

        return stringfied_data + "]"

if __name__ == "__main__":
    mystack = MyStack()

    mystack.push(MyElement(6))
    mystack.push(MyElement(2))
    mystack.push(MyElement(3))
    mystack.push(MyElement(7))
    mystack.push(MyElement(9))
    if mystack.top != None:
        print("top = " + str(mystack.top.val))
    print("InitStack = " + mystack.to_string())

    x = mystack.pop()
    y = mystack.pop()
    if x != None and y != None:
        print("pop1 = " + str(x.val) + ", pop2 = " + str(y.val))
    if mystack.top != None:
        print("top = " + str(mystack.top.val))
    print("Stack = " + mystack.to_string())

    mystack.push(MyElement(5))
    mystack.push(MyElement(8))
    mystack.push(MyElement(1))
    mystack.push(MyElement(4))
    if mystack.top != None:
        print("top = " + str(mystack.top.val))
    print("Stack = " + mystack.to_string())

    while mystack.top != None:
        z = mystack.pop()
        if z != None:
            print("pop = " + str(z.val))
        print("Stack = " + mystack.to_string())
