import json

def solve_csp(variables, domains, neighbors):
    # Ensure bidirectional graph
    for node, edges in list(neighbors.items()):
        for edge in edges:
            if edge not in neighbors: neighbors[edge] = []
            if node not in neighbors[edge]: neighbors[edge].append(node)

    def backtrack(assignment):
        if len(assignment) == len(variables): return assignment
        # MRV Heuristic
        unassigned = [v for v in variables if v not in assignment]
        var = min(unassigned, key=lambda v: len([c for c in domains if all(assignment.get(n) != c for n in neighbors.get(v, []))]))
        
        for color in domains:
            if all(assignment.get(n) != color for n in neighbors.get(var, [])):
                assignment[var] = color
                result = backtrack(assignment)
                if result: return result
                del assignment[var]
        return None
    return backtrack({})

if __name__ == "__main__":
    with open('telangana_data.json', 'r') as file:
        data = json.load(file)
    
    solution = solve_csp(data["districts"], data["domains"], data["neighbors"])
    print("--- Telangana Map Coloring Solution ---")
    if solution:
        for district, color in solution.items(): print(f"{district}: {color}")
    else:
        print("No solution found. Check adjacency list.")
