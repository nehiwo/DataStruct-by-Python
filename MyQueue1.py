#MyOueue verArray

class MyQueue:
    def __init__(self, size):
        self.size = size
        self.arr = [-1] * size
        self.head = 0
        self.tail = 0

    #Enqueue
    def enqueue(self, val):
        #Queue is Full
        if (self.tail + 1) % self.size == self.head:
            return None

        #Save an Element
        self.arr[self.tail] = val

        #Shift a Pointer
        self.tail = (self.tail + 1) % self.size

    #Dequeue
    def dequeue(self):
        #Queue is Null
        if self.head == self.tail:
            return None

        #Get an Element
        e = self.arr[self.head]
        self.arr[self.head] = -1

        #Shift a Pointer
        self.head = (self.head + 1) % self.size

        return e

    def to_string(self):
        stringfied_data = "["
        index = self.head
        while index != self.tail:
            stringfied_data += str(self.arr[index]) + " "
            if index == self.size - 1:
                index = 0
            else:
                index += 1

        return stringfied_data + "]"

if __name__ == "__main__":
    #QueueSize is 6
    myqueue = MyQueue(6)

    #Enququ & Print
    myqueue.enqueue(6)
    myqueue.enqueue(2)
    myqueue.enqueue(3)
    myqueue.enqueue(7)
    myqueue.enqueue(9)
    print("head = " + str(myqueue.head) + ", tail = " + str(myqueue.tail))
    print("InitQueue = " + myqueue.to_string())

    #Dequeue 2times
    x = myqueue.dequeue()
    y = myqueue.dequeue()
    print("x = " + str(x) + ", y = " + str(y))
    print("head = " + str(myqueue.head) + ", tail = " + str(myqueue.tail))
    print("Queue = " + myqueue.to_string())

    #Enqueue a nwe data
    myqueue.enqueue(5)
    myqueue.enqueue(8)
    #sizeover! Not Enqueue 1!
    myqueue.enqueue(1)
    print("head = " + str(myqueue.head) + ", tail = " + str(myqueue.tail))
    print("Queue = " + myqueue.to_string())

    #All Dequeue
    while myqueue.head != myqueue.tail:
        z = myqueue.dequeue()
        if z != None:
            print("z = " + str(z))
        print("head = " + str(myqueue.head) + ", tail = " + str(myqueue.tail))
        print("Queue = " + myqueue.to_string())
