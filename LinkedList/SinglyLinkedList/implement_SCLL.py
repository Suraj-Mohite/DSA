class Node:
    def __init__(self, item):
        self.next = None
        self.item = item

#Singly Circular Linked List
class SCLL:
    def __init__(self):
        self.end = None
        self.count = 0

    def is_empty(self):
        return self.end == None
    
    def count_items(self):
        return self.count
    
    def display(self):
        if self.end == None:
            print("SCLL Is Empty")
        else:
            temp = self.end.next

            while temp.next != self.end.next:
                print(f"|{temp.item}|-->", end="")
                temp = temp.next
            
            print(f"|{temp.item}|-->", end="")
            print()

    def insert_at_start(self, item):
        node = Node(item)
        if self.end == None:
            node.next = node
            self.end = node
        else:
            node.next = self.end.next
            self.end.next = node
        self.count += 1

    def insert_at_end(self, item):
        node = Node(item)

        if self.end == None:
            node.next = node
            self.end = node
        else:
            node.next = self.end.next
            self.end.next = node
            self.end = node
        
        self.count += 1

    def insert_after(self, item, data):
        node = Node(data)

        temp = self.find_item(item)
        if temp:
            if temp.next == self.end.next:
                self.insert_at_end(data)
            else:
                node.next = temp.next
                temp.next = node
                self.count += 1

    def delete_first(self):
        if self.end == None:
            pass
        else:
            if self.count == 1:
                self.end = None
            else:
                self.end.next = self.end.next.next
            self.count -= 1

    def delete_last(self):
        if self.end == None:
            pass
        else:
            if self.count == 1:
                self.end = None
            else:
                temp = self.end.next
                while temp.next != self.end:
                    temp = temp.next
                temp.next = temp.next.next
                self.end = temp

            self.count -= 1

    def delete_item(self, item):
        if self.end == None:
            pass
        else:
            temp = self.find_item(item)
            if temp:
                if temp.next == self.end.next:
                    self.delete_last()
                else:
                    temp_node = self.end.next
                    while temp_node.next != temp:
                        temp_node = temp_node.next
                    
                    temp_node.next = temp.next
                    self.count -= 1    

    def find_item(self, item):

        if self.end == None:
            return None
        else:
            temp = self.end.next
            while temp.next != self.end.next:
                if temp.item == item:
                    return temp
                temp = temp.next

            if temp.item == item:
                return temp
            return None

    def __iter__(self):
        if not self.end:
            return SCLLIterator(None) 
        return SCLLIterator(self.end.next)

class SCLLIterator:

    def __init__(self, start):
        self.current = start
        self.start = start
        self.flag = False

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        
        if self.current == self.start and self.flag:
            raise StopIteration
        else:
            self.flag = True
        data = self.current.item
        self.current = self.current.next
        return data

if __name__ == "__main__":
    obj = SCLL()
    # obj.display()
    obj.insert_at_start(78)
    # obj.display()
    obj.insert_at_start(8)
    obj.insert_at_start(448)
    obj.insert_at_start(783)
    obj.insert_at_start(782)
    # obj.display()
    # print(obj.count_items())
    obj.insert_at_end(444)
    obj.insert_at_end(333)
    # obj.display()
    # print(obj.count_items())
    # print(obj.find_item(448))

    # obj.insert_after(782, 777)
    # obj.display()
    # print(obj.count_items())
    # obj.delete_first()
    # obj.display()
    # print(obj.count_items())
    # obj.delete_last()
    # obj.delete_item(8)
    obj.display()
    # print(obj.count_items())

    for i in obj:
        print(i)