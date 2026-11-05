
class Solution:
    def toggle_case(self, s: str) -> str:
        result = ""

        for ch in s:
            if ch.islower():
                result += ch.upper()
            elif ch.isupper():
                result += ch.lower()
            else:
                result += ch

        return result


def main():
    s = input("Enter a string: ")

    obj = Solution()
    result = obj.toggle_case(s)

    print("Toggled string:", result)


if __name__ == "__main__":
    main()
