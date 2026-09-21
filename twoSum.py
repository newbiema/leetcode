class Solution(object):
    def twoSum(self,nums,target):
        for indeks_i,isi_i in enumerate(nums):
            for indeks_j,isi_j in enumerate(nums):
                hasil = isi_i + isi_j
                if hasil == target and indeks_i != indeks_j:
                    return [indeks_i,indeks_j]
                    
        
solution1 = Solution()
solution2 = Solution()
solution3 = Solution()
print(solution1.twoSum([2,7,11,15],9))
print(solution2.twoSum([3,2,4],6))
print(solution3.twoSum([3,3],6))
    
     
    