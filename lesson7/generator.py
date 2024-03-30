def raise_to_the_degrees(num, max_deg):
    i = 0
    for item in range(max_deg):
        yield num ** i
        i += 1


res = raise_to_the_degrees(10, 5)

print(res)

for i in res:
    print(i)
