a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

d = [(i, [(j, [k for k in c]) for j in b]) for i in a]
print(d)
