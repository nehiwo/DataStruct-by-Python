#hash search

import time

class MyNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    def to_string(self):
        return "(" + str(self.key) + "," + str(self.val) + ")"

class MyHashTable:
    def __init__(self, size):
        self.tbl = [None] * size

    def __get_hash(self, key):
        return key % len(self.tbl)

    def insert(self, key, val):
        hash_val = self.__get_hash(key)

        n = MyNode(key, val)

        if self.tbl[hash_val] == None:
            self.tbl[hash_val] = n
        else:
            ptr = self.tbl[hash_val]
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = n

    def delete(self, key):
        hash_val = self.__get_hash(key)

        prev_ptr = None
        ptr = self.tbl[hash_val]
        while ptr != None:
            if ptr.key == key:
                if ptr.next != None:
                    if prev_ptr != None:
                        prev_ptr.next = ptr.next
                    else:
                        self.tbl[hash_val] = ptr.next
                else:
                    if prev_ptr != None:
                        prev_ptr.next = None
                    else:
                        self.tbl[hash_val] = None
                return None
            prev_ptr = ptr
            ptr = ptr.next

    def search(self, key):
        hash_val = self.__get_hash(key)

        if self.tbl[hash_val] != None:
            ptr = self.tbl[hash_val]
            if ptr.key == key:
                return ptr
            while ptr.next != None:
                ptr = ptr.next
                if ptr.key == key:
                    return ptr
        else:
            return None
    def to_string(self):
        stringfied_tbl = ""
        for i in range(0, len(self.tbl)):
            if self.tbl[i] != None:
                stringfied_tbl += "tbl[" + str(i) + "] -> " + self.tbl[i].to_string()
                ptr = self.tbl[i]
                while ptr.next != None:
                    ptr = ptr.next
                    stringfied_tbl += " -> " + ptr.to_string()
                stringfied_tbl += "\n"
        return stringfied_tbl

if __name__ == "__main__":
    my_hash = MyHashTable(10)

    my_hash.insert(3, "Alice")
    my_hash.insert(12, "Bob")
    my_hash.insert(233, "Chris")
    my_hash.insert(95, "David")
    my_hash.insert(183, "Eve")
    my_hash.insert(25, "George")
    print("Hash : ")
    print(my_hash.to_string())

    start = time.time()
    x = my_hash.search(233)
    end = time.time()
    if x != None:
        print("get this data : " + x.to_string())
    else:
        print("cannot get a data by this key.")
    print("search time : " + str(end - start) + "\n")

    start = time.time()
    x = my_hash.search(12)
    end = time.time()
    if x != None:
        print("get this data : " + x.to_string())
    else:
        print("cannot get a data by this key.")
    print("search time : " + str(end - start) + "\n")

    start = time.time()
    x = my_hash.search(512)
    end = time.time()
    if x != None:
        print("get this data : " + x.to_string())
    else:
        print("cannot get a data by this key.")
    print("search time : " + str(end - start) + "\n")

    my_hash.delete(233)
    print("Hash : ")
    print(my_hash.to_string())
