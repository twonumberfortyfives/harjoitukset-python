#z = int(input("z = "))  # Enter a value for variable y
#x = int(input("x = "))  # Enter a value for variable x
#def numero(y):
#    return z - x  # Return the difference between z and x
#y = 0  Initialize the variable y (can be any value, depending on your logic)
#print(numero(y))  # Display the result of calling the function numero(y)
#------------------------------------------------------------------------------
#def max_sum(A):
#    x = 0                      # Initialize the variable x to accumulate the sum of elements
#    for i in A:                # Start of loop: for each element i in the list A
#        x += int(i)            # Add the integer value of i to the current sum x
#    return x / len(A)          # Return the average value by dividing the sum by the number of elements in the list
#
#try:
#    A = input("numbers: ").split()    # Input a string of numbers and split it into a list of elements
#    print(max_sum(A))                 # Call the max_sum function with the entered list and print the result
#except ValueError:
#    print("Input error")              # If a ValueError occurs, print the "Input error" message
#------------------------------------------------------------------------------
#guys = [12, 32, 4, 12]  # A list of numbers
#for i in range(len(guys)):  # Loop through each index in the list 'guys'
#    if guys[i] % 2 == 0:    # Check if the number at index 'i' is even
#        print("yes")        # If even, print "yes"
#    else:
#        print("no")         # If not even, print "no"
#-----------------------------------------------------------------------------
#def large(arr): 
#    maxss_ = arr[0]       # Initialize the variable maxss_ with the first element of the array 'arr'
#    for ele in arr:       # Loop through each element 'ele' in the array 'arr'
#        if ele < maxss_:  # Compare the current element 'ele' with the current smallest value 'maxss_'
#            maxss_ = ele   # If 'ele' is smaller than 'maxss_', update 'maxss_' to 'ele'
#    return maxss_         # Return the smallest value found
#
#list1 = [1, 4, 5, 2, 6]   # Example list of numbers
#
#result = large(list1)    # Call the function 'large' with the list 'list1' to find the smallest element
#print(result)            # Print the result (the smallest element in the list)
#------------------------------------------------------------------------------
#def calc_average(lst):
#    return sum(lst) / len(lst)  # Calculate the average by summing up the list and dividing by its length
#
#lst = [24, 19, 35, 46, 75, 29, 30, 18]  # Example list of numbers
#
#average = calc_average(lst)  # Calculate the average of the list using the calc_average function
#print("middle ", round(average, 3))  # Print the rounded average value with the message "middle "
