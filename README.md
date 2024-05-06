
## Welcome to my TRG Group interview process!

### Exercise Description:

In this exercise, you'll find a Python method designed to calculate the sum of a sequence of integers based on three non-negative values: begin, end, and step. If the begin value exceeds the end value, the function returns 0.

Examples:

sequence_sum(2,2,2) === 2

sequence_sum(2,6,2) === 12 // 2 + 4 + 6

sequence_sum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5

sequence_sum(1,5,3) === 5 // 1 + 4

### Approach:
To enhance user interaction, the code prompts users to input values directly in terminal. 
The project has incorporated input validation to ensure users provide only integer values, minimizing the risk of errors. 

![image](https://github.com/AdiMosoiu93/TRG_Interview_Project/assets/130320111/b2dfde13-5f9d-4a83-9dcd-4a6e62cba33e)


### What I learned from doing this exercise:
1. When using the **"range()"** function, the end value should be adjusted by adding 1 to include the specified value.
2. The **"isdigit()"** function can be utilized to verify the absence of alphabetical characters or symbols commonly found in floating-point numbers. This ensures that only integers are accepted. To enforce this condition, the "isdigit()" function was incorporated within a "while not" loop.

I found this exercise to be an engaging one!

Thank you.


## The project also includes a test case using Selenium and PyTest:
### Description of test case: check if user can enter a html tag.

Precondition: the check counter is 0.

Steps to reproduce: 

1. Go to http://testingchallenges.thetestingmap.org/index.php.
2. In the "First Name" input field enter `<h1>TRG Group</h1>`.
3. Click on the "Submit" button.

   Expected results:
   - the check counter increases by 4
   - the confirmation message is updated with the entered first name
   - username is updated with the entered first name
   
