class Solution:
    def isPalindrome(self, x: int) -> bool:
        result=''
        for i in str(x):
            result=i+result
        return result==str(x)