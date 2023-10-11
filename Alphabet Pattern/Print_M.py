# Print M
number_of_rows = 5
number_of_cols = 5
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if (cols==1 or cols ==5 or(rows==cols)and rows<4) or (rows+cols==6 and rows<4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")