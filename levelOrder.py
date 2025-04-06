    def levelOrder(self, root):
        queue = []
        node = root
        while(node.left or node.right):
            queue.append(node.data)
            node = node.left if node.left else node.right
            
        if max_height < height:
            max_height = height
            
        height = 0
        tree = root
        while(tree.left or tree.right):
            tree = tree.right if tree.right else tree.left
            height += 1
                
        if max_height < height:
            max_height = height
            
        return max_height