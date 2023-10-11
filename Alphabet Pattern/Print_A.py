# Print A
number_of_rows = 5
number_of_cols = 9
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if (rows+cols==6 or (cols-rows==3 and (rows!=1 and rows!=3 )) or (rows==3 and (cols==4 or cols==5))):
            print("*",end=" ")
        else:
            print(" ",end="")
    print(" ")