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
        else:
            head_node = self.head
            self.head = Node(data)
            self.head.next = head_node
            del head_node
        self.length += 1


    def __insert_tail__(self, data) -> None:
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.length += 1


    def __insert_position__(self, data, position) -> None:
        if position <= self.length+1:
            if position == 1:
                self.__insert_head__(data)
            elif position == self.length+1:
                self.__insert_tail__(data)
            else:
                prev_node = None
                curr_node = self.head
                while position > 1:
                    prev_node = curr_node
                    curr_node = curr_node.next
                    position -= 1
                node = Node(data)
                prev_node.next = node
                node.next = curr_node
                del prev_node, curr_node
                self.length += 1


    def insert(self, data, position='tail') -> None:
        position_type = type(position)
        if position_type == str:
            if position == 'head':
                self.__insert_head__(data)
            elif position == 'tail':
                self.__insert_tail__(data)
        elif position_type == int:
            self.__insert_position__(data,position)


    def __delete_head__(self) -> None:
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            self.length -= 1


    def __delete_tail__(self) -> None:
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                curr_node = self.head
                prev_node = None
                while curr_node != self.tail:
                    prev_node = curr_node
                    curr_node = curr_node.next
                self.tail = prev_node
                self.tail.next = None
            self.length -= 1


    def __delete_position(self, position) -> None:
        if position <= self.length:
            if position == 1:
                self.__delete_head__()
            elif position == self.length:
                self.__delete_tail__()
            else:
                prev_node = None
                curr_node = self.head
                next_node = curr_node.next
                while position > 1:
                    prev_node = curr_node
                    curr_node = next_node
                    next_node = next_node.next
                    position -= 1
                prev_node.next = next_node
                self.length -= 1


    def delete(self, position) -> None:
        position_type = type(position)
        if position_type == str:
            if position == 'head':
                self.__delete_head__()
            else:
                self.__delete_tail__()
        elif position_type == int:
            self.__delete_position(position)


    def update(self, position, data) -> None:
        if position <= self.length:
            if position == 1:
                self.head.data = data
            elif position == self.length:
                self.tail.data = data
            else:
                curr_node = self.head
                while position > 1:
                    curr_node = curr_node.next
                    position -= 1
                curr_node.data = data


    def traverse(self) -> None:
        if self.head:
            curr_node = self.head
            while curr_node != self.tail.next:
                print(curr_node.data, end='->')
                curr_node = curr_node.next
            print("NULL")
            del curr_node
        else:
            print("NULL")


    def positionitional_pointer(self, position) -> Node:
        if type(position) == int and position <= self.length:
            if position == 1:
                return self.head
            elif position == self.length:
                return self.tail
            curr_node = self.head
            curr_position = 1
            while curr_position < position:
                curr_node = curr_node.next
                curr_position += 1
            return curr_node
        return None