am=['note','ddd','yuguy','jklk','jdndd']
print(am[1::2])
print(am[::-1])
print(am)

am[0]='random'
print(am)

z=am

z[0]='haha'
print(z)
print(am)


z=am[:]
z[0]='new'
print(z)
print(am)
