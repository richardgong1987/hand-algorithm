def hanoi(n, a='a',b='b',c='c'):
 if n >=1:
    hanoi(n-1, a,c,b)
    print(f' From {a} to {c}')
    hanoi(n-1, b,a,c)



hanoi(3)

# \alpha