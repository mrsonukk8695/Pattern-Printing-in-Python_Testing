# Print D
number_of_rows = 5
number_of_cols = 9
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if cols==2 or (rows%4==1 and cols<5) or ((rows==3 or rows%2==0) and cols ==8):
            print("* " ,end="")
        else:
            print(" ",end="")
    print("")