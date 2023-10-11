# Print Y
number_of_rows = 5
number_of_cols = 5
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if ((rows==cols)and rows<4) or (rows+cols==6 and rows<4) or (cols==3 and rows>3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")