# node of a trie which is used for ease of implementation
class TrieNode:
    def __init__(self):
        # the other nodes
        self.children = {}

        # the sentences associated with this
        self.sentences = defaultdict(int)

'''
For each input character except '#'
return the top 3 historical hot sentences
that have the same prefix as the part of the sentence already typed.

The hot degree for a sentence is defined as
the number of times a user typed the exactly same sentence before.

The returned top 3 hot sentences should be sorted by hot degree.
(The first is the hottest one.)
If several sentences have the same hot degree,
use ASCII-code order (smaller one appears first).

If less than 3 hot sentences exist, return as many as you can.
When the input is '#', it means the sentence ends,
and in this case, you need to return an empty list.
'''

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()

        # adds all sentences which it was instantiated with
        for sentence, count in zip(sentences, times):
            self.add_to_trie(sentence, count)
        
        # stores current sentence and node
        self.curr_sentence = []
        self.curr_node = self.root
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            # this is the end of a sentence
            curr_sentence = "".join(self.curr_sentence)
            
            # add it to the trie now
            self.add_to_trie(curr_sentence, 1)
            
            # make everything else default
            self.curr_sentence = []
            self.curr_node = self.root
            return []
        
        self.curr_sentence.append(c)
        if c not in self.curr_node.children:
            # means it's never been seen
            self.curr_node = TrieNode()
            return []
        
        # go to the children of this node
        self.curr_node = self.curr_node.children[c]

        # find the sentences and their counts
        items = [(val, key) for key, val in self.curr_node.sentences.items()]

        # return the top 3 sentences ranked by count
        # which correspond to this character
        ans = heapq.nsmallest(3, items)
        return [item[1] for item in ans]

    # the trie is used to easily find words and sentences
    # it can be used to rank the results
    def add_to_trie(self, sentence, count):
        node = self.root
        for c in sentence:
            
            # adds the sentence to the trie
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

            # the new node has one less count for this sentence
            # because heapq finds the minimum
            node.sentences[sentence] -= count
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
