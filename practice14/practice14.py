import time


class Prak14:
    def __init__(self):
        pass

    def timer(f):
        def tmp(*args, **kwargs):
            t = time.time()
            res = f(*args, **kwargs)
            print("Время выполнения функции: %f" % (time.time() - t))
            return res
        return tmp


    @timer
    def oddList(self):
        lst = []
        for i in range(100000):
            if i % 2 == 0:
                lst.append(i)


    @timer
    def oddList2(self):
        lst = [x for x in range(100000) if x % 2 == 0]

    @staticmethod
    @timer
    def fibCash():
        lst = [0, 1, 1]
        def fibVar(n):
            nonlocal lst
            maxi = lst[-1]
            if maxi >= n:
                print("[", end="")
                for i in lst:
                    if i <= n:
                        print(i, end=", ")
                    else:
                        print("]")
                        break
            else:
                while n >= maxi:
                    lst.append(lst[-2]+lst[-1])
                    maxi = lst[-1]
                return lst
        return fibVar

    @staticmethod
    @timer
    def fibNoCash(n):
        lst = [0, 1, 1]
        while lst[-1] <= n:
            lst.append(lst[-2]+lst[-1])
        return lst







