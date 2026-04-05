class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)  # just the length

        n_h, n_l = [0]*n, [0]*n

        dict1, res = {}, SortedList()

        res.add(arr[n-1])

        dict1[arr[n-1]] = n-1

        for i in range(n-2,-1,-1):
            idx = res.bisect_left(arr[i])

            if idx < len(res):
                n_h[i] = dict1[res[idx]]

            res.add(arr[i])

            dict1[arr[i]] = i

        
        dict1, res = {}, SortedList()

        res.add(-arr[n-1])

        dict1[-arr[n-1]] = n-1

        for i in range(n-2,-1,-1):
            idx = res.bisect_left(-arr[i])

            if idx < len(res):
                n_l[i] = dict1[res[idx]]

            res.add(-arr[i])
            dict1[-arr[i]] = i


        h, l = [0]*n, [0]*n

        h[-1] = l[-1] = 1 

        for i in range(n-2,-1,-1):
            h[i] = l[n_h[i]]
            l[i] = h[n_l[i]]

        return sum(h)
