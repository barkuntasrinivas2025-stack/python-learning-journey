class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # i=0
        # j=i+1
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                # val = (nums[i]+nums[j])
                if(nums[i]+nums[j] == target):
                    return [i,j]
                # else: ret
if __name__ == "__main__":
    # 1. Create sample test data
    test_nums = [2, 7, 11, 15]
    test_target = 9
    
    # 2. Instantiate the Solution class
    solution = Solution()
    
    # 3. Call the function and catch the returned array
    result = solution.twoSum(test_nums, test_target)
    
    # 4. Print the output to your VS Code terminal
    print(f"Indices found: {result}")
        