    def isValid(self, s: str) -> bool:
        paran_dic = {
            '(' : ')',
            '{' : '}',
            '[' : ']'

        }

        l = 0
        r = 1

        res = False 
        s = "".join(sorted(s))
        if (len(s) % 2) != 0:
            res = False
            return res