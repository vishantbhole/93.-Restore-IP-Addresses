
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
