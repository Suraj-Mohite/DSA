
#implement Singly Linked List in Python

class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
    
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SinglyLinkedList:

    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start == None
    
    def display(self):
        if not self.is_empty():
            next = self.start
            while next:
                print(f"|{next.item}|-->", end="")
                next = next.next
            print()
       
    
    def insert_at_start(self, data):
        node = Node(data, self.start)
        self.start = node
        self.count +=  1

    def insert_at_end(self, data):
        node = Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next:
                temp = temp.next
            temp.next = node
        else:
            self.start = node

        self.count +=  1

    def search(self, data):
        temp = self.start
        while temp:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, item, data):
        item_node = self.search(item)
        if item_node:
            node = Node(data, item_node.next)
            item_node.next = node
            self.count +=  1
            return node
        else:
            return None
        
    def delete_first(self):
        if not self.is_empty():
            self.start = self.start.next
            self.count -=  1

    def delete_last(self):
        if self.start == None:
            pass
        elif self.start.next == None:
            self.start = None
            self.count -=  1
        else:
            temp = self.start
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
            self.count -=  1

    def delete_item(self, item):
        if self.start == None:
            pass
        elif self.start.next == None:
            if self.start.item == item:
                self.start = None
                self.count -=  1
        else:
            temp = self.start
            if temp.item == item:
                self.start =  temp.next
                self.count -=  1
            else:

                while temp.next != None:
                    if temp.next.item == item:
                        temp.next = temp.next.next
                        self.count -=  1
                        break
                    temp = temp.next
        
                # while temp.next.next != None:
                #     if temp.next.item == item:
                #         temp.next = temp.next.next
                #         break
                #     temp = temp.next
                
                # if temp.next.item == item:
                #     temp.next = temp.next.next

    def count_item(self):
        return self.count
                    
    def __iter__(self):
        return SLLIterator(self.start)


obj = SinglyLinkedList()
obj.insert_at_start(67)
obj.insert_at_start(94)
obj.insert_at_start(84)
obj.insert_at_end(200)
obj.insert_at_start(54)
obj.insert_at_end(625)
obj.display()

# print(obj.insert_after(200, 90))
obj.display()
obj.delete_first()
obj.display()
obj.delete_last()
obj.delete_item(54)
obj.display()

for i in obj:
    print(i, end=" ")

print()
print(obj.count_item())