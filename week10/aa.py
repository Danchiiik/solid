nums = [2, 5, 1, 3, 4, 7]
n = 3
a = []
b = []
c = []
for i in nums[:n]:
    a.append(i)
for i in nums[n:]:
    b.append(i)

for i in range(len(a)):
    c.append(a[i])
    c.append()
    
print(a)
print(b)