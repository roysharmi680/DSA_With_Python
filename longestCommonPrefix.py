
class Solution:
    def longestCommonPrefix(self, st):
        if not st:
            return ""

        st.sort()
        first = st[0]
        last = st[-1]
        ans = []

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ''.join(ans)
            ans.append(first[i])

        return ''.join(ans)


if __name__ == "__main__":
    st = input("Enter strings separated by space: ").split()

    obj = Solution()
    result = obj.longestCommonPrefix(st)

    print("Longest Common Prefix:", result)
