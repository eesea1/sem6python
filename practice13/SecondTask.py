



class SuperStr(str):
    def __init__(self, st):
        self.st = st

    def is_repeatance(self, s):
        if type(s) != str:
            return False
        st = str(self.st)
        while st.find(s) != -1:
            st = st.replace(s, "")
        if len(st) != 0:
            return False
        else:
            return True

    def is_palindrom(self):
        st = str(self.st).lower()
        n = int(len(st)/2)
        for i in range(n):
            if st[i] == st[i*(-1)-1]:
                continue
            else:
                return False
                break
        return True

