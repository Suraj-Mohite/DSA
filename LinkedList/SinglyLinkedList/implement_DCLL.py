class Node:
    def __init__(self, item):
        self.next = None
        self.prev = None
        self.item = item

class DCLL:
    def __init__(self):
        self.start = None
        self.count = 0

    def is_empty(self):
        return self.start == None
    
    def display(self):
        if self.start == None:
            print("DCLL is empty")
        else:
            temp = self.start
            while temp.next != self.start:
                print(f"|{temp.item}|-->", end="")
                temp = temp.next

            print(f"|{temp.item}|-->", end="")
            print()

    def count_item(self):
        return self.count
    
    def insert_at_start(self, item):
        node = Node(item)

        if self.start == None:
            node.prev = node
            node.next = node
            self.start = node

        else:
            node.next = self.start
            node.prev = self.start.prev

            self.start.prev.next = node
            self.start.prev = node

            self.start = node

        self.count += 1

    def insert_at_end(self, item):
        node = Node(item)

        if self.start == None:
            node.prev = node
            node.next = node
            self.start = node

        else:
            node.next = self.start
            node.prev = self.start.prev

            self.start.prev.next = node
            self.start.prev = node

        self.count += 1

    def insert_after(self, item, data):
        temp = self.find_item(item)
        if temp:
            if temp == self.start.prev:
                self.insert_at_end(data)
            else:
                node = Node(data)
                node.next = temp.next
                node.prev = temp

                temp.next.prev = node
                temp.next = node
                self.count += 1

    def delete_first(self):
        if self.is_empty():
            pass
        else:
            if self.count == 1:
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next

            self.count -= 1

    def delete_last(self):
        if self.is_empty():
            pass
        else:
            if self.count == 1:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev

            self.count -= 1

    def delete_item(self, item):
        if not self.start :
            pass
        temp = self.find_item(item)
        if temp:
            if temp.next == self.start:
                self.delete_last()
            elif temp.prev.next == self.start:
                self.delete_first()
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                self.count -= 1

    def find_item(self, item):
        if self.start == None:
            return None
        else:
            temp = self.start
            while temp.next != self.start:
                if temp.item == item:
                    return temp
                temp = temp.next

            if temp.item == item:
                return temp
            return None
            
    def __iter__(self):
        return DCLLIterator(self.start)

class DCLLIterator:

    def __init__(self, start):
        self.current = start
        self.first = start
        self.flag = False

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        if self.first == self.current and self.flag:
            raise StopIteration
        else:
            self.flag = True
            
        data = self.current.item
        self.current = self.current.next
        return data


if __name__ == "__main__":
    obj=DCLL()
    obj.display()
    obj.insert_at_start(90)
    obj.insert_at_start(930)
    obj.insert_at_start(390)
    obj.insert_at_start(390)
    # obj.display()
    # print(obj.count_item())
    obj.insert_at_end(888)
    obj.insert_at_end(999)
    obj.insert_at_end(9)
    # obj.display()
    print(obj.count_item())
    # # print(obj.find_item(990))

    # obj.delete_first()
    # obj.display()
    # obj.delete_last()
    # obj.display()
    # print(obj.count_item())
    # obj.delete_item(999)
    obj.display()
    print(obj.count_item())

    for i in obj:
        print(i)