class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        a = list(map(lambda x,y:x-y,gas,cost))
        if sum(a) < 0:
            return -1
        else:
            total = 0
            j = 0
            index = 0
            for i in range(len(a)):
                
                j = a[i] +j
                if j >=0:
                    continue
                else:
                    total = total+j
                    j = 0
                    index = i+1
                                          
            return index
            
        
        
        
