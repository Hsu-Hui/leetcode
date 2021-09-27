class Solution:
    def reverse(self, x: int) -> int:
        plus_minus = ""
        reverse_x = ""
        if x<0:
            plus_minus = "-"
            x = -x
        for i in str(x):
            reverse_x = i + reverse_x
        reverse_x = plus_minus +reverse_x
        if int(reverse_x)>pow(2,31)-1 or int(reverse_x)<pow(-2,31):
            return 0
        return int(reverse_x)