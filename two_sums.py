nums = [2,7,4,11,5,15]
target=9
hash={}
coord=[]
for i,n in enumerate(nums):
    #print(i,n)
    diff =target-n
    #print(diff)
    print(hash)
    if diff in hash:
        print ([hash[diff],i])
        a=hash[diff],i
        coord.append(a)
    hash[n]=i
print(coord)
        



