import json

def solve_sudoku(grid):
    variables = [(r, c) for r in range(9) for c in range(9)]
    domains = {(r, c): list(range(1, 10)) if grid[r][c] == 0 else [grid[r][c]] for r, c in variables}
    
    neighbors = {var: set() for var in variables}
    for r1, c1 in variables:
        for r2, c2 in variables:
            if (r1, c1) != (r2, c2) and (r1 == r2 or c1 == c2 or (r1 // 3 == r2 // 3 and c1 // 3 == c2 // 3)):
                neighbors[(r1, c1)].add((r2, c2))

    def backtrack(assignment):
        if len(assignment) == len(variables): return assignment
        unassigned = [v for v in variables if v not in assignment]
        var = min(unassigned, key=lambda v: len([val for val in domains[v] if all(assignment.get(n) != val for n in neighbors[v])]))
        
        for value in domains[var]:
            if all(assignment.get(n) != value for n in neighbors[var]):
                assignment[var] = value
                result = backtrack(assignment)
                if result: return result
                del assignment[var]
        return None

    solution = backtrack({})
    if solution: return [[solution[(r, c)] for c in range(9)] for r in range(9)]
    return None

if __name__ == "__main__":
    with open('sudoku_board.json', 'r') as file:
        data = json.load(file)
    
    solved = solve_sudoku(data["board"])
    print("--- Solved Sudoku Board ---")
    for row in solved: print(row)
