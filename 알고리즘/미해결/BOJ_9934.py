arr = [[] for i in range(3)]
inputarr = [1,6,4,3,2,5,7]

def inorder(inputarr, size):
    if(len(arr) == 1):
        return
    mid = len(arr)//2
    arr[size].append(inputarr[mid])
    inorder(inputarr[:mid], size+1)
    inorder(inputarr[mid+1:], size+1)

inorder(inputarr,0)
print(arr)