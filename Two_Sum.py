from collections import defaultdict


class Solution:
    
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        Trivial algorithm: Too slow.
        """
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i != j and n1 + n2 == target:
                    return [i, j]
        
    def twoSum2(self, nums, target: int):
        """
        Still really slow...
        Reduces the length of the array. But still O(n**2) on the sub-list
        """
        asc = sorted(enumerate(nums), key=lambda x: x[1])
        max_num = asc[-1][1]
        min_val = target - max_num  # only consider numbers above this value
        
        asc_sub = [x for x in asc if x[1] >= min_val]
        print(asc_sub)
        
        for i, n1 in asc_sub:
            for j, n2 in asc_sub:
                if i != j and n1 + n2 == target:
                    return [i, j]

    def twoSum3(self, nums, target):
        """
        Hashtable solution: O(n)
        Mind: The same number can occur multiple times => list of indices
        """
        value2indices = defaultdict(list)
        for i, number in enumerate(nums):
            value2indices[number].append(i)
                    
        for number, indices in value2indices.items():
            
            i = indices[0]
            complement = target - number
            
            if complement in value2indices.keys():
                for j in value2indices[complement]:
                    if i != j:
                        return [i, j]
                    
    def twoSum(self, nums, target):
        """
        Hashtable solution - only one pass: O(n)
        """
        value2index = {}
        
        for i, number in enumerate(nums):
            
            complement = target - number
            if complement in value2index.keys():
                
                return [value2index[complement], i]
                    
            value2index[number] = i