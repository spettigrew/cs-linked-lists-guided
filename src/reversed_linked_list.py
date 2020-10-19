"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None
def reverse(head_of_list):
    # Reverse all the pointers:
    # Loop (while) go while… we still have nodes to process
    # We have a current_node
    # Initialize current_node
    current_node = head_of_list
    # We need a reference to prev
    # When we start, prev is none
    prev = None
    # On each iteration of the loop:
    while current_node is not None:
        print("Current node:", current_node.value)
    # We need a reference to next_node:
    # Next_node = current_node.next
        next_node = current_node.next
    # Set current_node.next to prev
        current_node.next = prev
    # Set prev to cur_node
        prev = current_node
    # Update current_node to point to next_node
        current_node = next_node
    return current_node
x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')
x.next = y
y.next = z
cur_node = x
while cur_node:
    print(cur_node.value)
    cur_node = cur_node.next
print("------")
new_head = reverse(x)
print(new_head)
#
# print("reversed list:")
# cur_node = new_head
# while cur_node:
#     print(cur_node.value)
#     cur_node = cur_node.next
# print("-----")
# print(x.value, x.next)
# print(y.value, y.next.value)
# print(z.value, z.next)