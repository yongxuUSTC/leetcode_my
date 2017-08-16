class Solution_Generic(object):
    
    def mergeFindMedian(self, nums1,nums2):
        nums3=[]
        
        i=0
        j=0
        ### merge method
        while(i<len(nums1) and j < len(nums2)):
            if (nums1[i] <= nums2[j]):
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1

        while(i<len(nums1)):
            nums3.append(nums1[i])  
            i += 1

        while(j<len(nums2)):
            nums3.append(nums2[j])
            j +=  1
        
        if (len(nums3)%2==1):
            return nums3[len(nums3)//2]     ### odd: median is //2
        else:
            return (nums3[len(nums3)//2-1]+nums3[len(nums3)//2])*0.5 ###even, median is //2-1 ave //2 
            ### *0.5  ,not /2 (will be an int)
            
            ### array means just a list, not a matrix
