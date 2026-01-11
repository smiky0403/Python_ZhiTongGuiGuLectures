
x = dict()

x["a"] = 1
x["b"] = 2
x["c"] = 3
x["d"] = 4
x.update({"e":5})
print(x)
x0 = 3 in x.values()
x1 = "e" in x.keys()
print(x0, x1)

for k in x.keys():
    print(f"key = {k}", end = " ")
print()
for k0 in x:
    print(f"key = {k0}", end = " ")
print()
    

for v in x.values():
    print(f"value = {v}")

for k, v in x.items():
    print(f"key = {k} ; value = {v}", sep = ";")
    
x.update({'a': 10})
print(f"values: {list(x.values())} ; keys: {list(x.keys())}" )



#x[6] += 100   #not working
x["f"] = x.get("f", 100) + 1

print(f"values: {list(x.values())} ; keys: {list(x.keys())}" )
    

#x.update("a" : 10)

y = set()
y.add(1)
y.add(2)
y.add(3)
y.add(3)
y.add(4)
y.add(5)
y.add(6)
y.add(6)
y.add(7)
y.add(8)
print("Set: ", list(y))
y0 =  7 in y
print(y0)

y.pop()
y.pop()
print("Set: ", list(y))
y.remove(4)
y.remove(6)
print("Set: ", list(y))
y.discard(7)
print("Set: ", list(y))



for k in y:
    print(k, sep = "  ", end = " ; ")
    
print()




"""
strs = "cat dog dog cat"
wd = strs.split(" ")
print(wd)
"""