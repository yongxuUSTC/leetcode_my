class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ###method1:
        #nums3=[]
        #i=0
        #j=0
        #while(i<len(nums1) and j < len(nums2)):
        #    if (nums1[i] <= nums2[j]):
        #        nums3.append(nums1[i])
        #        i += 1
        #    else:
        #        nums3.append(nums2[j])
        #        j += 1
        #
        #while(i<len(nums1)):
        #    nums3.append(nums1[i])  
        #    i += 1
        #
        #while(j<len(nums2)):
        #    nums3.append(nums2[j])
        #    j +=  1
        # 
        #if (len(nums3)%2==1):
        #    return nums3[len(nums3)//2]
        #else:
        #    return (nums3[len(nums3)//2-1]+nums3[len(nums3)//2])*0.5
        
        #######################################################################################################################
        ###method2:
                #to search the average median in a binary search method, as it asks for log(m+n), for log(m+n): binary search or binary search tree
        #idea: to find the i-th and j-th element in the begining of the right half in the merged n+m array, so if i, then j=half-j, half=(n+m)/2
        m=len(nums1) # assume shorter one, or swap it
        n=len(nums2) # assume longer one, or swap it
        
        if m >n:
            nums1, nums2, n, m =nums2, nums1, m, n
        
        #special cases:
        if m==0 and n != 0: # one of them is empty
            if n%2==1:
                return nums2[n//2]
            else:
                return (nums2[n//2-1] + nums2[n//2])*0.5
        elif m==0 and n==0: # both of them are empty
            return None 
            
        #half=(n+m)/2 ### or (m+n+1)//2 ???  ###bug
        half=(n+m+1)/2
        #i=m//2 #the index in n for the 1st or 2nd index in the whole sorted right half
        #j=half-i # the index in m for the 1st or 2nd index in the whole sorted right half 
        iMin=0 # only traverse on the m array, so the j in n array can be decided as above, so the time complexity is log(m)
        iMax=m 
        while iMin <= iMax:
            i=(iMin+iMax)//2
            j=half-i
            if i<m and nums2[j-1] > nums1[i]:  ### [0, j-1] should be all smaller than i, i and j is not comparable, i is too small
                iMin=i+1
            elif i>0 and nums1[i-1] > nums2[j]: ### [0, i-1] should be all smaller than j, i and j is not comparable, i is too large
                iMax=i-1
            else:
                if i==0:  ## all i is larger than all j
                    maxleft=nums2[j-1]   ### i==0. so j=half-0=half
                elif j==0: # i=half-0=half=(n+m)/2, 
                    maxleft=nums1[i-1]
                else: ### nums2[j-1] < nums1[i] or nums1[i-1] < nums2[j], i and j in the middle
                    maxleft=max(nums2[j-1], nums1[i-1])
            
                if i==m:
                    minright=nums2[j]
                elif j == n:
                    minright=nums1[i]
                else:
                    minright=min(nums1[i],nums2[j])
                
                if (m+n)%2 == 0:
                    return (minright+maxleft)*0.5
                else:
                    return maxleft
