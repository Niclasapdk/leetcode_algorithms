nums = [0,0,1,1,1,1,2,2,3,3,4]

def remove_dups(arr):
    j = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[j] = arr[i]
            j += 1
    del arr[j::]
    return j, arr

print(remove_dups(nums))