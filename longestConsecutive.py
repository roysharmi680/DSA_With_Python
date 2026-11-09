
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def longestConsecutive(self, root):
        self.ans = 0

        def dfs(node):
            if node is None:
                return 0, 0

            inc = 1
            dec = 1

            left_inc, left_dec = dfs(node.left)
            right_inc, right_dec = dfs(node.right)

            # Check left child
            if node.left:
                if node.left.val == node.val + 1:
                    inc = max(inc, left_inc + 1)
                elif node.left.val == node.val - 1:
                    dec = max(dec, left_dec + 1)

            # Check right child
            if node.right:
                if node.right.val == node.val + 1:
                    inc = max(inc, right_inc + 1)
                elif node.right.val == node.val - 1:
                    dec = max(dec, right_dec + 1)

            # Combine increasing and decreasing paths
            self.ans = max(self.ans, inc + dec - 1)

            return inc, dec

        dfs(root)
        return self.ans


# Build binary tree from level-order input
def buildTree(values):
    if not values or values[0] == "None":
        return None

    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if values[i] != "None":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] != "None":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root


def main():
    values = input("Enter tree nodes in level order: ").split()

    root = buildTree(values)

    obj = Solution()
    result = obj.longestConsecutive(root)

    print("Longest consecutive path length:", result)


if __name__ == "__main__":
    main()
