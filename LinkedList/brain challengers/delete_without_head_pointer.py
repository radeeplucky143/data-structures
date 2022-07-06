""" This program was used to delete the pointed node without using the head pointer.
            Auxilary space :
            Time Complexity:
            Techniques used:  3 Pointer Technique

Author: Radeep Yenni (radeeplucky143@gmail.com)
Usage: python delete_without_head_pointer.py --type [SLL, CLL, DLL, DCLL]
"""

import argparse
from LinkedList import SingleLinkedList, CircularLinkedList, DoublyCircularLinkedList, DoublyLinkedList
linkedlist_dict = dict(SLL=SingleLinkedList.LinkedList, DLL=DoublyLinkedList.LinkedList,
                       CLL=CircularLinkedList.LinkedList, DCLL=DoublyCircularLinkedList.LinkedList)


def delete_node_without_head_pointer(pointer):
    next_node = pointer.next
    pointer.data = next_node.data
    pointer.next = next_node.next


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', choices=['SingleLinkedList', 'CircularLinkedList', 'DoublyLinkedList', 'DoublyCircularLInkedList'])
    args = parser.parse_args()
    linkedlist_type = args.type

    linked_list = linkedlist_dict[linkedlist_type]()
    for value in range(100): linked_list.insert(value)
    linked_list.traverse()
    pointer = linked_list.head.next.next.next.next.next.next.next.next
    delete_node_without_head_pointer(pointer)
    linked_list.traverse()