def  subsets(nums):
    res = []
    n = len(nums)
    sub = []
    
    def dfs(f):
        if f == n:
            return
        
        for i in range(f, n):
            sub.append(nums[i])
            res.append(sub.copy())
            dfs(i + 1)
            sub.pop()
            
    dfs(0)
    return res


def main():
    x = [1, 2, 3]
    res = subsets(x)
    print(x)
    print(res)
    
main()