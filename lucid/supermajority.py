num = int(input())
list_of_dups = []
dup = 0
for i in range(num):
    x = int(input())
    list_of_dups.append(x)
for var in list_of_dups:
    if list_of_dups.count(var) > dup:
        dup = list_of_dups.count(var)

#print(dup, list_of_dups)
#print(dup,  len(list_of_dups) * (2/3))
if dup > len(list_of_dups) * (2/3):
    print("True")
else:
    print("False")