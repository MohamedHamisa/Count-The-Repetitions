class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        dp = []
        for i in range(len(s2)):
            start = i
            cnt = 0
            for j in range(len(s1)):
                if s1[j] == s2[start]:
                    start += 1
                    if start == len(s2):
                        start = 0
                        cnt += 1
            dp.append((start,cnt))
        res = 0
        next = 0
        for _ in range(n1):
            res += dp[next][1]
            next = dp[next][0]
        return res // n2
		
    



