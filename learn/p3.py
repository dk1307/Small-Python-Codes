def convert(cel):
    f=(9/5)*float(cel)+32
    return f
cel=float(input("enter temp in cel:"))
if cel < 5:
    print(convert(cel))
else:
    print("its not convert")
