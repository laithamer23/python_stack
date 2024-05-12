# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]


# def bigsizenumber(number):
    
    
    # for i in range(len(number)):
        # if number [i] > 0:
            # number [i]= "big"
    # return number


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).

def replacethevalue(number):
   count = 0
   replacethevalue= sum(1 for num in number if num >0 )
   if number:
        number[-1] = replacethevalue


     

          
        



            