def findMax(arr):
    
    max = arr[0]
    for nums in arr:
        if max < nums:
            max = nums 
    return max


def main():
    arr = [3,2,5,1,8,4]
    biggestInt = findMax(arr)
    print(biggestInt)
    

main()