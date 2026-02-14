# half-half recursive, (while combine, do it assembly)
def merge_sort(arr):
    
    def dfs(arr):
        if len(arr) < 2:
            return arr
        
        mid = len(arr)//2
        
        left = arr[:mid]
        right = arr[mid:]
        
        res = merge(dfs(left), dfs(right))
        
        return res

    def merge(left, right):
        res = []
        i = j = 0
        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
            
        while i < len(left):
            res.append(left[i])
            i += 1
            
        while j < len(right):
            res.append(right[j])
            j += 1       
        
        return res


    return dfs(arr)
    
    
    
def main():
    arr = [1,6,5,2,7,3,4,8,0]
    arr= merge_sort(arr)
    print(arr)
    print(len(arr)//2)
    #
    
main()