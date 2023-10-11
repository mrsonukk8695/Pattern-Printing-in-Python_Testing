# Print N
number_of_rows = 5
number_of_cols = 6
for rows in range(1,number_of_rows+1):
    for cols in range(1,number_of_cols):
        if(cols==1 or rows==cols or cols==5):
            print("*",end="")
        else:
            print(" ",end="")
    print("")