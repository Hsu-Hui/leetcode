class Solution:
    def romanToInt(self, s: str) -> int:
        number={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=number[s[0]]
        for i in range(1,len(s)):
            v1=number[s[i]]#右邊
            v2=number[s[i-1]]#左邊
            if(v2>=v1):
                sum=sum+v1
            else:
                sum=sum+v1-2*v2
        return sum
        