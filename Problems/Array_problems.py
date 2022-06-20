
###https://leetcode.com/problems/rotate-array/
#Rotate Array

#Rotate an array of n elements to the right by k steps.

#For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#How many different ways do you know to solve this problem?


def rotate_array(n,k) -> [] :
    res=[i+1 for i in range(n)]
    print(res)
    for _ in range(k+1):
        res=res[1:]+[res[0]]
    return res
#print(rotate_array(7,3))
class Solution:
    def __init__(self,nums) -> None:
        self.nums=nums
    def rotate(self, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        n=len(self.nums)-1
        for _ in range(k):
            self.nums=[self.nums[-1]]+self.nums[0:n]
    def get(self):
        print(self.nums)

p=Solution([1, 2, 3, 4, 5, 6, 7])
p.rotate(3)
p.get()


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        k=k%(len(nums))
        l,r=0,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l,r=0,k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l,r=k,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1       

#Problem 2 
#Given s = "the sky is blue",
#return "blue is sky the".

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r=0,len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        l,r=0,0
        for i,v in enumerate(s):
            if v==" ":
                r=i-1
                while l<r:
                    s[l],s[r]=s[r],s[l]
                    l+=1
                    r-=1
                l=i+1
        r=len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1


##https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        r=0
        for i in tokens:
            #print(s)
            if i not in ["+","/","-","*"] : s.append(int(i))
            else: 
                t=s.pop()
                l=s.pop()
                if i == "+" : s.append(l+t)
                if i == "/" : s.append(int(l/t))
                if i == "*" : s.append(l*t)
                if i == "-" : s.append(l-t)
        return s.pop()

##https://leetcode.com/problems/implement-strstr/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1
    
    
##https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.s=[]
        self.size =0
        self.min=math.inf
    def push(self, val: int) -> None:
        self.s.append(val)
        self.size +=1
        self.min=min(self.min,val)
        
    def pop(self) -> None:
        t=self.s[self.size-1]
        self.s.pop()
        self.size -=1
        if self.size >= 1: 
            if self.min == t : self.min=min(self.s)
        if self.size==0: self.min=math.inf

    def top(self) -> int:
        return self.s[self.size-1]
    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


#https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        c={}
        d={}
        
        for c1, c2 in zip(s, t):
            
            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in c) and (c2 not in d):
                c[c1] = c2
                d[c2] = c1
            
            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both            
            elif c.get(c1) != c2 or d.get(c2) != c1:
                return False
            print(c1,c2,c[c1],d[c2])
        return True
#https://leetcode.com/problems/median-of-two-sorted-arrays/

#Time complexity O(nlogn)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            for x in nums1:
                nums2.append(x)
            nums1 = sorted(nums2)
            c = len(nums1)
            return (nums1[int(c/2)] + nums1[int((c/2)) - 1])/2 if c % 2 == 0 else nums1[int((c-1)/2)]
        else:
            for x in nums2:
                nums1.append(x)
            nums2 = sorted(nums1)
            c = len(nums2)
            return (nums2[int(c/2)] + nums2[int((c/2)) - 1])/2 if c % 2 == 0 else nums2[int((c-1)/2)]
