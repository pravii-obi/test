# using two pointer
nums=[2,9,12,15]
target=14
l=0 # left pointer
r=len(nums)-1 # right pointer
while(l<r):
    sum=nums[l]+nums[r]
    if target==sum: 
        print(f" opstion is {l},{r} and pair value are {nums[l]} {nums[r]}")
    if target>sum: #our target greater the sum num to increamt the left pointer else decease right pointer
        l=l+1 # increse poniter
    else:
        r=r-1 # decrement pointer

