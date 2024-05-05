class SequenceSumCalculator:
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.step = 0

    def get_input(self):
        # Prompt the user to input the beginning value of the sequence.
        self.begin = self.get_valid_input("Insert begin value: ")

        # Prompt the user to input the end value of the sequence.
        self.end = self.get_valid_input("Insert end value: ")

        # Prompt the user to input the step value for the sequence.
        self.step = self.get_valid_input("Insert step value: ")

        # Check if begin value is greater than end, return 0
        if self.begin > self.end:
            print("Begin value should not be greater than end value.")
            return 0

    def get_valid_input(self, message):
        input_value = input(message)
        while not input_value.isdigit():
            print("Please enter an integer number.")
            input_value = input("Insert correct value: ")
        return int(input_value)

    def calculate_sequence_sum(self):
        total_sum = 0
        # Loop through the sequence and add each integer to the sum
        for i in range(self.begin, self.end + 1, self.step):
            total_sum += i
        return total_sum

# Below is an alternative approach achieving the same functionality as the `range()` function used in the previous method.
# total_sum = 0
#         # Loop through the sequence and add each integer to the sum
#         current_value = self.begin
#         while current_value <= self.end:
#             total_sum += current_value
#             current_value += self.step
#         return total_sum

# Create an instance of the SequenceSumCalculator class
sequence_calculator = SequenceSumCalculator()

# Get user input for sequence parameters
sequence_calculator.get_input()

# Calculate and print the total sum
print("Total sum:", sequence_calculator.calculate_sequence_sum())
