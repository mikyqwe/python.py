"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."""
class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		for i in range(0,len(nums)):
			for j in range(i+1,len(nums)):
				if nums[i]+nums[j] == target:
					return [i,j]
		