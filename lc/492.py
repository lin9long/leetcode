class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        """
        构建矩形
        :param area:
        :return:
        """
        import math
        l = math.sqrt(area)
        l = round(l)
        if l*l == area:
            return [l,l]
        else:
            r = round(area / l)
            while not r * l == area:
                l += 1
                r = round(area / l)
            return [l,r] if l >= r else [r,l]