# kembalikan nilai True kalo x adalah palindrome, dan sebaliknya
# brarti harus samain dari kiri ke kanan

class Solution(object):
    def isPalindrome(self,x):
        string = str(x) # ini jadinya "123"
        y = len(string)-1
        # print(kanan)
        for indeks, i in enumerate(string):
            # print(f'{i} ini indeks ke-{indeks}')
            kanan = string [y - indeks] # [2-0] = berati indeks ke 2
                                        # [2-1] = 1
                                        # [2-2 ] = 0
            # print(i,kanan)
            if i != kanan:
                return False
            
        return True

solution1 = Solution()
print(solution1.isPalindrome(121))