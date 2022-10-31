class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=[] #result array , stores eveery subset's xor
        a=0 #stores subset's xor
        make(nums,a,0,ans) #function call for recursion or backtracking
        return sum(ans) #final answer after updation of result array
              
def make(nums,a,i,ans): 
    if i==len(nums): #if the index reaches to end of nums, 
        ans.append(a) #time to store the xor formed of subset
        return #return back to the called function
    make(nums,a,i+1,ans) #when the element need not to include in subset(no xor) and i+1 is for next element 
	#will backtrack
    make(nums,a^nums[i],i+1,ans) #when the element is included
