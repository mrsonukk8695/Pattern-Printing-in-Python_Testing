# Print O
number_of_rows = 4
number_of_cols = 4
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if rows==cols or rows+cols==5:
            print(" ",end="")
        else:
            print("* ",end="")
    print("")