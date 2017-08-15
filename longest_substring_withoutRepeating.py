class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, longestnum, visited=0, 0, [False for _ in range(128)]
        for i in range(len(s)):
            if visited[ord(s[i])]:
                while s[i] != s[start]:
                    #visited[ord(s[i])]=False #bug
                    visited[ord(s[start])]=False
                    start += 1
                start += 1
            else:
                visited[ord(s[i])]=True
                
            longestnum=max(longestnum, i-start+1) # save the longestnum all the time, so it is ok to set visited[] to False above
            #suppose we discard the before substrings, but we keep their longest number, if we come across it later again, we regard it as unvisited, because we have already set it to be unvisited, so we can capture it into our new substring as valid one
            
        return longestnum
        
if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("pwwpkew")
    
    ### substring is a continous one, subsequence can skip, is discontinous
