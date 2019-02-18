class A(object):
    pass
class B(A):
    pass
class C(A):
    pass

class D(B, C):
    pass
class E(C, B):
    pass
class F(D, E):
    pass