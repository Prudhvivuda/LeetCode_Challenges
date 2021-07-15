Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
--------------------------------------------------

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        ln = len(nums)
        for i in range(ln-1, 1, -1):
            c = nums[i]
            start = 0
            end = i-1
            while start < end:
                if nums[start] + nums[end] > c:
                    ans += end - start
                    end -= 1
                elif nums[start] + nums[end] <= c:
                    start += 1
        return ans
