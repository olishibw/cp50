x = float(input("what is x? "))
y = float(input("what is y? "))

t = input("what kind of operator? ")
if t == "-":
    w = round(x-y)
    print(w)
elif t == "/":
    r = (x/y)
    print(r)
elif t == "*":
    e = round(x*y)
    print(e)
elif t == "+":
    z = round(x+y)
    print(f"{z:,}")  # format sting
