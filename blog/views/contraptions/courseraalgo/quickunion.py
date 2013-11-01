__author__ = 'Teo'

# - integer array of size N
# - interpretation: id[i] is parent of i
# - root of i is id[id[id[...[i]...]]


class QuickUnionUF:

    def __init__(self, N):
        self.idz = [None] * N
        # set id of each object to self (N array accesses)
        for x in range(0, N):
            self.idz[x] = x

    def root(self, i):
        #chase parent pointers until reaching root
        #the parent of i is id[i].
        while self.idz[i] != i:
            i = self.idz[i]
        return self.idz[i]

    def connected(self, p, q):
        #if p and q have the same root then they're connected.
        return self.root(p) == self.root(q)

    def union(self, p, q):
        # change root of p to point to root of q.
        root_p = self.root(p)
        root_q = self.root(q)
        self.idz[root_p] = root_q

