    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in hash:
                return [i,hash[y]]
            else: 
                hash[x] = i
                
