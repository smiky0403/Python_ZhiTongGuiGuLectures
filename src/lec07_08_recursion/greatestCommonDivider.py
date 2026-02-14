def gcd(num1:int, num2:int) ->int:
    
    if num2 == 0:
        return num1

    return gcd(num2, num1%num2)
    
    

def main():
    w1 = (3,5)
    res1 = gcd(w1[0], w1[1])
    print(res1)
    
    w2=  (115,100)
    res2 = gcd(w2[0], w2[1])
    print(res2)    

    w3 = (51,68)
    res3 = gcd(w3[0], w3[1])
    print(res3)    

main()
    