# lambda функции

f = lambda x, y: x+y

# comprehensive
a =[x**2 for x in range(20) if x%2==0]
b =[x**2 if x%2==0 else 'None' for x in range(10) ]
c = [i for i in range(10)]
print(a)
print(b)

fibb = [0,1]
for i in range(2,10):
    fibb.append(fibb[i-2]+fibb[i-1])

print(fibb)

d = [(x,x**2) for x in fibb if x%2==0 and x!=0]
print(d)

e = map(lambda x: (x, x**2) if (x%2==0) else 'None', fibb)
print(f'{list(e)=}')

string = '1 2 3 4 5 6'
f = map(int, string.split())
print(list(f))

# filter

g = filter(lambda x: x%2==0, fibb)
print(list(g))

h = map(lambda x: (x, x**2), filter(lambda x: not x%2 and (x!=0), fibb))
print(list(h))

# zip

k = zip([1,2,3,4,5], ['q','w','e'], ['a','s','d'])
print(list(k))

# enumerate

l = enumerate(fibb)
print(list(l))