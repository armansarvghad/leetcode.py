"""
LeetCode Problem: Sudoku Solver
Problem Number: 37
Difficulty: Hard
Topic: Backtracking
Link: https://leetcode.com/problems/sudoku-solver/
"""

class Solution:
    # Naive Check
    # Time Complexity: O(9^n) -> Time Limit Exceeded
    # Space Complexity: O(1)
    def solveSudoku(self, board):
        def validChoice(row, col, choice):
            for i in range(9):
                if board[i][col] == choice:
                    return False
                if board[row][i] == choice:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == choice:
                    return False
            return True

        def solve(row, col):
            if row == 9:
                return True
            if col == 9:
                return solve(row + 1, 0)

            if board[row][col] == ".":
                for choice in range(1, 10):
                    if validChoice(row, col, str(choice)):
                        board[row][col] = str(choice)
                        if solve(row, col + 1):
                            return True
                        else:
                            board[row][col] = "."
                return False
            else:
                return solve(row, col + 1)                

        solve(0, 0)

    # Hash Sets
    # Time Complexity: O(9^n)
    # Space Complexity: O(1)
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]

        empty = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    digit = int(board[r][c])
                    rows[r].add(digit)
                    cols[c].add(digit)
                    sqrs[(r // 3) * 3 + (c // 3)].add(digit)
        
        def solve(idx):
            if idx == len(empty):
                return True
            
            r, c = empty[idx]
            sqr = (r // 3) * 3 + (c // 3)

            for digit in range(1, 10):
                if not (digit in rows[r]) and not (digit in cols[c]) and not (digit in sqrs[sqr]):
                    rows[r].add(digit)
                    cols[c].add(digit)
                    sqrs[(r // 3) * 3 + (c // 3)].add(digit)
        
                    board[r][c] = str(digit)
                    if solve(idx + 1):
                        return True
                    
                    sqrs[sqr].remove(digit)
                    cols[c].remove(digit)
                    rows[r].remove(digit)

        solve(0)

    # Bitmasks
    # Time Complexity: O(9^n)
    # Space Complexity: O(1)
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        sqrs = [0] * 9

        empty = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    digit = int(board[r][c])
                    rows[r] |= 1 << digit
                    cols[c] |= 1 << digit
                    sqrs[(r // 3) * 3 + (c // 3)] |= 1 << digit
        
        def solve(idx):
            if idx == len(empty):
                return True
            
            r, c = empty[idx]
            sqr = (r // 3) * 3 + (c // 3)

            for digit in range(1, 10):
                if not ((1 << digit) & rows[r]) and not ((1 << digit) & cols[c]) and not ((1 << digit) & sqrs[sqr]):
                    rows[r] |= 1 << digit
                    cols[c] |= 1 << digit
                    sqrs[sqr] |= 1 << digit
        
                    board[r][c] = str(digit)
                    if solve(idx + 1):
                        return True
                    
                    sqrs[sqr] ^= 1 << digit
                    cols[c] ^= 1 << digit
                    rows[r] ^= 1 << digit

        solve(0)