# Print W
number_of_rows = 5
number_of_cols = 30
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if (rows==cols or (rows+cols==10 and rows>=3) or (cols-rows==4 and rows>3) or rows+cols==14):
            print("*",end="")
        else:
            print(" ",end="")
    print("")