# Print Z
number_of_rows = 6
number_of_cols = 6
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if rows+cols==7 or (rows==1 or rows==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")