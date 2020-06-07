class Solution:

    def reverse(self, x: int) -> int:
        """
        整数反转
        """

        if x > 2**31-1 and x < -2**31 :
            return 0

        if x >= 10 or x <= -10:
            if x > 0 :
                x_r = int(str(x)[::-1])
            else :
                x_r = - int(str(x)[:0:-1])
        else :
            x_r = x

        return x_r if x_r < 2**31-1 and x_r > -2**31 else 0