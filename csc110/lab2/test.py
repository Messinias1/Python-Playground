n = int(input())
values = input().split()
min_value = 10 ** 9
min_index = 0
for i in range(n):
    num = int(values[i])
    if num < min_value:
        min_value = num
        min_index = i
print(min_index)