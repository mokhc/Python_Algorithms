# Test - Post-Order Traversal Iteratively (left right parent ... left right parent ... root)
# Set the post-order traversal values of a binary tree
# @mokhc
# 13/04/26 (6)
from collections import deque
from print_btree import print_btree

# class BNode
class BNode():
	def __init__(self, v, left="", right=""):
		self.val = v
		self.left = left
		self.right = right

class Tra():
	def post_tra2(self, input: BNode):
		"""
		:param input: input
		:type input: BNode
		:return: res1
		:rtype: list

		# key concept - using pop or popleft()
		and setting the order in which the node value(s) are inserted into the return list
		and using if conditions and append() or insert() to set the order in which the node(s)
		are inserted into the deque or stack
		"""
		if type(input) is None:
			return []
		res1 = []
		stack1 = deque([input])  # [input]
		while len(stack1) - 0 > 0:
			tmp1 = stack1.popleft()
			res1.insert(0, tmp1.val)
			if tmp1.left:
				stack1.insert(0, tmp1.left)
			if tmp1.right:
				stack1.insert(0, tmp1.right)
		return res1
	
	def post_tra1(self, input: BNode):
		"""
		:param input: input
		:type input: BNode
		:return: res1
		:rtype: list

		# key concept - using pop or popleft()
		and setting the order in which the node value(s) are inserted into the return list
		and using if conditions and append() or insert() to set the order in which the node(s)
		are inserted into the deque or stack
		"""
		if type(input) is not BNode:
			return []
		res1 = []
		stack1 = [input]  # [input]
		while len(stack1) > 0:
			tmp1 = stack1.pop(len(stack1)-1)
			res1.insert(0, tmp1.val)
			if tmp1.left:
				stack1.insert(len(res1), tmp1.left)
			if tmp1.right:
				stack1.insert(len(res1), tmp1.right)
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

print("----- 1 -----")
s1 = Tra()
print(s1.post_tra1(t1))
print("----- 2 -----")
s2 = Tra()
print(s2.post_tra2(t1))  # 4 5 2 6 3 1


# reference:
# https://github.com/liyin2015/python-coding-interview/blob/master/Colab_Codes/chapter_tree_data_structure_and_traversal.ipynb