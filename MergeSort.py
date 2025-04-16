def merge(numArr, p, q, r):
    L = numArr[p:q+1]
    R = numArr[q+1:r+1]
    
    L.append(float('inf'))
    R.append(float('inf'))
    
    i = j = 0
    
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            numArr[k] = L[i]
            i += 1
        else:
            numArr[k] = R[j]
            j += 1
    
def mergeSort(numArr,p,r):
    if p < r:
        q = (p+r)//2
        mergeSort(numArr,p,q)
        mergeSort(numArr,q+1,r)
        merge(numArr,p,q,r)
    return numArr
    

def main():
    numArr = [9,8,7,6,5,4,3,2,1]
    print(numArr)
    sortedNumArr = mergeSort(numArr, 0, len(numArr)-1)
    print(sortedNumArr)
    
    
main()