class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(cur_par: List[int], op_brackets: int, cl_brackets: int) -> None:
            if op_brackets == n and cl_brackets == n:
                res.append(''.join(cur_par))
                return
            
            cur_par.append('(')
            if op_brackets < n:
                backtrack(cur_par, op_brackets + 1, cl_brackets)
            cur_par.pop()
            cur_par.append(')')
            if cl_brackets < op_brackets:
                backtrack(cur_par, op_brackets, cl_brackets + 1)
            cur_par.pop()
        
        backtrack([], 0, 0)
        return res