nums = [2,3,1,1,1]
n = len(nums)
i = -1
step = 0
check = 0
while(i<n-1):
    if(nums[i] == 0 or nums[0] == 0):
        check = -1
        break
    if(i == -1):  
        i+=nums[0]
        step+=1
    else:
        i+=nums[i]
        step+=1
if(check == -1):
    print("Not able to jump and the step is:",step)
else:
    print("Number of steps to jump the entire array:", step)
        