
## Welcome to my TRG Group interview process!

Exercise Description:
In this exercise, you'll find a Python method designed to calculate the sum of a sequence of integers based on three non-negative values: begin, end, and step. If the begin value exceeds the end value, the function returns 0.

Examples:
sequence_sum(2,2,2) === 2
sequence_sum(2,6,2) === 12 // 2 + 4 + 6
sequence_sum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
sequence_sum(1,5,3) === 5 // 1 + 4

Approach:
To enhance user interaction, the code prompts users to input values directly. 
The project has incorporated input validation to ensure users provide only integer values, minimizing the risk of errors. 

What I learned from doing this exercise:
1. When using the "range()" function, the end value should be adjusted by adding 1 to include the specified value.
2. The "isdigit()" function can be utilized to verify the absence of alphabetical characters or symbols commonly found in floating-point numbers. This ensures that only integers are accepted. To enforce this condition, the "isdigit()" function was incorporated within a "while not" loop.

I found this exercise to be an engaging one!
Thank you.
