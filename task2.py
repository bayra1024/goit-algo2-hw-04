from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not all(isinstance(elem, str) for elem in strings):
            raise TypeError(
                f"Illegal argument for keysWithPrefix: prefix = {strings} must be a list of strings"
            )
        for i, word in enumerate(strings):
            trie.put(word, i)

        result = ""
        current = self.root
        while len(current.children) == 1:
            result += list(current.children.keys())[0]
            current = list(current.children.values())[0]

        return result


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

print("DONE")
