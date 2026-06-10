class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #seen = set()
        #for i in range(len(nums)):
        #    seen.add(nums[i])
        seen = set(nums)

        
        
        longestSeq = 0
        for num in seen:
            if((num - 1) not in seen):
                currSeq = 1
                while(num + 1) in seen:
                    currSeq += 1
                    num += 1
                #if(currSeq > longestSeq):
                    #longestSeq = currSeq
                longestSeq = max(currSeq, longestSeq)
            #else: **#if((num - 1) in seen)**
                #continue
        return longestSeq