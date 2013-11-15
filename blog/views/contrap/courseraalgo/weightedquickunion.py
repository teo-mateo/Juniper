__author__ = 'Teo'
#########################
#weighted quick-union
# - integer array of size N
# - interpretation: id[i] is parent of i
# - root of i is id[id[id[...[i]...]]
# - avoid tall trees
# - keep track of size of each tree (number of objects)
# - balance by linking root of smaller tree to root of larger tree.

class WeightedQuickUnionUF:

    def __init__(self, N):
        self.idz = [None] * N

        # set id of each object to self (N array accesses)
        for x in range(0, N):
            self.idz[x] = x

        self.sz = [None] * N
        for x in range(0, N):
            self.sz[x] = 1 #initial weight of each item.

    def root(self, i):
        #chase parent pointers until reaching root
        #the parent of i is id[i].
        while self.idz[i] != i:
            #path compression: if the node is not a root, make it point to its grandparent.
            #this makes the algorithm almost linear.
            self.idz[i] = self.idz[self.idz[i]]
            i = self.idz[i]
        return self.idz[i]

    def connected(self, p, q):
        #if p and q have the same root then they're connected.
        return self.root(p) == self.root(q)

    def union(self, p, q):
        # change root of p to point to root of q.
        root_p = self.root(p)
        root_q = self.root(q)

        if self.sz[p] < self.sz[q]:
            #if p's tree is smaller, add it to q's root.
            self.idz[root_p] = root_q
            self.sz[root_q] += self.sz[root_p]
        else:
            #if q's tree is smaller, add it to p's root.
            self.idz[root_q] = root_p
            self.sz[root_p] += self.sz[root_q]

if __name__ == "__main__":
    wqu = WeightedQuickUnionUF(10)
    wqu.union(2, 3)

    if wqu.connected(2,3):
        print('2,3 connected.')
        print('root of 2: ' + `wqu.root(2)`)
        print('root of 3: ' + `wqu.root(3)`)
        #print 'size of tree that is rooted ad '
