cols = int(input())
es = ""
spacing = input().split()
og = input()
for i in spacing:
    es += og[int(i)-1::cols]
print(es)