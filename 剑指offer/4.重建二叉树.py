# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 21:38
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 4 重建二叉树.py
# @Software: PyCharm

'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

'''
利用二叉树前序遍历和中序遍历的特性。前序遍历的第一个值一定为根节点，对应于中序遍历中间的一个点。
在中序遍历序列中，这个点左侧的均为根的左子树，这个点右侧的均为根的右子树。
这时可以利用递归，分别取前序遍历[1:i+1]和中序遍历的[:i]对应与左子树继续上一个过程，
取前序遍历[i+1:]和中序遍历[i+1]对应于右子树继续上一个过程，最终得以重建二叉树。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        '''
        # 返回构造的TreeNode根节点
        :param pre: 前序
        :param tin: 中序
        :return:    根节点
        '''
        # write code here
        if not pre and not tin:
            return None
        root = TreeNode(pre[0])
        if set(pre) != set(tin):
            return None
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1: i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root

    def reConstructBinaryTree1(self, tin, post):
        '''
        返回构造 TreeNode 根节点
        :param tin:  中序
        :param post: 后序
        :return:     根节点
        '''
        if not tin and not post:
            return None
        root = TreeNode(post[-1])
        if set(tin) != set(post):
            return None
        i = tin.index(post[-1])
        root.left = self.reConstructBinaryTree1(tin[:i], post[:i])
        root.right = self.reConstructBinaryTree1(tin[i+1:], post[i:-1])
        return root

pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]
post = [5, 6, 3, 4, 2, 1]
test = Solution()
newTree1 = test.reConstructBinaryTree(pre, tin)
newTree2 = test.reConstructBinaryTree1(tin, post)


# 求树的深度
def depth(tree):
    if tree is None:
        return 0
    left, right=depth(tree.left), depth(tree.right)
    return max(left, right)+1

# print(depth(newTree1))


# 按层次输出树的值
def PrintNodeByLevel(tree):
    currentLevel = [tree]
    data = []
    while currentLevel:
        data.append([c.val for c in currentLevel])
        nextLevel = []
        for i in currentLevel:
            if i.left:
                nextLevel.append(i.left)
            if i.right:
                nextLevel.append(i.right)
        currentLevel = nextLevel
    return data

print(PrintNodeByLevel(newTree1))


# 通用解法
#def buildTree(self, inorder, postorder):
#   """
#   :type inorder  : List[int]
#   :type postorder: List[int]
#   :rtype: TreeNode
#   """
#   if inorder:
#       idx = inorder.index(postorder.pop())
#       root = TreeNode(inorder[idx])
#       root.right = self.buildTree(inorder[idx+1:], postorder)
#       root.left = self.buildTree(inorder[:idx], postorder)
#       return root


