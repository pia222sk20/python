# remove
list_a = [1,1,1,2]
# list_a.remove(1)
# print(list_a)
# 1. solution
for i in range(len(list_a)-1,-1,-1):
    if list_a[i] == 1:
        del list_a[i]

print(list_a)        
    
# remove
list_a = [1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(list_a)):    
    print('*')
    if 1 in list_a:
        list_a.remove(1)
    else:
        break

print(list_a)        
