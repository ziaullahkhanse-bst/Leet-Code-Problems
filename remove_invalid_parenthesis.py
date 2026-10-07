class Solution(object):
    def removeInvalidParentheses(self, s):
        answers = []
        already_seen = set()
        to_check = [s]
        
        while to_check:
            current = to_check.pop(0)
            
            if current in already_seen:
                continue
            already_seen.add(current)
            
            if self.is_valid(current):
                answers.append(current)
                continue
            
            if answers:
                continue
            
            for i in range(len(current)):
                if current[i] == '(' or current[i] == ')':
                    shorter = current[:i] + current[i+1:]
                    to_check.append(shorter)
        
        return answers
    
    def is_valid(self, s):
        open_count = 0
        for char in s:
            if char == '(':
                open_count = open_count + 1
            elif char == ')':
                open_count = open_count - 1
                if open_count < 0:
                    return False
        return open_count == 0


sol = Solution()
print(sol.removeInvalidParentheses("()())()"))
print(sol.removeInvalidParentheses("(a)())()"))
print(sol.removeInvalidParentheses(")("))
print(sol.removeInvalidParentheses("()"))
print(sol.removeInvalidParentheses("(())"))
print(sol.removeInvalidParentheses("())"))