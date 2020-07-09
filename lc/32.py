

from typing import List


class Solution:
    """
    最长的有效括号
    """

    def longestValidParentheses(self, s) -> int:
        stack = []
        res = 0
        # str(a)
        for i in range(len(s)):
            # print(i)
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)
            else:
                stack.pop()
                res = max(res, i - (stack[-1] if stack else -1))
        return res


if __name__ == '__main__':
    str = "((()))()))"
    s = Solution()
    lend = s.longestValidParentheses(str)
    print(lend)
