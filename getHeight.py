    def getHeight(self,root):
        #Write your code here
        height = 0
        max_height = 0
        tree = root
        while(tree.left or tree.right):
            tree = tree.left if tree.left else tree.right
            height += 1
            
        max_height = height
        height = 0
        
        tree = root
        while(tree.left or tree.right):
            tree = tree.right if tree.right else tree.left
            height += 1
                
            
        if max_height < height:
            max_height = height
            print("Max height: ", max_height)
            
        return max_height