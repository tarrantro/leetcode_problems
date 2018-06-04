class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        b = []
        if root:
            a = [root]
            c = []
            while a:
                
                com_val = a[0].val
                for i in a:
                    
                    if i.val > com_val:
                        com_val = i.val
                    c.append(i.left)
                    c.append(i.right)
                    
                b.append(com_val)    
                a = [x for x in c if x]
                c = []
            
        return b
