# x = [0,1,2,3,4,5,6,7,8,9]


for x in range(10):
    for y in range(10):
        print(f"{x*y:3}", end="")
    print()


for x in range(10):
    for y in range(10):
        if y == 9:
            print(f"{x*y:3}")
        else:
            print(f"{x*y:3}", end="")
#for i in y:
 #   print(f"")