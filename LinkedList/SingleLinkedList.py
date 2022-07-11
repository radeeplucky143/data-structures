class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0


    def __add__(self, linkedlist):
        if self.head and linkedlist.head:
            self.tail.next = linkedlist.head
            self.tail = linkedlist.tail
            self.length += linkedlist.length
        elif linkedlist.head:
            self.head = linkedlist.head
            self.tail = linkedlist.tail
            self.length = linkedlist.length


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
            self.__insert_position__(data, position)


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


    def __delete_position__(self, position) -> None:
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
            self.__delete_position__(position)


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


    def search(self, data, count=1) -> list:
        position_found = list()
        elements_found = count
        if self.head and count >= 1:
            curr_node = self.head
            position = 1
            while curr_node:
                if curr_node.data == data:
                    count -= 1
                    position_found.append(position)
                    if count == 0:
                        return position_found
                curr_node = curr_node.next
                position += 1
            return position_found if elements_found != count else None
        return None


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


    def positional_pointer(self, position) -> Node:
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


if __name__ == '__main__':
    next_time = 'Y'
    ob = LinkedList()
    message = 'SingleLinkedList operations:\n     1.Insertion\n     2.Deletion\n     3.Update\n     4.Search\n     5.Traversal\n    6.Positional pointer\n'
    print(message)
    while next_time == 'Y':
        for _ in range(5):
            choice = int(input("Please enter your choice of operation: "))
            if choice == 1:
                data = int(input("please enter data to insert: "))
                position = input("please enter position head/tail  or position<int> : ")
                if position.isnumeric():
                    ob.insert(data, int(position))
                else:
                    ob.insert(data, position)
            elif choice == 2:
                data = int(input("please enter data to delete: "))
                position = input("please enter position head/tail  or position<int> : ")
                if position.isnumeric():
                    ob.delete(data, int(position))
                else:
                    ob.delete(data, position)
            elif choice == 3:
                data = int(input("please enter data to update: "))
                position = int(input("please enter position number : "))
                ob.update(position, data)
            elif choice == 4:
                data = int(input("please enter data to search: "))
                count = int(input("please enter number of occurences : "))
                print(f"Data Found in :{ob.search(data, count)} positions")
            elif choice == 5:
                print("Head: ", ob.head.data) if ob.head else print("Head: ", ob.head)
                print("Tail:", ob.tail.data) if ob.tail else print("Tail: ", ob.tail)
                print("Length: ", ob.length)
                ob.traverse()
            elif choice == 6:
                position = int(input("please enter position number: "))
                print(f"{position} data: {ob.positional_pointer(position).data}")
            else:
                print("please enter correct choice")
        next_time = input("Do you want to perform another operation -> 'Y/N' : ")