n = int(input())
l = list(map(int,input().split()))
m = int(input())
num = list(map(int,input().split()))
l.sort()

def search(arr, low, high, x):
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return 1
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return 0

for i in num:
    print(search(l,0,n-1,i))
