#Print K
number_of_rows = 5
number_of_cols = 5
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if (cols ==2 or(rows==cols or rows+cols==6) and cols>2):
            print("*",end="")
        else:
            print(" ",end="")
    print("")