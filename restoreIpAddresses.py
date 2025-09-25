
#93. Restore IP Addresses
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        if len(s) > 12:
            return res

        def backtrack(i,dots,currIP):
            if dots == 4 and i == len(s):
                res.append(currIP[:-1])
                return
            if dots > 4:
                return

