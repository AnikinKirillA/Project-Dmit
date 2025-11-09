def FAC_P_Q(p: Polynomial):
    """Сделал: Соколовский Артём"""
    if p.m<0:
        zero=Rational(Integer(0,0,[0]),Natural(0,[1]))
        return Rational(Integer(0,0,[0]),Natural(0,[1])),Polynomial(0,[zero])
    L=Natural(p.C[0].denominator.len,p.C[0].denominator.A[:])
    for i in range(1,p.m+1):
        d=Natural(p.C[i].denominator.len,p.C[i].denominator.A[:])
        L=LCM_NN_N(L,d)
    ints=[]
    for i in range(0,p.m+1):
        ci=p.C[i]
        fd=DIV_NN_N(Natural(L.len,L.A[:]),Natural(ci.denominator.len,ci.denominator.A[:]))
        fd_int=TRANS_N_Z(fd)
        ints.append(ci.numerator*fd_int)
    abs_list=[ABS_Z_N(z) for z in ints]
    G=abs_list[0]
    for i in range(1,len(abs_list)):
        G=GCF_NN_N(G,abs_list[i])
    G_int=TRANS_N_Z(Natural(G.len,G.A[:]))
    reduced=[Z/G_int for Z in ints]
    one=Natural(0,[1])
    newC=[Rational(Integer(z.s,z.len,z.A[:]),Natural(one.len,one.A[:])) for z in reduced]
    newP=Polynomial(p.m,newC)
    factor=Rational(TRANS_N_Z(Natural(G.len,G.A[:])),Natural(L.len,L.A[:]))
    return factor,newP
