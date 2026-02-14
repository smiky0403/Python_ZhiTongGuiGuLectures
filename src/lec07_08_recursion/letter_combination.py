def  letterCombinations(digits):
    p_char = { '2': 'abc', '3': 'def', '4':'ghi',
             '5':'jkl', '6':'mno', '7':'pqrs',
             '8':'tuv', '9':'wxyz','*':'+',
             '0':' '}
    
    path = []
    res = []
    n = len(digits)
    
    def dfs(f):
        if f == n:
            res.append(''.join(path.copy()))
            return
        
        tmp = digits[f]
        for ch in p_char[tmp]:
            path.append(ch)
            dfs(f + 1)
            path.pop()
            
        
    dfs(0)
    return res

def main():
    digits = '23'
    res = letterCombinations(digits)
    
    print(res)
    
main()