# PROBLEM STATEMENT

Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

 - For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
 - 
Two formulas are concatenated together to produce another formula.

 - For example, "H2O2He3Mg4" is also a formula.
 - 
A formula placed in parentheses, and a count (optionally added) is also a formula.

 - For example, "(H2O2)" and "(H2O2)3" are formulas.

Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

# EXAMPLE

    Input: formula = "Mg(OH)2"
    Output: "H2MgO2"

Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

# APPROACH

The code is quite long but basically, we are doing these steps

    1. Evaluate the formula using a Stack such that we are left with no parenthesis
    2. Once done, we should have a number after each element's symbol in the stack
    3. We now take a dictionary and put each element with its count
    4. Take the keys of dictionary in sorted order and push the keys along with their values in output list
    5. Finally, return the list as a string.
