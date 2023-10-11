# Print F
number_of_rows = 5
number_of_cols = 4
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if (cols==1 or rows%2!=0 and rows<5) :
            print("* ",end="")
        else:
            print(" ",end="")
    print("")