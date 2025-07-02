class TreeNode: 
    # A class that represents a tree node. 
    # You can build a tree from this one class. 
    def __init__(self, value=None): 
        self._value = value  # The name of the person
        self.children = []
        self.parent = None 
        self.level = 0 
 
    def add_child(self, child_node): 
        child_node.parent = self 
        child_node.level = child_node.parent.level + 1 
        self.children.append(child_node) 
         
    def get_child(self, value): 
        for child in self.children: 
            if child.value == value: 
                return child 
         
        return None 
     
    def get_parent(self): 
        return self.parent 
 
    def remove_child(self, child_node): 
        self.children = [child for child in self.children if child is not 
child_node] 
 
    @property 
    def value(self): 
        return self._value 
 
    @value.setter 
    def value(self, value): 
        self._value = value 
 
    def get_parent(self): 
        return self.parent 
 
    def get_level(self): 
        return self.level 
 
    def is_leaf(self): 
        if self.children: 
            return False 
        else: 
            return True 
         
    def get_list_of_children(self): 
        message = "" 
        if self.children: 
            message += f"{self.value}'s children are: " 
            for child in self.children: 
                message += str(child.value) + ", " 
                 
        else: 
            message = f"{self.value} has no children" 
             
        return message 
                 
 
    def traverse(self): 
        # moves through each node referenced from self downwards 
        print(self._value) 
 
        for child in self.children: 
            child.traverse() 
             
    def __str__(self, level=0): 
        # return a string representation of the tree beginning 
        # with the current node. 
        ret = "\t"*level + repr(self.value) + '\n' 
        for child in self.children: 
            ret += child.__str__(level+1) 
         
        return ret 
 
### Main Program  
 
node = TreeNode("Adam") 
node.add_child(TreeNode("Cain")) 
node.add_child(TreeNode("Abel")) 
node.add_child(TreeNode("Seth")) 
 
node = node.get_child("Cain") 
node.add_child(TreeNode("Enoch")) 
node = node.get_parent() 
node = node.get_child("Seth") 
node.add_child(TreeNode("Enosh")) 
node = node.get_parent() 
 
print(node.__str__())
