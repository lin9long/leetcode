def maxArea(self, height: List[int]) -> int:
    """
    盛最多水的容器
    :param self:
    :param height:
    :return:
    """
    p_l = 0
    p_r = len(height) - 1
    l = len(height) - 1
    area = 0
    while p_l < p_r:
        l_h = height[p_l]
        r_h = height[p_r]
        if l_h > r_h:
            area = max(area, r_h * l)
            p_r -= 1
        else:
            area = max(area, l_h * l)
            p_l += 1
        l -= 1
    return area