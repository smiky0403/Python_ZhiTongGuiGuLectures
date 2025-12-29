from ArrayList_DIY import ArrayList_DIY as AL


arr = AL()

for i in range(10):
    arr.add(i)

arr.add_at(3, 99)
arr.remove_at(5)

print(arr.data)
print(arr.size, arr.capacity)
