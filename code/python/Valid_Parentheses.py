class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                tmp.append(i)
            elif i=='}':
                if len(tmp)==0 or tmp.pop()!='{':
                    return False
            elif i==']':
                if len(tmp)==0 or tmp.pop()!='[':
                    return False
            elif i==')':
                if len(tmp)==0 or tmp.pop()!='(':
                    return False
        if len(tmp) != 0:
            return False
        return True
