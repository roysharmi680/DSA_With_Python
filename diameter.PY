
class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root):
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if node is None:
                return 0

            first = 0
            second = 0

            for child in node.children:
                depth = 1 + dfs(child)

                if depth > first:
                    second = first
                    first = depth
                elif depth > second:
                    second = depth

            diameter = max(diameter, first + second)

            return first

        dfs(root)
        return diameter


# Main program
def main():
    # Create the N-ary tree
    root = TreeNode(1, [
        TreeNode(3, [
            TreeNode(5),
            TreeNode(6)
        ]),
        TreeNode(2),
        TreeNode(4)
    ])

    obj = Solution()
    result = obj.diameter(root)

    print("Diameter of N-ary tree:", result)


if __name__ == "__main__":
    main()
