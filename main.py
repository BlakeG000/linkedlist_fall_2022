from random import shuffle
from time import thread_time
class LinkedList:
    # The __Node class is used internally by the LinkedList class. It is
    # invisible from outside this class due to the two underscores
    # that precede the class name. Python mangles names so that they
    # are not recognizable outside the class when two underscores
    # precede a name but aren't followed by two underscores at the
    # end of the name (i.e. an operator name).
    class __Node:
        def __init__(self, item, next=None):
            self.item = item
            self.next = next

        def getItem(self):
            return self.item

        def getNext(self):
            return self.next

        def setItem(self, item):
            self.item = item

        def setNext(self, next):
            self.next = next

    def __init__(self, contents=[]):
        # Here we keep a reference to the first node in the linked list
        # and the last item in the linked list. The both point to a
        # dummy node to begin with. This dummy node will always be in
        # the first position in the list and will never contain an item.
        # Its purpose is to eliminate special cases in the code below.
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if 0 <= index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            return cursor.getItem()

        raise IndexError("LinkedList index out of range")

    def __setitem__(self, index, val):
        if 0 <= index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            cursor.setItem(val)
            return

        raise IndexError("LinkedList assignment index out of range")

    def insert(self, index, item):
        # This is left as an exercise for the reader.
      if index == 0:
        self.numItems += 1
        cursor = self.first
        newitem = self.__Node(item,cursor.getNext())
        cursor.setNext(newitem)
        return
      if 0 <= index:
        
        cursor = self.first.getNext()
        for i in range(1, index):
          cursor = cursor.getNext()
          if cursor == None:
            cursor = self.first.getNext()
        newitem = self.__Node(item,cursor.getNext())
        cursor.setNext(newitem)
        self.numItems += 1
        return
        

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                            str(type(self)) + " + " + str(type(other)))

        result = LinkedList()

        cursor_self = self.first.getNext()

        while cursor_self is not None:
          result.append(cursor_self.getItem())
          cursor_self = cursor_self.getNext()
        cursor_other = other.first.getNext()

        while cursor_other is not None:
          result.append(cursor_other.getItem())
          cursor_other = cursor_other.getNext()
      

        #TODO: Finish this.

        return result

    def __contains__(self, item):
        # This is left as an exercise for the reader.
      cursor_self = self.first.getNext()
      while cursor_self is not None:
        if cursor_self.getItem() == item:
          return True
        cursor_self = cursor_self.getNext()

      return False

        

    def __delitem__(self, index):
        # This is left as an exercise for the reader.
      
      if 0 < index < self.numItems:
        cursor = self.first.getNext()
      
        for i in range(index-1):
          cursor = cursor.getNext()
        toDelete = cursor.getNext()
        cursor.setNext(cursor.getNext().getNext())
        toDelete.setNext(None)
        self.numItems -= 1
        return
      elif index == 0: 
        toDelete = self.first.getNext()
        self.first.setNext(toDelete.getNext())
        toDelete.setNext(None)
        self.numItems -= 1
        raise IndexError("LinkedLisk index out of range")

      
    def swap(self,i,j):
      temp = self[j]
      self[j] = self[i]
      self[i] = temp
      
    def isSorted(self):
      cursor = self.first.getNext()
      while cursor.getNext() is not None:
        if cursor.getItem() > cursor.getNext().getItem():
          return False
        cursor = cursor.getNext()
      return True
      
    def bubbleSort(self):
      while not self.isSorted():
        for i in range(self.numItems - 1):
          if self[i]>self[i+1]:
            self.swap(i,i+1)
      
    def __eq__(self, other):
        # This is left as an exercise for the reader.
      if type(self) != type(other):
        return False
      if self.numItems != other.numItems:
        return False
      cursor_self = self.first.getNext()
      cursor_other = other.first.getNext()

      while cursor_self is not None:
        if cursor_self.getItem() != cursor_other.getItem():
          return False

        cursor_self = cursor_self.getNext()
        cursor_other = cursor_other.getNext()

      return True

    def __len__(self):
        # This is left as an exercise for the reader.
      return self.numItems

    def append(self, item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1

    def __str__(self):
        # This is left as an exercise for the reader.
      curser = self.first.getNext()
      outString = "["
      
      
      while curser is not None:
        outString += str(curser.getItem())
        outString += ","

        curser = curser.getNext()
      outString = outString.rstrip(",")
      outString += "]"
      return outString
    
    

def main():
    lst = LinkedList()

    for i in range(100):
        lst.append(i)

    lst2 = LinkedList(lst)

    print(lst)
    print(lst2)

    if lst == lst2:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")

    lst3 = lst + lst2

    if len(lst3) == len(lst) + len(lst2):
      print("Test 2 Passed")
    else:
        print("Test 2 Failed")

    if 1 in lst3:
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")

    if 2 in lst3:
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")

    del lst[1]

    if 1 in lst:
        print("Test 5 Failed")
    else:
        print("Test 5 Passed")

    if len(lst) == 99:
        print("Test 6 Passed")
    else:
        print("Test 6 Failed")

    if lst == lst2:
        print("Test 7 Failed")
    else:
        print("Test 7 Passed")

    del lst2[2]

    if lst == lst2:
        print("Test 8 Failed")
    else:
        print("Test 8 Passed")

    lst4 = LinkedList(lst)
    lst.insert(0, 100)
    lst4 = LinkedList([100]) + lst4

    print(lst)
    print(lst4)

    if lst == lst4:
      print("Test 9 Passed")
    else:
        print("Test 9 Failed")

    lst.insert(1000, 333)
    lst4.append(333)

    if lst == lst4:
      print("Test 10 Passed")
    else:
      print("Test 10 Failed")
      
    print(lst)
    print(lst4)

    lst5 = LinkedList([5,4,3,2,1])
    print(lst5.isSorted())
    lst5.bubbleSort()
    print(lst5)
if __name__ == "__main__":
    main()