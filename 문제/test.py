inp = []
result = []

for i in range(10):
    inp.append(int(input()))

for i in range(len(inp)):
    result.append(inp[i]%42)

print(result)
result = set(result)
print(result)
print(len(result))