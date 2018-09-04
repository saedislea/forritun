max_int = 0
#Get a number from the user
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

#Number most be positive
    #If the number is negative the program stops and finds the maximum number
while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int


#Print the maximum number
print("The maximum is", max_int)    # Do not change this line
