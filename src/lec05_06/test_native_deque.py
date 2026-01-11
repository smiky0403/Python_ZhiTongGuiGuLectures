from collections import deque

x = deque()
x.append(10)
x.append(20)
x.append(30)
x.append(40)
x.append(50)
x.append(60)
x.append(70)
x.append(80)

print(x)

x.pop()
x.pop()

print(x[-1])  #peel
print(x)

x.popleft()
x.popleft()
x.popleft()
x.appendleft(100)
x.appendleft(110)

print(x[0]) #peek left
print(x)

x.remove(40)
print(x)
x.reverse()
print(x)
x.clear()
print(x)

print("123".isdigit())
print("-123".isalpha())