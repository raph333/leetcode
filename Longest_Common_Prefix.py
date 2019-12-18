from typing import List


class Solution:

    @staticmethod
    def longestCommonPrefix1(strs: List[str]) -> str:
        """
        Fist approach: go through each string and shorten the longest common prefix if necessary.
        """
        def common_prefix(s1: str, s2: str) -> str:

            if s1 == '' or s2 == '':
                return ''

            for i, (c1, c2) in enumerate(zip(s1, s2)):
                if c1 != c2:
                    return s1[:i]

            return s1[:i + 1]


        if len(strs) == 0:
            return ''

        longest_prefix = strs[0]

        for string in strs[1:]:

            longest_prefix = common_prefix(string, longest_prefix)

            if longest_prefix == '':
                return ''

        return longest_prefix

    @staticmethod
    def longestCommonPrefix2(strs: List[str]) -> str:
        """
        Cleaner: check the i-th character of each string simultaneously
        """
        longest_common_prefix = ''

        for characters in zip(*strs):

            if len(set(characters)) == 1:
                longest_common_prefix += characters[0]
            else:
                return longest_common_prefix

        return longest_common_prefix

    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        """
        Same as above only faster: don't check (i.e. make set of) all characters. Continue after first different
        character => speedup
        """
        longest_common_prefix = ''

        for i, characters in enumerate(zip(*strs)):

            first_char = characters[0]

            for char in characters[1:]:
                if char != first_char:
                    return longest_common_prefix

            longest_common_prefix += first_char

        return longest_common_prefix

