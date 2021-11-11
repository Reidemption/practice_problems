  #https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

def reversePrint(llist):
  if llist:
      reversePrint(llist.next)
      print(llist.data)
