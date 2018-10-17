a=[1,4,5,-4,-1,2,-5,-5,2,7,-1]

dodatnie = 0
ujemne = 0

for x in a:
    if x > 0:
        # dodatnie = sum(a)
        dodatnie += 1
    elif x<0:
        ujemne += 1

print(f"Ujemnych: {ujemne} , Dodatnich {dodatnie}")
