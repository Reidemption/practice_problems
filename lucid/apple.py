def main(fruit):
    sample = ['a','p','l','e']
    it = 1
    count = 0
    a = 0
    p = 0
    l=0
    e=0
    if "a" in fruit and "p" in fruit and "l" in fruit and "e" in fruit:
        #print("a" * it + "p" *2 * it + "l" * it + "e" * it)
        a = fruit.count('a')
        p = fruit.count('p')
        p = p//2
        l = fruit.count('l')
        e = fruit.count('e')
    nl = [a,p,l,e]
    count = min(nl)
    print(count)

main("a1app2ppl3lee")