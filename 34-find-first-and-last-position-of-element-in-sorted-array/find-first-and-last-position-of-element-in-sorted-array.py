class Solution:
    def first_position(self, nums, target, n):
        result = -1
        start, end = 0, n
        
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                result = mid
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return result
    
    def last_position(self, nums, target, n):
        result = -1
        start, end = 0, n
        
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                result = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return result
    
    def searchRange(self, nums, target):
        n = len(nums) - 1
        fp = self.first_position(nums, target, n)
        lp = self.last_position(nums, target, n)
        return [fp, lp]