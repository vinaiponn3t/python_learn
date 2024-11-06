class TreeNode:
   
    def __init__(self,data):
        self.data = data
        #print childทุกตัวใน level เดียวกัน
        self.children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self 
        self.children.append(child)
        
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#         return level      
        
#     def print_tree(self):
#         space = " " * self.get_level()*3
#         prefix = space+ "|__" if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 # for a in self.children:
#                 child.print_tree()
        
# def build_product_tree():
#     root=TreeNode('Electronics')
    
#     laptop = TreeNode('Laptop')
#     laptop.add_child(TreeNode('Mac'))
#     laptop.add_child(TreeNode('Surface'))
#     laptop.add_child(TreeNode('Thinkpad'))
    
    
    
#     cellphone = TreeNode('Cell Phone')
#     cellphone.add_child(TreeNode('iPhone'))
   
    
#     cellphone.add_child(TreeNode('GooGle Pixel'))
#     cellphone.add_child(TreeNode('Vivo'))
    
    
    
#     tv = TreeNode('TV')
#     tv.add_child(TreeNode('SamSong'))
#     tv.add_child(TreeNode('LG'))
    
    
#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)
    
#     iphone = TreeNode('iPhone')
#     iphone.add_child(TreeNode('iphone15'))
#     return root
    
# if __name__ == '__main__':
#     root=build_product_tree()  
#     #print(root.get_level())
#     root.print_tree()
#     pass    
root = TreeNode("sport")
print(root.data)   
f = TreeNode('football')
f.add_child(TreeNode('vvvv'))
print()   
print()   
print(dir(f.children))

print()
print()
print(f.children.__doc__)
print(f.children is None)
print(root.children)       
print(root.parent)       
#print(root.add_child(['football','vallayball','running']))       
root.add_child(TreeNode('football'))  
print(root.data)    
print(f.children)