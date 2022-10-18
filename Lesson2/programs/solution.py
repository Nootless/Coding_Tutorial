# DO NOT VIEW UNTIL YOU HAVE FINISHED THE CALCULATOR

if __name__ == '__main__':

    operations = {
        '+':1,
        '-':2,
        '*':3,
        '/':4
    } # operations that can be computed 
    
    # default to yes 
    user_input = 'y'
    
    while user_input == 'y':
        print('==================================')
        # Variables to keep track of numbers and operator
        num1 = float(input('First Number: '))
        num2 = float(input('Second Number: '))
        operate = input('Operation(+,-,*,/): ')
        num3 = None

        # used to go through each operation
        if operations.get(operate) == 1:
            num3 = num1 + num2
        elif operations.get(operate) == 2:
            num3 = num1 - num2
        elif operations.get(operate) == 3:
            num3 = num1 * num2
        elif operations.get(operate) == 4:
            num3 = num1 / num2
        
        # prints out the numbers
        print(f'\n{num1} {operate} {num2} == {num3}')
        print('==================================')
        user_input = input('Continue? (y/n): ')
