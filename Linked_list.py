class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    def insertafter(self,prev_node,new_data):
        if prev_node is Node:
            print("node cannot be Null")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head  is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value, " -> ",end=" ")
            temp  = temp.next
        print(" ")
    def clear(self):
        tmp = self.head
        while tmp:
            next_tmp = tmp.next
            del tmp.value
            tmp = next_tmp

if __name__ == "__main__":
    llist = DoublyLinkedList()
    llist.append(1)
    llist.push(2)
    llist.push(3)
    llist.append(4)
    llist.insertafter(llist.head.next, 5)
    llist.printList()
    llist.clear()




