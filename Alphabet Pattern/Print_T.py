#Print T
number_of_rows = 5
number_of_cols = 5
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if ((rows==1) or (cols==3)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")