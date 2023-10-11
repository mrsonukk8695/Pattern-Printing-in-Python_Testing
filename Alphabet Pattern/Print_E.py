# Print E
number_of_rows = 5
number_of_cols = 5
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols):
        if (cols==1 or rows%2==1):
            print("* ",end="")
        else:
            print(" ",end="")
    print("")