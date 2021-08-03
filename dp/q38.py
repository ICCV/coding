class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(1,n):
            new_res = ''
            a = res[0]
            acnt = 0
            k=0
            while k<len(res):
                if k == len(res)-1:
                    if res[k] == a:
                        acnt += 1
                        new_res = new_res + str(acnt) + str(a)
                    else:
                        new_res = new_res + str(acnt) + str(a)+'1'+str(res[k])
                else:
                    if res[k] != a:
                        new_res = new_res + str(acnt) + str(a)
                        a = res[k]
                        acnt = 0
                    acnt += 1
                k += 1
            res = new_res
        return res



if __name__ == '__main__':
    n = 4
    s = Solution()
    print(s.countAndSay(n))