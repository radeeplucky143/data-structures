class Stack:

    def __init__(self) -> None:
        self.stackbox = list()
        self.stackbox_size = 0


    def push(self, data) -> None:
        self.stackbox.append(data)
        self.stackbox_size += 1


    def pop(self) -> None:
        if self.stackbox_size >= 1:
            del self.stackbox[-1]


    def traverse(self) -> None:
        print(self.stackbox)


    def isempty(self) -> bool:
        if self.stackbox_size == 0:
            return True
        return False


    def size(self) -> int:
        return self.stackbox_size


    def peek(self) -> int:
        if self.stackbox_size >= 1:
            return self.stackbox[-1]


ob = Stack()
ob.push(8)
ob.push(78)
ob.push(5)
ob.traverse()
print(ob.peek())
ob.pop()
ob.traverse()
print(ob.peek())
