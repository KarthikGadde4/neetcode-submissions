class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        arr = [[] for _ in range(len(nums) + 1)]

        for key in freq:
            count = freq[key]
            arr[count].append(key)
        
        result = []
        for i in range(len(arr) - 1, 0, -1):
            for j in range(len(arr[i])):
                result.append(arr[i][j])
                if(len(result) == k):
                    return result
                

        






        
