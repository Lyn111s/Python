result = 0

for a in range(4):
    num = int(input())
    if num < 0:
        break
    result += num

print(result)