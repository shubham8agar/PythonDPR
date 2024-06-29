arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]

n = len(arr)  ##12
count=0

#print(n)
var1 = []
for i in range(n):
    #print(i, ":", arr[i])
    if arr[i] != 0:
        var1.append(arr[i])
    else:
        count += 1
        
for i in range(0,count):
        var1.append(0)

print(var1)