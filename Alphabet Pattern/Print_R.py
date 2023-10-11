#Print R
number_of_rows = 5
number_of_cols = 5
for rows in range(1, number_of_rows+1):
    for cols in range(1,number_of_cols+1):
        if ((cols==1 or rows%2!=0 and rows<4 and cols<5 )or (cols==5 and rows==2) or (rows==4 and cols==3) or (rows==5 and cols==4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")