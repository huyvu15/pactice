def eight_queens(board_size):
    def is_valid(queens):
        left = right = col = queens[-1]
        for r in reversed(queens[:-1]):
            left, right = left-1, right+1
            if r in (left, col, right):
                return False
        return True
    
    def solve(queens):
        if len(queens) == board_size:
            return queens
        for col in range(board_size):
            if col not in queens:
                queens.append(col)
                if is_valid(queens):
                    solution = solve(queens)
                    if solution:
                        return solution
                queens.pop()
        return None
    
    return solve([])

solution = eight_queens(12)
print(solution)