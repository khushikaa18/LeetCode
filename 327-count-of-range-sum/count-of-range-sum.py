class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        def merge_sort(left,right):
            if right-left<=1:
                return 0
            mid=(left+right)//2

            count=merge_sort(left,mid)+merge_sort(mid,right)

            j=k=mid
            for i in range(left, mid):
                
                # find lower bound
                while k < right and prefix[k] - prefix[i] < lower:
                    k += 1
                
                # find upper bound
                while j < right and prefix[j] - prefix[i] <= upper:
                    j += 1
                
                count += (j - k)
            temp = []
            l, r = left, mid
            
            while l < mid and r < right:
                if prefix[l] <= prefix[r]:
                    temp.append(prefix[l])
                    l += 1
                else:
                    temp.append(prefix[r])
                    r += 1
            temp.extend(prefix[l:mid])
            temp.extend(prefix[r:right])
            prefix[left:right] = temp
            return count
        return merge_sort(0,len(prefix))

        