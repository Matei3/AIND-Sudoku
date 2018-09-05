# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver
In this project I have developed an agent which can solve a Sudoku puzzle using constraint propagation. 

The basic implementation of the project required the use of one strategy, **Naked twins** and to impose diagoanl constraints, but I have further implemented 2 more strategies: **Only Choice** and **Hidden Twins**. 

Below are 2 questions that were asked to check the students' understanding of the solutions they provided.


# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: In order to solve the naked twins problem using constraint propagation we need to first look for 'twins'. 
   They are boxes with the same 2 possible solutions in the same unit and then eliminate the  possible solutions for the twins from the possible solutions of all the other boxes in the unit.
   For this we apply the following steps on all the units in the unit list:
   
   Step 1. Find the possible twins:
              We create a copy of the unit and go over it box by box.
           When we find a box with 2 possible solutions we check the remainder of the unit to see if we can find a box with same possible solutions.
           If we do find the second box with the same possible solutions, we eliminate the 2 boxes from the unit in order to narrow the searchspace and also not to get the pair twice, and add the possible solutions to a string that we will call twin_values.
           Once we have done this operation up to the end of the unit we check to see if our string with possible solutions for twins is empty.
           If the if the twin_values string is empty ,we move to the next unit and apply Step1, if not we move to Step2.
   
   Step 2. Eliminate the solutions of the twins from all the other boxes:
           Now the copy of our unit contains just the non-twin boxes while all the values for a twin are in the twin_value string.
           All we have to do now is to go through all the remanining boxes in the copy of the unit and eliminate the solutions that appear in the twin_value string.
           Next, we move to the next unit.
             

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: In order to solve the diagonal sudoku problem we just add the diagonals to the units in our problem. 
   Now all constraint propagation strategies that are applied on units(naked twins, only choice) will be used across the diagonal, 
   imposing the 1-element per unit constraint of sudoku on it. 

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
