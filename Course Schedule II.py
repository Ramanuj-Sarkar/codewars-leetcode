class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency list
        adj = [[] for _ in range(n)]
        # number of prerequisites
        indegree = [0] * n

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        # these are the ones without prerequisites
        q = deque([i for i in range(n) if indegree[i] == 0])
        ans = []

        # get all the stuff out of q
        while q:
            
            node = q.popleft()
            ans.append(node)

            for adjnode in adj[node]:
                indegree[adjnode] -= 1
                # add nodes which have no other prerequisites
                if indegree[adjnode] == 0:
                    q.append(adjnode)
        
        # if len(ans) != n, then it's impossible to take all the courses
        return ans if len(ans) == n else [] 
