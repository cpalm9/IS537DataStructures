a = [1,4,6,9]
b = [2,3,4,5,6,8,10]
c = []
# loop through the arrays to append the elements to the new array
# for x in range(len(b)):
#     # check if the elements are less than or greater than the current
#     # you need to make sure the indexes are in the range
#     a.append(b[x])
#     # if b[x] < a[x]:
#     #     a.append(a[x])
#     # else:
#     #     a.append(b[x])
#     if a[x] < a[x + 1]:
#         a[x] = a[x]
#     else:
#         a[x] = a[x + 1]

## didn't get it in time

## correct way

ai = 0
bi = 0
while ai < len(a) and bi < len(b):
    if a[ai] < b[bi]:
        c.append(a[ai])
        ai+=1
    else:
        c.append(b[bi])
        bi+=1
print(c)

# c = sorted(a + b)
# print(c)
    
    