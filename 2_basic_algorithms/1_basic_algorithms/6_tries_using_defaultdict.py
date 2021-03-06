# Tries Using Defaultdict
'''
A cleaner way to build a trie is with a Python default
dictionary. The following TrieNode class is using
collections.defaultdict instead of a normal dictionary.
'''

import collections


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        # Adding word to trie
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]
            current_node.is_word = True

    def exists(self, word):
        # Checking if word exists within the trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word

# Adding words
valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
word_trie = Trie()
for valid_word in valid_words:
    word_trie.add(valid_word)

assert word_trie.exists('the')
assert word_trie.exists('any')
assert not word_trie.exists('these')
assert not word_trie.exists('zzz')
print('All tests passed!')


'''
The Trie data structure is part of the family of Tree
data structures. It shines when dealing with sequence
data, whether it's characters, words, or network nodes.
When working on a problem with sequence data, ask
yourself if a Trie is right for the job.
'''
