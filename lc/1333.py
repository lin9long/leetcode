from typing import List

class Solution:
    """
    餐厅过滤器
    """
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        import heapq
        tmplist = restaurants
        if veganFriendly == 1 :
            tmplist = filter(lambda x : x[2]==1,restaurants)
            # tmplist = list(tmplist)
        tmplist = filter(lambda x : x[3]<=maxPrice,tmplist)
        tmplist = filter(lambda x : x[4]<=maxDistance,tmplist)
        tmplist = sorted(tmplist,key=lambda x:[x[1],x[0]],reverse=True)
        return [i[0] for i in tmplist]