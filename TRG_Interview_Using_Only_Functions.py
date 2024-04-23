"""
Exercise:
Write a method using Python that returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step. If begin value is greater than the end, function should return 0.

Examples:
sequence_sum(2,2,2) === 2
sequence_sum(2,6,2) === 12 // 2 + 4 + 6
sequence_sum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
sequence_sum(1,5,3) === 5 // 1 + 4
"""

def get_sequence_sum():
    # Prompt the user to input the beginning value of the sequence.
    input_begin = input('Insert begin value: ')

    # Check if the input is a float number
    while not input_begin.isdigit():
        # If input is not an integer, prompt the user to enter a correct integer number.
        print("Please enter an integer number.")
        input_begin = input('Insert correct begin value: ')

    # Prompt the user to input the end value of the sequence.
    input_end = input('Insert end value: ')

    # Check if the input is a float number
    while not input_end.isdigit():
        # If input is not an integer, prompt the user to enter a correct integer number.
        print("Please enter an integer number.")
        input_end = input('Insert correct end value: ')

    # Prompt the user to input the step value for the sequence.
    input_step = input('Insert step value: ')

    # Check if the input is a float number
    while not input_step.isdigit():
        # If input is not an integer, prompt the user to enter a correct integer number.
        print("Please enter an integer number.")
        input_step = input('Insert correct step value: ')

    # Convert input values to integers
    begin = int(input_begin)
    end = int(input_end)
    step = int(input_step)

    # Check if step value is 0
    while step == 0:
        print("Step value cannot be 0. It needs to be at least 1.")
        # Prompt the user again to input the step value
        input_step = input('Insert correct step value: ')
        # Check if the new input is a float number
        while not input_step.isdigit():
            # If input is not an integer, prompt the user to enter a correct integer number.
            print("Please enter an integer number.")
            input_step = input('Insert step value: ')
        # Convert the new input value to integer
        step = int(input_step)

    # Check if begin value is greater than end, return 0
    if begin > end:
        print("Begin value should not be greater than end value.")
        return 0

    # Initialize total_sum to 0
    total_sum = 0

    # Loop through the sequence and add each integer to the sum
    for i in range(begin, end + 1, step):
        total_sum += i

    # Return the total sum
    return total_sum

# Call the function and print the result
print("Total sum:", get_sequence_sum())
