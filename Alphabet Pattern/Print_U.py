# Print U
number_of_rows = 5
number_of_cols = 5
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if ((cols==1 or cols==5) and rows<5) or  (rows==5 and (cols!=1 and cols<5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")