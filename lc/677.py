class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.k_v = {}

    def insert(self, key: str, val: int) -> None:
        self.k_v[key] = val

    def sum(self, prefix: str) -> int:
        def kmp(mom_string, son_string):
            # 传入一个母串和一个子串
            # 返回子串匹配上的第一个位置，若没有匹配上返回-1
            test = ''
            if type(mom_string) != type(test) or type(son_string) != type(test):
                return -1
            if len(son_string) == 0:
                return 0
            if len(mom_string) == 0:
                return -1
            # 求next数组
            next = [-1] * len(son_string)
            if len(son_string) > 1:  # 这里加if是怕列表越界
                next[1] = 0
                i, j = 1, 0
                while i < len(son_string) - 1:  # 这里一定要-1，不然会像例子中出现next[8]会越界的
                    if j == -1 or son_string[i] == son_string[j]:
                        i += 1
                        j += 1
                        next[i] = j
                    else:
                        j = next[j]

            # kmp框架
            m = s = 0  # 母指针和子指针初始化为0
            while (s < len(son_string) and m < len(mom_string)):
                # 匹配成功,或者遍历完母串匹配失败退出
                if s == -1 or mom_string[m] == son_string[s]:
                    m += 1
                    s += 1
                else:
                    s = next[s]

            if s == len(son_string):  # 匹配成功
                return m - s
            return -1
            # 匹配失败

        count = 0
        for k, v in self.k_v.items():
            # print(k,v,prefix,kmp(k,prefix))
            if kmp(k, prefix) == -1:
                continue
            elif kmp(k, prefix) == 0:
                count += v
                # print(k,v,prefix,kmp(k,prefix),count)
        return count

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)