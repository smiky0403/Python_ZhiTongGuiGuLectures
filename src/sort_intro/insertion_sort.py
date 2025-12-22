# stable
#interate i
# search all left to i from right,  insert element i till amke sure i smaillest
#this make every iterate, i and its left are sorted small to large
def insertion_sort(arr):
    for i in range(1, len(arr) ):
        j = i
        temp = arr[i]
        while( j > 0 and temp > arr[j]):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp 
        
            
   # return arr

def main():
    arr = [1,2,6,2,3,9,7,8,11]
    insertion_sort(arr)
    print(arr)

main()