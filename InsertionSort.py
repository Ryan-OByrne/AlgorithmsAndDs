def insertionSort(numArr):
    for i in range(1, len(numArr)):
        key = numArr[i]
        j = i-1
        while j >=0 and numArr[j] > key:
            numArr[j+1] = numArr[j]
            j -= 1
        numArr[j+1] = key
    
    return numArr

def main():
    numArr = [9,8,7,6,5,4,3,2,1]
    print(numArr)
    sortedNumArr = insertionSort(numArr)
    print(sortedNumArr)
    
    
main()