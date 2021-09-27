class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        tmp=''

        for i in zip(*strs):
            if len(set(i)) == 1:
                tmp += i[0]
            else:
                break
        return tmp