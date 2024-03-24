try:
    # print(hello)
    print("hello")
except NameError as err:
    print(err)
else:
    print("I am ELSE")
finally:
    print("FINALLY code")
