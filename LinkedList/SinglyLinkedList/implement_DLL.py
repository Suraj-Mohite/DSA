class Node:
    def __init__(self, item):
        self.prev = None
        self.next = None
        self.item = item

class DLL:
    def __init__(self):
        self.start = None
        self.count = 0

    def is_empty(self):
        return self.start == None
    
    def display(self):

        if self.is_empty():
            print("Linked list is empty")
        else:
            temp = self.start
            while temp != None:
                print(f"|{temp.item}|-->", end="")
                temp = temp.next

            print()
    
    def count_items(self):
        return self.count
    
    def insert_at_start(self, item):
        node = Node(item)

        if not self.start:
            self.start = node
        else:
            node.next = self.start
            self.start.prev = node
            self.start = node

        self.count += 1

    def insert_at_end(self, item):
        node = Node(item)
        if not self.start:
            self.start = node
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next

            node.prev = temp
            temp.next = node

        self.count += 1

    def insert_after(self, item, data):
        node = Node(data)
        temp = self.find_item(item)
        if temp:
            if temp.next:
                node.next = temp.next
                node.prev = temp
                temp.next.prev = node  #node.next.prev = node
                temp.next = node

            else:
                node.prev = temp
                temp.next = node

            self.count += 1
            return node
        return None

    def delete_at_start(self):

        if not self.start:
            pass
        else:
            if not self.start.next:
                self.start = None
            else:
                self.start.next.prev = None
                self.start = self.start.next

            self.count -= 1

    def delete_at_end(self):

        if not self.start:
            pass
        else:
            temp = self.start
            if not temp.next:
                self.start = None
            else:
                while temp.next:
                    temp = temp.next

                temp.prev.next = None

            self.count -= 1

    def delete_item(self, item):
        temp = self.find_item(item)
        if temp:
            if not temp.prev:
                self.delete_at_start()
            elif not temp.next:
                self.delete_at_end()
            else:
                temp.next.prev = temp.prev
                temp.prev.next = temp.next

                self.count -= 1

    def find_item(self, item):

        if not self.start:
            return None
        else:
            temp = self.start
            while temp != None:
                if temp.item == item:
                    return temp
                temp = temp.next

            return None
        
    def __iter__(self):
        return DLLIterator(self.start)
        
class DLLIterator:
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

if __name__ == "__main__":
    obj = DLL()
    # obj.display()
    # obj.insert_at_start(89)
    # obj.insert_at_start(990)
    # obj.insert_at_start(3489)
    # obj.display()
    # print(obj.count_items())

    # obj.insert_at_end(666)
    # obj.insert_at_end(444)
    # obj.insert_at_end(888)
    # obj.display()
    # print(obj.count_items())

    # obj.display()
    # print(obj.count_items())

    # obj.delete_at_start()
    # obj.display()
    # print(obj.count_items())

    # obj.delete_at_end()

    obj.delete_item(89)
    obj.display()
    print(obj.count_items())


    for i in obj:
        print(i)