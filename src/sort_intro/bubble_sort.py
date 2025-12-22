#  from left to right, 1 by 1 neighbor compare, move larger to right like a bubble 
def bubble_sort(arr):
    
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] =  arr[j + 1], arr[j]
   #return arr


def main():
    arr = [3, 5, 1, 2, 9, 7, 8, 0, 11]
    bubble_sort(arr)
    print(arr)
    
    
main()