import json

def solve_csp(variables, domains, neighbors):
    def backtrack(assignment):
        if len(assignment) == len(variables): return assignment
        var = [v for v in variables if v not in assignment][0]
        for color in domains:
            if all(assignment.get(n) != color for n in neighbors.get(var, [])):
                assignment[var] = color
                result = backtrack(assignment)
                if result: return result
                del assignment[var]
        return None
    return backtrack({})

if __name__ == "__main__":
    with open('australia_data.json', 'r') as file:
        data = json.load(file)
    
    solution = solve_csp(data["variables"], data["domains"], data["neighbors"])
    print("--- Australia Map Coloring Solution ---")
    for state, color in solution.items():
        print(f"{state}: {color}")
