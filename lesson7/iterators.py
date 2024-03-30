num_list = [21, 73, 32]

for num in num_list:
    print(num)

iterator = iter(num_list)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
var = "loop"
print(f"{var:=^40}")

for item in iterator:
    print(item)
