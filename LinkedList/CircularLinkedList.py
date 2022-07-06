class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0


    def __insert_head__(self, data) -> None:
        if self.head is None:
            self.head = self.tail = Node(data)
            self.tail.next = self.head
        else:
            head_node = self.head
            self.head = Node(data)
            self.head.next = head_node
            self.tail.next = self.head
            del head_node
        self.length += 1


    def __insert_tail__(self, data) -> None:
        if self.head is None:
            self.head = self.tail = Node(data)
            self.tail.next = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            self.tail.next = self.head
        self.length += 1


    def __insert_pos__(self, data, pos) -> None:
        if pos <=  self.length+1:
            if pos == 1:
                self.__insert_head__(data)
            elif pos == self.length+1:
                self.__insert_tail__(data)
            else:
                prev_node = None
                curr_node = self.head
                while pos > 1:
                    prev_node = curr_node
                    curr_node = curr_node.next
                    pos -= 1
                node = Node(data)
                prev_node.next = node
                node.next = curr_node
                del prev_node, curr_node
                self.length += 1


    def insert(self, data, pos='tail') -> None:
        pos_type = type(pos)
        if pos_type == str:
            if pos == 'head':
                self.__insert_head__(data)
            elif pos == 'tail':
                self.__insert_tail__(data)
        elif pos_type == int:
            self.__insert_pos__(data,pos)



    def traverse(self) -> None:
        if self.head:
            curr_node = self.head
            print(curr_node.data, end='->')
            curr_node = curr_node.next
            while curr_node != self.head:
                print(curr_node.data, end='->')
                curr_node = curr_node.next
            print("HEAD")
            del curr_node
        else:
            print("NULL")


    def detect_loop(self):
        fast_pointer = self.head
        slow_pointer = self.head
        while fast_pointer and slow_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if fast_pointer == slow_pointer:
                return True
        return False