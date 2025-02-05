# remove duplicates

list1 =[1,1,1,2,2,3,4,5,2,5,7,8,9,10,11,23,44,55,66,77,66,55,65,67]

ans=[]

for item in list1:
    if item not in ans:
        ans.append(item)



print(ans)

print(list(set(list1)))