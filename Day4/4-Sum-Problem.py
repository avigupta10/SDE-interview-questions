class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end = 0, 0
        res = 0
        st = set()
        while end < len(s):
            if s[end] not in st:
                st.add(s[end])
                end += 1
                res = max(res, len(st))
            else:
                st.remove(s[start])
                start += 1
        return res
