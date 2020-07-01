
from typing import List

class Solution:
    """
    单词拆分、动态规划
    """
    def wordBreak(self, s: str, c: List[str]) -> bool:

        # for i in range(len(wordDict)):
        #     replace_list = []
        #     s_c = ''
        #     target = wordDict[i]
        #     tmp_s = s.replace(target,'&')
        #     if tmp_s == s :
        #         continue
        #     else:
        #         replace_list.append(target)
        #         for j in range(i,len(wordDict)):
        #             tmp_s = tmp_s.replace(wordDict[j],'&')
        #             if not tmp_s.replace('&','') :
        #                 return True
        # return  False
        tar_list = [False] * (len(s) + 1)
        tar_list[0] = True
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if tar_list[i] and s[i:j] in c:
                    tar_list[j] = True
        return tar_list[-1]