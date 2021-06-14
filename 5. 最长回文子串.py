class Solution(object):
    def longestPalindrome(self, s):
        """
        1. 外层for循环便利string
        2. 内层以当前字符作为核心,向两遍(begin-1, end+1)拓展回文子串长度
        3. 注意核心有两种情况,单字符核心("a")与双字符核心("bb")
        """
        len_s = len(s)

        def could_longer(begin, end):
            if (begin - 1) < 0 or (end + 1) >= len_s:
                return begin, end, end - begin + 1

            if s[begin - 1] == s[end + 1]:
                begin -= 1
                end += 1
                return could_longer(begin, end)
            else:
                return begin, end, end - begin + 1

        best_begin = 0
        best_end = 0
        best_length = 1
        for idx in range(len_s - 1):  # 最后一个字符,最长也就1
            begin = idx

            if s[begin] == s[begin + 1]:  # 可单字符核心,也可双字符核心的情况
                begin_1, end_1, length_1 = could_longer(begin, begin)
                begin_2, end_2, length_2 = could_longer(begin, begin + 1)

                if length_1 >= length_2:
                    begin, end, length = begin_1, end_1, length_1
                else:
                    begin, end, length = begin_2, end_2, length_2
            else:  # 普通情况
                begin, end, length = could_longer(begin, begin)

            if length > best_length:
                best_begin, best_end, best_length = begin, end, length

        return s[best_begin:best_end + 1]


    def longestPalindrome_version_2(self, s):
        """
        优化上述中心法
        1. 递归形式的拓展判定改成循环的方式
        2. 合并了单核心与双核心的 代码
        2. 精简了一些变量
        """
        len_s = len(s)

        def longest(begin, end):
            while (begin >= 0) and (end < len_s) and (s[begin] == s[end]):
                begin -= 1
                end += 1
            return begin + 1, end - 1

        best_begin = 0
        best_end = 0
        for idx in range(len_s - 1):  # 最后一个字符,最长也就1

            begin_1, end_1 = longest(idx, idx)  # 单字符核心
            begin_2, end_2 = longest(idx, idx + 1)  # 双字符核心

            if (end_1 - begin_1) >= (end_2 - begin_2):
                begin, end = begin_1, end_1
            else:
                begin, end = begin_2, end_2

            if (end - begin) > (best_end - best_begin):
                best_begin, best_end = begin, end

        return s[best_begin:best_end + 1]


    def longestPalindrome_version_3(self, s):
        """
        abcdedcba
        考虑上述回文子串
        在向右遍历的过程中, 考虑s[0:i+1]
        假设在i时,s[0:i+1]出现了更长的回文子串,那么i一定是结尾,且长度+1或+2
        因为跨过回文子串中心之前,maxlen不会变, 跨过之后,没跨过1个增加1或2
        """
        start = 0
        maxlen = 1
        for i in range(1, len(s)):  # 字符串长度至少等于3
            odevity_c = s[i - maxlen: i + 1]  # 奇偶性改变的情况, 长度加1 change
            if odevity_c == odevity_c[::-1]:
                start = i - maxlen
                maxlen += 1

            if (i-maxlen-1) >= 0:  # 有肯能i-1更新了max_len, i就不能更新了
                odevity_e = s[i - maxlen - 1: i + 1]  # 奇偶性不变的情况, 长度加2 equal

                if odevity_e == odevity_e[::-1]:
                    start = i - maxlen - 1
                    maxlen += 2

        return s[start: start + maxlen]


if __name__ == '__main__':

    test_cases = ["babad"]
    for test in test_cases:
        print(Solution().longestPalindrome_version_3(test))

