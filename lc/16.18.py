class Solution:
    """
    匹配模式，通过pattern匹配value模式
    """
    def patternMatching(self, pattern: str, value: str) -> bool:
        if not pattern:
            return not value
        a_cnt, b_cnt = pattern.count('a'), pattern.count('b')
        for a_l in range(1 if a_cnt == 0 else (len(value) // a_cnt + 1)):
            lens, strs, i = [a_l, 0], [None, None], 0
            if not b_cnt:
                if len(value) != a_l * a_cnt:
                    continue
            else:
                if (len(value) - a_cnt * a_l) % b_cnt != 0:
                    continue
                lens[1] = (len(value) - a_cnt * a_l) // b_cnt
            for p in pattern:
                if strs[ord(p) - 97] is not None and strs[ord(p) - 97] != value[i:(i + lens[ord(p) - 97])]:
                    break
                strs[ord(p) - 97] = value[i:(i + lens[ord(p) - 97])]
                i += lens[ord(p) - 97]
            else:
                if strs[0] != strs[1]:
                    return True
        return False
