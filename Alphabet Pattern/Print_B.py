# Print B
number_of_rows = 5
number_of_cols = 7
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if cols==1 or (rows%2==1 and cols<5) or (rows%2==0 and cols ==7):
            print("* ",end="")
        else:
            print(" ",end="")
    print("")