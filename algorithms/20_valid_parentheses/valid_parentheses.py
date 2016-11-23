class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        open_chars = {'(':1, '{':2, '[':3}
        open_chars_rev = {1:'(', 2:'{', 3:'['}
        close_chars = {')':1, '}':2 ,']':3}
        for char in s:
            if char in open_chars:
                stack.append(char)
            elif not stack:
                return False
            else:
                if stack.pop() != open_chars_rev[close_chars[char]]:
                    return False
        return len(stack) == 0

        

if __name__ == "__main__":
    x = Solution()
    print x.isValid("()")