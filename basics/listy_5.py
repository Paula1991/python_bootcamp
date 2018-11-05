print("   ", end=" ")
for x in range(10):
    print(f"{x:2}",end =" ")

print()
print()

for x in range(10):
    print(x, end="  ")
    for y in range(10):
        print(f"{x*y:3}", end="")
    print()


#for x in range(10):
#    for y in range(10):
#        if y == 9:
#          print(f"{x*y:3}")
#        else:
#          print(f"{x*y:3}", end="")
