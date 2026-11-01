
class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        double_string = s + s
        return goal in double_string


def main():
    s = input("Enter the original string: ")
    goal = input("Enter the goal string: ")

    obj = Solution()
    result = obj.rotateString(s, goal)

    print(result)


if __name__ == "__main__":
    main()
