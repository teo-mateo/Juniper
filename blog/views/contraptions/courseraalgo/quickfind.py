__author__ = 'Teo'

# Coursera alogrithms part I

#    - quick-find  is too slow.
#    - quadratic = N^2 array accesses

class QuickFindUF:
    def __init__(self, N):
        self.n = N
        self.idz = [None] * N
        for x in range(0, N):
            self.idz[x] = x

    def connected(self, p, q):
        return self.idz[p] == self.idz[q]

    def union(self, p, q):
        pid = self.idz[p]
        qid = self.idz[q]
        for i in range(0, self.n):
            if self.idz[i] == pid:
                self.idz[i] = qid