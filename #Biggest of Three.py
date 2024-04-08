#Biggest of Three

p = int(input("Give me a number: "))
q = int(input("Another: "))
r = int(input("This is the last one: "))

if p == q == r:
    print("Same thing")
elif p >= q and p >= r:
    print(f"The biggest number is {p}.")
elif q >= p and q >= r:
    print(f"The biggest number is {q}.")
else:
    print(f"The biggest number is {r}.")
