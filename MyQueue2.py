#Queue ver.SingleLinkedList

class MyElement:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    #Enqueue
    def enqueue(self, element):
        #Queue is None
        if self.tail == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            self.tail = element

    #Dequeue
    def dequeue(self):
        #Queue is None
        if self.head == None:
            return None
        else:
            element = self.head
            self.head = element.next
            if element.next == None:
                self.tail = None

            element.next = None

            return element

    def to_string(self):
        stringfied_data = "["
        ptr = self.head
        while ptr != None:
            stringfied_data += str(ptr.val) + " "
            ptr = ptr.next

        return stringfied_data + "]"

if __name__ == "__main__":
    #Create a Queue
    myqueue = MyQueue()

    #Entry a Queu
    myqueue.enqueue(MyElement(6))
    myqueue.enqueue(MyElement(2))
    myqueue.enqueue(MyElement(3))
    myqueue.enqueue(MyElement(7))
    myqueue.enqueue(MyElement(9))
    if myqueue.head != None and myqueue.tail != None:
        print("head = ", myqueue.head.val, "tail = ", myqueue.tail.val)
    print("InitQueu = " + myqueue.to_string())

    #Dequeue 2times
    x = myqueue.dequeue()
    y = myqueue.dequeue()
    if x != None and y != None:
        print("x = ", x, ", y = ", y)
    if myqueue.head != None and myqueue.tail != None:
        print("head = ", myqueue.head.val, ", tail = ", myqueue.tail.val)
    print("Queue = " + myqueue.to_string())

    #Enqueue a nwe data
    myqueue.enqueue(MyElement(5))
    myqueue.enqueue(MyElement(8))
    myqueue.enqueue(MyElement(1))
    if myqueue.head != None and myqueue.tail != None:
        print("head = ", myqueue.head.val, ", tail = ", myqueue.tail.val)
    print("Queue = " + myqueue.to_string())

    #All Dequeue
    while myqueue.head != myqueue.tail:
        z = myqueue.dequeue()
        if z != None:
            print("z = ", z)
        if myqueue.head != None and myqueue.tail != None:
            print("head = ", myqueue.head.val, ", tail = ", myqueue.tail.val)
        print("Queue = " + myqueue.to_string())
