class Solution(object):
    def scoreOfParentheses(self, s):
        depth = 0
        score = 0
        for i in range(len(s)):
            if s[i] == '(':
                depth = depth + 1
            else:
                depth = depth - 1
                if s[i - 1] == '(':
                    score = score + (2 ** depth)
        return score

sol = Solution()
print(sol.scoreOfParentheses('()'))
print(sol.scoreOfParentheses('(())'))
print(sol.scoreOfParentheses('()()'))
print(sol.scoreOfParentheses('((()))'))
print(sol.scoreOfParentheses('(()())'))
print(sol.scoreOfParentheses('()(())'))