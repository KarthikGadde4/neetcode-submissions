class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        counts = Counter(nums)

        topKFreq = [item[0] for item in counts.most_common(k)]
        return topKFreq
