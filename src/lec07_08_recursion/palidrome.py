def  partition(s):
    res = []
    n = len(s)
    subs = []
    
    def dfs(f):
        if f == n:
            res.append(subs.copy())
            
        for i in range(f, n):
            tmp = s[f: i + 1]
            if tmp == tmp[::-1]:
                subs.append(tmp)
                dfs(i + 1)
                subs.pop()                
            
    dfs(0)    
    return res



def main():
    s = "aab"
    res = partition(s)
    print(res)

main()