
class Solution(object):

    def generateAbbreviations(self, word):
        result = []

        def backtrack(index, current, count):
            if index == len(word):
                if count > 0:
                    current += str(count)

                result.append(current)
                return

            # Option 1: Abbreviate the current character
            backtrack(index + 1, current, count + 1)

            # Option 2: Keep the current character
            new_current = current

            if count > 0:
                new_current += str(count)

            new_current += word[index]

            backtrack(index + 1, new_current, 0)

        backtrack(0, "", 0)

        return result


def main():
    word = input("Enter a word: ")

    obj = Solution()
    result = obj.generateAbbreviations(word)

    print("Generalized Abbreviations:")
    print(result)


if __name__ == "__main__":
    main()
