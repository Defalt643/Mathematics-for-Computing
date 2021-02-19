from __future__ import division
import numpy as np

class Tableau:

    def __init__(self, obj):
        self.obj = [1] + obj
        self.rows = []
        self.cons = []
        self.sumc = []
        self.x = []
        self.sumr = []

    def add_constraint(self, expression, value):
        self.rows.append([0] + expression)
        self.cons.append(value)

    def _pivot_column(self):
        idx = self.obj.argmin()
        return idx

    def _pivot_row(self, col):
        rhs = [self.rows[i][-1] for i in range(len(self.rows))]
        lhs = [self.rows[i][col] for i in range(len(self.rows))]
        ratio = []
        for i in range(len(rhs)):
            ratio.append(rhs[i]/lhs[i])
            f = np.absolute(ratio)
        return np.argmin(f)

    def display(self):
        np.set_printoptions(suppress=True)
        self.x = np.matrix([self.obj] + self.rows)
        print(self.x)


    def _pivot(self, row, col):
        e = self.rows[row][col]
        self.rows[row] /= e
        for r in range(len(self.rows)):
            if r == row: continue
            self.rows[r] = self.rows[r] - self.rows[r][col]*self.rows[row]
            self.obj = self.obj - self.obj[col]*self.rows[row]

    def _check(self):
        if min(self.obj[1:-1]) >= 0:
            return 1
        return 0

    def solve(self):
        for i in range(len(self.rows)):
            self.obj += [0]
            ident = [0 for r in range(len(self.rows))]
            ident[i] = 1
            self.rows[i] += ident + [self.cons[i]]
            self.rows[i] = np.array(self.rows[i], dtype=float)
        self.obj = np.array(self.obj + [0], dtype=float)
        self.display()

        while not self._check():
            c = self._pivot_column()
            c1 = np.array([c])
            self.sumc.append([0] + c1)
            r = self._pivot_row(c)
            r1 = np.array([r])
            self.sumr.append([0] + r1)
            self._pivot(r,c)
            print('pivot column:', c+1,'pivot row:',r+2)
            self.display()

        Newmatrix = np.delete(self.x,np.s_[:len(self.rows[0])-1],1)
        print(Newmatrix)
        print('Z = ', Newmatrix[0]*(-1))
        n = np.array(self.sumc)
        m = np.array(self.sumr)
        p = m+1
        for i in range(len(p)):
            print('X',n[i],'= ',Newmatrix[p[i]])

        for j in range(len(Newmatrix) - 1):
            j += 1
            if (j != n):
                print('X', [j], '= 0')

        Nsame = 0
        same = 0
        for j in range(len(Newmatrix) - 1):
            for k in range(len(p)):
                if (Newmatrix[j + 1] == Newmatrix[p[k]]):
                    same = same + 1
                else:
                    Nsame = Nsame + 1
            if (Nsame != same and Nsame > same):
                print("S", [j + 1], '= ', Newmatrix[j + 1])
            else:
                print("S", [j + 1], '= ', 0)

            Nsame = 0
            same = 0

if __name__ == '__main__':
    """
        Minimize Z = X1 + X2 - 4X3
        st
        X1 + X2 + 2X3 ≤ 9
        X1 + X2 - 1X3 ≤ 6
        -X1 + X2 + X3 ≤ 7
        X1,X2,X3 ≥ 0
    """
    t = Tableau([1,1,-4])
    t.add_constraint([1, 1,2], 9)
    t.add_constraint([1, 1,-1], 6)
    t.add_constraint([-1,1, 1], 7)
    t.solve()