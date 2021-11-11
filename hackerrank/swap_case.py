#https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    new_case= ''
    for i in s:
        if i.isupper():
            new_case += i.lower()
        elif i.islower():
            new_case += i.upper()
        elif i.isspace():
            new_case += " "
        else:
            new_case += i
    return new_case
