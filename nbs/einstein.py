#!/usr/bin/python
import math

eCharge = 1.602176462e-19
mu0 = 4.0 * math.pi * 1e-7
c = 299792458.0
eps0 = 1.0 / (mu0 * c * c)
h = 6.62606876e-34
hBar = h / (2.0 * math.pi)
kb = 1.3806503e-23
avogadro = 6.02214199e23
fConst = eCharge * eCharge / (4.0 * math.pi * eps0)
me = 9.10938188e-31
mp = 1.67262158e-27
md = 1.99900750083 * mp
ab = hBar * hBar / (fConst * me)
Ha = fConst * fConst * me / hBar / hBar
Ry = Ha / 2.0

e0 = -0.5 * 1.1676  # Ha per atom
rho0D2GCC = 0.171  # rho0 D2 g/cc
rho0D2KGM3 = rho0D2GCC * 1000.0  # rho0 D2 kg/m^3
nn0 = rho0D2KGM3 / md * ab * ab * ab  # number of D atoms in ab^3
p0 = 0.0

GPaToAU = 1e9 / (Ha / ab / ab / ab)
AUToGPa = 1.0 / GPaToAU
MbarToAU = 100.0 * GPaToAU
AUToMbar = 1.0 / MbarToAU
AUToK = Ha / kb
KToAU = kb / Ha
K4ToAU = 10000.0 * kb / Ha
AUToeV = Ha / eCharge
eVToAU = 1.0 / AUToeV
timeAU = hBar / Ha
sToAU = Ha / hBar  # == 1/tAU(sec)
e6cmPerSToAU = 1e6 * 0.01 / ab / sToAU  # 10^4*tAU/lAU
kmPerSToAU = 1e3 / ab / sToAU  # 10^3*tAU/lAU
AUTokmPerS = 1.0 / kmPerSToAU
AUToe6cmPerS = 1.0 / e6cmPerSToAU
AUTogcc = md / (ab * ab * ab) / 1000.0
gccToAU = 1.0 / AUTogcc
eVToK = eVToAU * AUToK

eVperangsquareToTHzsquare = eCharge * 1e20 * avogadro * 1000 * 1e-24


def einstein_crystal(spring_k: float, temperature: float, mass: float):
    K = spring_k
    T = temperature
    M = mass

    omega0 = math.sqrt(K / M * eVperangsquareToTHzsquare)
    x = hBar * omega0 * 1e12 / kb / T
    entropyperatom = (
        3
        * kb
        * (0.5 * x / math.tanh(0.5 * x) - math.log(2.0 * math.sinh(0.5 * x)))
        / eCharge
    )
    energyperatom = 3 * kb * T * 0.5 * x / math.tanh(0.5 * x) / eCharge
    helmholtzfreeenergyperatom = (
        3 * kb * T * (math.log(2.0 * math.sinh(0.5 * x))) / eCharge
    )

    return helmholtzfreeenergyperatom, energyperatom, entropyperatom
