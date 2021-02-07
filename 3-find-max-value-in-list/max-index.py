arr = [1,2,1,3,5,6,4,55,66]
len_arr = len(arr)
max_val = arr[0]
max_index = 0
for l in range(1,len_arr):
    if max_val < arr[l]:
        max_val = arr[l]
        max_index = l
print("Result = Max value in array {0} and Index at {1} ".format(max_val,max_index))