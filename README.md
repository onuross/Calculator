# Basic Calculator Functions

This Python script defines a set of basic calculator functions, allowing users to perform various mathematical operations. The user is presented with a menu to choose an operation, and the script executes the corresponding function.

## Menu and Operations

The menu offers the following operations:
1. **Division**: Takes two numbers and calculates the quotient, remainder, and fraction.
2. **Exponentiation**: Calculates the result of raising a base to a given exponent.
3. **Prime Number Check**: Determines whether a given number is prime.
4. **Dividers**: Finds the dividers of a given number.
5. **Root**: Calculates the nth root of a number.
6. **Combination**: Computes the combination of two numbers.
7. **Permutation**: Computes the permutation of two numbers.
8. **Factorial**: Calculates the factorial of a number.
   
## Main Function and Execution

The `main()` function is the entry point of the script. It first calls `menuPrint()` to get the user's choice of operation. Depending on the choice, the script proceeds to execute the corresponding function.

## Calculator Functions

Each calculator function (`makeDivision`, `exponentiation`, `primeNumber`, `findDividers`, `takeRoot`, `combination`, `permutation`, `factorial`) is designed to perform a specific mathematical operation. Some of these functions are currently empty (`exponentiation`, `primeNumber`, `findDividers`, `takeRoot`, `combination`, `permutation`, `factorial`), and you may need to implement them based on your requirements.

## Input Validation

The script uses the `numberCheckOne` and `numberCheckTwo` functions for input validation, ensuring that the user enters valid integers.

## Additional Notes

- The `exponentiation`, `primeNumber`, `findDividers`, `takeRoot`, `combination`, `permutation`, `factorial` functions need to be implemented with their respective calculations.

- It seems there's a missing `return` statement in the `menuPrint()` function, and the menu items should be separated by line breaks.

- The `operator` variable in the `main()` function is used without being defined; you may want to ensure it's correctly implemented or rename it to match the menu item.

Feel free to complete the functions and adjust the script according to your specific needs.
