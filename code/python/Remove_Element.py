class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result=[]
        for i in range(len(nums)):
            if(val==nums[i]):
                result.append(val)
                #print(result)
        for j in range(len(result)):
            print(result[j])
            nums.remove(result[j])
        return len(nums)