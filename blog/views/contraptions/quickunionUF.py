__author__ = 'Teo'


class QuickUnionUF:

    def __init__(self, N):
        self.idz = [None] * N
        for x in range(0, N):
            self.idz[x] = x

    def root(self, i):
        while self.idz[i] != i:
            i = self.idz[i]

        return self.idz[i]

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)

        self.idz[root_p] = root_q




if __name__ == "__main__":
    c = QuickUnionUF(10)
    c.union(6, 2)
    c.union(5, 2)
    c.union(5, 3)
    c.union(9, 2)

    if c.connected(9, 3):
        print ("9 and 3 connected.")
    else:
        print ("9 and 3 not connected.")

    print c.idz