#https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

def printLinkedList(head):
    if head:
        print(head.data)
        printLinkedList(head.next)
