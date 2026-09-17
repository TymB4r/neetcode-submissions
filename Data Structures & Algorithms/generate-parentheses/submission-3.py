class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(cur_par: List[str], op_brackets: int, cl_brackets: int) -> None:
            if op_brackets == n and cl_brackets == n:
                res.append(''.join(cur_par))
                return
            
            if op_brackets < n:
                cur_par.append('(')
                backtrack(cur_par, op_brackets + 1, cl_brackets)
                cur_par.pop()
            
            if cl_brackets < op_brackets:
                cur_par.append(')')
                backtrack(cur_par, op_brackets, cl_brackets + 1)
                cur_par.pop()
        
        backtrack([], 0, 0)
        return res