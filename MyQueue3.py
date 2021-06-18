#MyQueue ver DoublyLinkedList

import MyList

class MyQueue:
    def __init__(self):
        self.dlist = MyList.MyDoublyLinkedList()

    #Enqueue
    def enqueue(self, element):
        self.dlist.append(element)

    #Dequeue
    def dequeue(self):
        element = self.dlist.get(0)
        self.dlist.delete(element)

    def to_string(self):
        return self.dlist.to_string()

if __name__ == "__main__":
    #Create a Queue
    myqueue = MyQueue()

    #Entry a Queu
    myqueue.enqueue(MyList.MyElement(6))
    myqueue.enqueue(MyList.MyElement(2))
    myqueue.enqueue(MyList.MyElement(3))
    myqueue.enqueue(MyList.MyElement(7))
    myqueue.enqueue(MyList.MyElement(9))
    if myqueue.dlist.head != None and myqueue.dlist.tail != None:
        print("head = ", myqueue.dlist.head.val, "tail = ", myqueue.dlist.tail.val)
    print("InitQueu = " + myqueue.to_string())

    #Dequeue 2times
    x = myqueue.dequeue()
    y = myqueue.dequeue()
    if x != None and y != None:
        print("x = ", x, ", y = ", y)
    if myqueue.dlist.head != None and myqueue.dlist.tail != None:
        print("head = ", myqueue.dlist.head.val, ", tail = ", myqueue.dlist.tail.val)
    print("Queue = " + myqueue.to_string())

    #Enqueue a nwe data
    myqueue.enqueue(MyList.MyElement(5))
    myqueue.enqueue(MyList.MyElement(8))
    myqueue.enqueue(MyList.MyElement(1))
    if myqueue.dlist.head != None and myqueue.dlist.tail != None:
        print("head = ", myqueue.dlist.head.val, ", tail = ", myqueue.dlist.tail.val)
    print("Queue = " + myqueue.to_string())

    #All Dequeue
    while myqueue.dlist.head != myqueue.dlist.tail:
        z = myqueue.dequeue()
        if z != None:
            print("z = ", z)
        if myqueue.dlist.head != None and myqueue.dlist.tail != None:
            print("head = ", myqueue.dlist.head.val, ", tail = ", myqueue.dlist.tail.val)
        print("Queue = " + myqueue.to_string())
