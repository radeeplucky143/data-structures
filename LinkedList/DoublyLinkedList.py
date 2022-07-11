class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0


    def __insert_head__(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            curr_node = Node(data)
            curr_node.next = self.head
            self.head.prev = curr_node
            self.head = curr_node
            del curr_node
        self.length += 1


    def __insert_tail__(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            curr_node = Node(data)
            self.tail.next = curr_node
            curr_node.prev = self.tail
            self.tail = curr_node
            del curr_node
        self.length += 1


    def insert(self, data, position='tail') -> None:
        position_type = type(position)
        if position_type == str:
            if position == 'head':
                self.__insert_head__(data)
            elif position == 'tail':
                self.__insert_tail__(data)
        elif position_type == int:
            self.__insert_position__(data, position)


    def traversal(self) -> None:
        if self.head:
            print("NULL<->", end='')
            curr_node = self.head
            while curr_node:
                print(curr_node.data, end='<->')
                curr_node = curr_node.next
            print("NULL")
            del curr_node
        else:
            print("NULL")