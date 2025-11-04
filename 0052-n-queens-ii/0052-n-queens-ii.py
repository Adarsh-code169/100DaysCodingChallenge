class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()        # occupied columns
        diag = set()        # occupied main diagonals (r - c)
        anti_diag = set()   # occupied anti-diagonals (r + c)
        self.count = 0
        
        def backtrack(r):
            if r == n:      # placed queens in all rows
                self.count += 1
                return
            
            for c in range(n):
                if c in cols or (r - c) in diag or (r + c) in anti_diag:
                    continue
                    
                # place queen
                cols.add(c)
                diag.add(r - c)
                anti_diag.add(r + c)
                
                backtrack(r + 1)
                
                # remove queen (backtrack)
                cols.remove(c)
                diag.remove(r - c)
                anti_diag.remove(r + c)
        
        backtrack(0)
        return self.count
