class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p :
            level += 1
            p = p.parent  
        return level
          
    def print_tree(self):
        space = ' ' * self.get_level() * 3
        prefix = space + "|--"if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
        
def build_product_tree():
    root = TreeNode("Sports")
    
    football = TreeNode("Football")
   
    manchester_united = TreeNode("ManChester_United")
    
    ronaldo_7 = TreeNode("RONALDO_7")
    manchester_united.add_child(ronaldo_7)
    football.add_child(manchester_united)
    root.add_child(football)
    
    # print(ronaldo_7.get_level())
    # print(manchester_united.get_level())
    # print(football.get_level())
    return root
    
if __name__ == '__main__':
    root = build_product_tree()
    #print(root.get_level())
    root.print_tree()
    pass