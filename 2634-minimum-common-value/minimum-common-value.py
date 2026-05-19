class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = list((Counter(nums1) & Counter(nums2)).elements())

        if not common:
            return -1

        return min(common)