from P.Polynomial import Polynomial
from TRANS.TRANS_INT_Q import TRANS_INT_Q

def TRANS_STR_P(s:str):
    l=0
    if s[0] == '-':
        q = TRANS_INT_Q(-1)
        l = len(s)-1
    else:
        q = TRANS_INT_Q(1)
        l = len(s)
    q_arr = [q]
    if l==1 or s[-1]=='1':
        q_arr.append(TRANS_INT_Q(0))
        return Polynomial(1, q_arr)
    for i in range((int(s[-1]))):
        q_arr.append(TRANS_INT_Q(0))
    return Polynomial(int(s[-1]), q_arr)

