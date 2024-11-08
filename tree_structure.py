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
    root = TreeNode("Health food")
    
    breakfast = TreeNode("Breakfast")
    lunch = TreeNode("Lunch")
    dinner = TreeNode("Dinner")
   
    fried_rice = TreeNode("Fried_Rice")
    beep_soup = TreeNode("Beep Soup")
    
    steak = TreeNode("Steak")
    salad = TreeNode("Salad")
    
    breakfast.add_child(steak)
    lunch.add_child(fried_rice)
    lunch.add_child(beep_soup)
    dinner.add_child(salad)
    
    
    
    greeksalad = TreeNode("Greek Salad")
    caesarsalad = TreeNode("Caesar Salad")
    cobbsalad = TreeNode("Cobb Salad")
    
    salad.add_child(greeksalad)
    salad.add_child(caesarsalad)
    salad.add_child(cobbsalad)
    
    root.add_child(breakfast)
    root.add_child(lunch)
    root.add_child(dinner)
    
    # print(ronaldo_7.get_level())
    # print(manchester_united.get_level())
    # print(football.get_level())
    return root
    
if __name__ == '__main__':
    root = build_product_tree()
    #print(root.get_level())
    root.print_tree()
    pass