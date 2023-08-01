l = [[1,2,4,5,3],[4,6,3,2],[-55,3,7,9,5]]
max = 0
HighValueIndex = 0
for i in l:
	currentSum = sum(i)
	if(currentSum>max):
		max = currentSum
		HighValueIndex = i
print(max)
print(HighValueIndex)
print(l.index(HighValueIndex))
