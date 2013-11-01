from blog.views.contraptions.courseraalgo.quickunion import QuickUnionUF

__author__ = 'Teo'











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