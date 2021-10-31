# User function Template for python3

class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # code here
        st, en = -1, -2
        prev = -1
        ans = 0
        v = []
        for i in range(n):
            v.append([start[i], end[i]])

        v.sort(key=lambda x: x[1])

        for s, e in v:
            if prev < s:
                if s > st:
                    st = s
                if en < e:
                    en = e
                    prev = en
                ans += 1
        return ans