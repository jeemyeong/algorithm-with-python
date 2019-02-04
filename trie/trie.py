class Trie:
    def __init__(self, char):
        self.char = char
        self.children = {}

    def add(self, word):
        if not word:
            return
        ch = word[0]
        if ch in self.children:
            self.children[ch].add(word[1:])
        else:
            self.children[ch] = Trie(ch)
            self.children[ch].add(word[1:])

    def find_prefix(self, prefix):
        if not prefix:
            return True
        ch = prefix[0]
        if ch not in self.children:
            return False
        return self.children[ch].find_prefix(prefix[1:])

if __name__ == "__main__":
    root = Trie('*')
    root.add("hackathon")
    root.add('hack')

    print(root.find_prefix('hac'))
    print(root.find_prefix('hack'))
    print(root.find_prefix('hackathon'))
    print(root.find_prefix('ha'))
    print(root.find_prefix('hammer'))
