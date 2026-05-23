# second largest array
arr=[10,20,30,40,50,60]
f_max=arr[0]
s_max=arr[0]
if len(arr)<=1:
    print(" your arry contains one elemnts")
else:
    for i in range(1,len(arr)): # first loop for finding fist element
        if f_max<arr[i]:
            f_max=arr[i]
    for i in range(1,len(arr)):#second loop for finding elemnt element 
        if s_max<arr[i] and arr[i]!=f_max: # this condition ingoner the first max elemnt and return second max
            s_max=arr[i]   
print(s_max)
