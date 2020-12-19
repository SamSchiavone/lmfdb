from lmfdb import db
from sage.all import QQ, PolynomialRing, pari

# given a record from db.hmf_forms, get the polredabs coeffs of its hecke field
def get_hecke_field(rec):
    pol = db.hmf_hecke.lookup(rec['label'], projection = 'hecke_polynomial')
    R = PolynomialRing(QQ, 'x')
    x = R.gens()[0]
    pol = R(pol)
    pol = R(pari(pol).polredbest().polredabs())
    return pol.coefficients()

def assign_hecke_field(rec):
    rec['hecke_field'] = get_hecke_field(rec)
    return rec
