#!/usr/bin/env python
 
 
def rational_to_contfrac(x,y):
    # Converts a rational x/y fraction into a list of partial quotients [a0, ..., an]
    a = x // y
    pquotients = [a]
    while a * y != x:
        x, y = y, x - a * y
        a = x // y
        pquotients.append(a)
    return pquotients
 
def convergents_from_contfrac(frac):
    # computes the list of convergents using the list of partial quotients
    convs = [];
    for i in range(len(frac)): convs.append(contfrac_to_rational(frac[0 : i]))
    return convs
 
def contfrac_to_rational (frac):
    # Converts a finite continued fraction [a0, ..., an] to an x/y rational.
    if len(frac) == 0: return (0,1)
    num = frac[-1]
    denom = 1
    for _ in range(-2, -len(frac) - 1, -1): num, denom = frac[_] * num + denom, num
    return (num, denom)
 
n = 130293403397924930670347161122260411360743004016661636387075141125935939349475557950374330864663613708450851543613818580618697532506963030299282677739754681641907703194842033068614318423216427331062753545084531165659246486747822432168693404929380093887712040910272117990194045924420141523914986508603787677563
 
e = 94078370114488085268649740016578191342321432062383772456364843572644682941796738907329656695404837943415211955007850665325806581560980782714990853919510050951041769823732115101892965788925741400638610286258069858262183364146633258158203982412123367253512814171104752666424717739604113050957013473158501064153
 
c = 90730476301891154318609901961556178470093982248910116490217061235820764485202877452430690870724112266683100346419583737545650748359928063632837994530565412729020718301386266313464423038700107632520232308453842670150092328043034889091651074854994595672710067473367875531296903927970579280007900397371641583832
 
def egcd(a, b):
    if a == 0: return (b, 0, 1)
    g, x, y = egcd(b % a, a)
    return (g, y - (b // a) * x, x)
 
def mod_inv(a, m):
    g, x, _ = egcd(a, m)
    return (x + m) % m
 
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
 
def crack_rsa(e, n):
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)
   
    for (k, d) in convergents:
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            # check if x*x - s*x + n = 0 has integer roots
            D = s * s - 4 * n
            if D >= 0:
                sq = isqrt(D)
                if sq * sq == D and (s + sq) % 2 == 0: return d
 
d = crack_rsa(e, n)
m = hex(pow(c, d, n)).rstrip("L")[2:]
print(m.decode("hex"))