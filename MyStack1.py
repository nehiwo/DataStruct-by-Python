#stack ver Array

class MyStack:
    def __init__(self, size):
        self.size = size
        self.arr = [-1] * size
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, val):
        if self.top == self.size - 1:
            return None
        else:
            self.top += 1
            self.arr[self.top] = val

    def pop(self):
        if self.is_empty():
            return None
        else:
            e = self.arr[self.top]
            self.arr[self.top] = -1
            self.top -= 1

        return e

    def to_string(self):
        stringfied_data = "["
        for i in range(0, self.top + 1):
            stringfied_data += str(self.arr[i]) + " "

        return stringfied_data + "]"

if __name__ == "__main__":
    mystack = MyStack(6)

    mystack.push(6)
    mystack.push(2)
    mystack.push(3)
    mystack.push(7)
    mystack.push(9)
    print("top = ", mystack.top)
    print("InitStack = " + mystack.to_string())

    x = mystack.pop()
    y = mystack.pop()
    if x != None and y != None:
        print("pop1 = ", x, ", pop2 = ", y)
    print("top = ", mystack.top)
    print("Stack = " + mystack.to_string())

    mystack.push(5)
    mystack.push(8)
    mystack.push(1)
    mystack.push(4)
    mystack.push(10)
    print("top = ", mystack.top)
    print("Stack = " + mystack.to_string())
