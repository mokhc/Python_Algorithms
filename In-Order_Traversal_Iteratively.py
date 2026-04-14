# Test - In-Order Traversal Iteratively (left parent right ... root ... left parent right)
# Set the in-order traversal values of a binary tree
# @mokhc
# 05/04/26
from collections import deque
from print_btree import print_btree

# class BNode
class BNode():
	def __init__(self, v, left="", right=""):
		self.val = v
		self.left = left
		self.right = right

class Tra():
	def in_tra1(self, input: BNode):
		"""
		:param input: input
		:type input: BNode
		:return: res1
		:rtype: list
		"""
		# base
		if type(input) == None:
			return []
		cur1 = input
		res1 = []
		stack1 = []  #
		# loop to get values into the return list
		while len(stack1) > 0 or cur1:
			while cur1:
				stack1.append(cur1)
				cur1 = cur1.right
			temp = stack1.pop()
			res1.insert(0, temp.val)
			cur1 = temp.left
		return res1
	
	def in_tra2(self, input: BNode):
		"""
		:param input: input
		:type input: BNode
		:return: res1
		:rtype: list
		"""
		# base
		if type(input) != BNode:
			return []
		cur1 = input
		res1 = []
		stack1 = deque(list())
		# loop to get values into the return list
		while len(stack1) > 0 or cur1:
			while cur1:
				stack1.append(cur1)
				cur1 = cur1.left
			temp = stack1.pop()
			res1.append(temp.val)
			cur1 = temp.right
		return res1

# implementation 1
t1 = BNode(1)
t1.left = BNode(2)
t1.right = BNode(3)
t1.left.left = BNode(4)
t1.left.right = BNode(5)
t1.right.left = BNode(6)
print_btree(t1)
"""
 ___1___
 |     |
_2_   _3
| |   |
4 5   6
"""

print("----- 1 -----")  # [4, 2, 5, 1, 6, 3]
s1 = Tra()
print(s1.in_tra1(t1))
print("----- 2 -----")
s2 = Tra()
print(s2.in_tra2(t1))

# reference:
# https://github.com/liyin2015/python-coding-interview/blob/master/Colab_Codes/chapter_tree_data_structure_and_traversal.ipynb
