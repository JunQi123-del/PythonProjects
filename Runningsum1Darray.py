"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""


def runningSum(self, nums):
        returnList = []
        sumOfNumber = 0
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1): #check for inclusive value of start
                sumOfNumber+=nums[j]
            returnList.append(sumOfNumber)
            sumOfNumber=0
        return returnList

#or 

def runningSum1(self, nums):
        result = []
        sum = 0
        for i in nums:
            sum+=i
            result.append(sum)
        return result