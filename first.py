arr = [1,2,3,4,5,6]

def get_sum(arr):
    totalsum = 0
    iteration = 0
    for num in arr:
        iteration = iteration+1
        print('iteration',iteration)
        totalsum = totalsum+num
    return totalsum

arr1 = [1,2,3,4,5,6,7]
print(get_sum(arr1))
