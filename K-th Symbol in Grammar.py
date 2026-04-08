# you start with the digit 0 if n == 1
# otherwise, you add 1 for every 0 and 0 for every 1 and decrement n
# so if n == 2, the digits are 01
# and if n == 3, the digits are 0110
# you find the k'th digit (1-indexed)
class Solution:
    def depthFirstSearch(self, n: int, k: int, rootVal: int) -> int:
        if n == 1:
            return rootVal

        totalNodes = 2 ** (n - 1)

        # Target node will be present in the right half sub-tree of the current root node.
        if k > (totalNodes / 2):
            nextRootVal = 1 if rootVal == 0 else 0
            return self.depthFirstSearch(n - 1, k - (totalNodes / 2), nextRootVal)
        # Otherwise, the target node is in the left sub-tree of the current root node.
        else:
            nextRootVal = 0 if rootVal == 0 else 1
            return self.depthFirstSearch(n - 1, k, nextRootVal)

    def kthGrammar(self, n: int, k: int) -> int:
        return self.depthFirstSearch(n, k, 0)
