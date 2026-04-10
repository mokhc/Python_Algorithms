# Test - Level Order Traversal Iteratively
# Set the level order traversal values of a binary tree
# @mokhc
# 31/03/26
from collections import deque

# binary tree node.
class BNode():
    def __init__(self, v, l='', r=''):
        self.val = v
        self.left = l
        self.right = r

class Level_Order:
    # function 1
    def LevelOrder1(self, r) -> list:
        # base
        if type(r) != BNode:
            return
        same_level = list([r])
        temp = []
        tempret = []
        ret = []
        # loop to set value(s) level by level
        while len(same_level) > 0:
            for v in same_level:
                tempret.append(v.val)
                if v.left:
                    temp.append(v.left)
                if v.right:
                    temp.append(v.right)
            ret.append(tempret)
            tempret = []
            same_level = temp
            temp = []
        return ret
    
    # function 2
    def LevelOrder2(self, r) -> list:
        # base
        if type(r) is None:
            return
        same_level = deque([r])
        temp = []
        tempret = []
        ret = []
        # loop to set value(s) level by level
        while same_level:
            for v in reversed(same_level):
                tempret.append(v.val)
                if v.left:
                    temp.insert(0, v.left)
                if v.right:
                    temp.insert(0, v.right)
            ret.insert(len(ret), tempret)
            tempret = []
            same_level = temp
            temp = []
        return ret

# implementation 1
t1 = BNode(1)
t1.left = BNode(2, BNode(4, BNode(8)), BNode(5))
t1.right = BNode(3, BNode(6))

s1 = Level_Order()
print(s1.LevelOrder1(t1)) # [[1], [2, 3], [4, 5, 6], [8]]

# reference:
# https://github.com/liyin2015/python-coding-interview/blob/master/Colab_Codes/chapter_tree_data_structure_and_traversal.ipynb
    
