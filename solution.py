assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'
diagonal_units=[]
def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units.append([rows[i]+cols[i] for i in range(0,9)])
diagonal_units.append([rows[i]+cols[8-i] for i in range(0,9)])
unitlist = row_units + column_units + square_units+diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    for unit in unitlist:
        temp_unit=unit.copy()
        twin_list_values=""
        #print(two_element_list)
        for element in temp_unit:
            if len(values[element])==2:
                for element1 in temp_unit[temp_unit.index(element)+1:]:
                    if  values[element]==values[element1]:
                        temp_unit.remove(element)
                        temp_unit.remove(element1)
                        twin_list_values=twin_list_values+values[element] 
	
        # Eliminate the naked twins as possibilities for their peers
        if len(twin_list_values)!=0:
            for element in temp_unit:
                for digit in twin_list_values: 
                    assign_value(values, element, values[element].replace(digit,''))                       
    return values

def cross(a, b):
    return [s+t for s in a for t in b]

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    grid_string={}
    assert len(grid)==81
    for i in range (0,81):
        if grid[i]=='.':
            assign_value(grid_string,boxes[i],'123456789')
        else:
            assign_value(grid_string,boxes[i],grid[i])
    return grid_string

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    #boxes_solved=[box for box in values.keys() if len(values[box]) == 1]
    for box in boxes:
        if len(values[box])==1:
            for peer in peers[box]:
                assign_value(values,peer, values[peer].replace(values[box],''))
    return values

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        for digit in '123456789':
            boxes=[]
            for box in unit:
                if digit in values[box]:
                   boxes.append(box)
            if  len(boxes)==1:
                assign_value(values,boxes[0], digit)           
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Your code here: Use the Eliminate Strategy
        values=eliminate(values)
        # Your code here: Use the Only Choice Strategy
        values=only_choice(values)
        # Your code here: Use the Naked Twins Strategy
        values=naked_twins(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # Stop the program if all boxes solved
        stalled=solved_values_after!=27
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values=reduce_puzzle(values)
    
    if values is False:
       return False
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s=min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    minimum_possibilities_position=s
    minimum_possibilities_value=values[minimum_possibilities_position]
    for digit in minimum_possibilities_value:
        temp_values=values.copy()
        temp_values[minimum_possibilities_position]=digit
        temp_solution=search(temp_values)
        if temp_solution:
            return temp_solution
    return False
def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values=grid_values(grid)
    return (search(values))

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
