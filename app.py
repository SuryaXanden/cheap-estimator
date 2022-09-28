# Estimator model for https://www.youtube.com/watch?v=skOpzcpPIcE

"""
# v1

x=1500
print(f"x: {x}")
a=1800
print(f"a: {a}")
b=1200
print(f"b: {b}")

aDiff = abs(x-a)
print(f"aDiff: {aDiff}")
bDiff = abs(x-b)
print(f"bDiff: {bDiff}")

minDiff = (min(a,b),min(aDiff, bDiff))[aDiff!=bDiff]

print(f"minDiff: {minDiff}")
"""

"""
# v2
def estimator(x, a, b):
    aDiff = abs(x-a)
    bDiff = abs(x-b)

    if aDiff == bDiff:
        return a if a < b else b
    elif aDiff < bDiff:
        return aDiff
    elif bDiff < aDiff:
        return bDiff

    # return (min(a,b),min(aDiff, bDiff))[aDiff!=bDiff]
x=1500
print(f"x: {x}")
a=1800
print(f"a: {a}")
b=1200
print(f"b: {b}")
print(f"estimate: {estimator(x, a, b)}")
"""

'''
# v3
def estimator(x, aMin, aMax, bMin, bMax):
    print(f"x: {x}")
    a = aMax - aMin
    b = bMax - bMin

    aDiff = abs(x-a)
    bDiff = abs(x-b)

    if aDiff == bDiff:
        return "a" if a < b else "b"
    elif aDiff < bDiff:
        return "aDiff"
    elif bDiff < aDiff:
        return "bDiff"

    # return (min(a,b),min(aDiff, bDiff))[aDiff!=bDiff]
# print(f"estimate: {estimator(x, *(800,1400), *(900,1500))}")
# print(f"estimate: {estimator(x, *(800,1400), *(1000,1000))}")
# print(f"estimate: {estimator(x, *(1600,2100), *(1000,1500))}")
# print(f"estimate: {estimator(*(500,), *(600,1000), *(1000,2000))}")
print(f"estimate: {estimator(*(1200,), *(700,1200), *(0,1000))}")
'''

# v4
def estimator(x, aMin, aMax, bMin, bMax):
    print(f"x: {x}")

    a = aMax - aMin
    b = bMax - bMin

    aDiff = abs(x-a)
    bDiff = abs(x-b)

    # print({
    #     "x": x,
    #     "aMin": aMin,
    #     "aMax": aMax,
    #     "bMin": bMin,
    #     "bMax": bMax,
    #     "a": a,
    #     "b": b,
    # })

    if x in [aMin, aMax]:
        return "aMin" if x == aMin else "aMax"
    elif x in [bMin, bMax]:
        return "bMin" if x == bMin else "bMax"
    elif aDiff and aDiff == bDiff:
        return "a" if a < b else "b"
    elif aDiff < bDiff:
        return "aDiff"
    elif bDiff < aDiff:
        return "bDiff"


# return (min(a,b),min(aDiff, bDiff))[aDiff!=bDiff]
# print(f"estimate: {estimator(x, *(800,1400), *(900,1500))}")
# print(f"estimate: {estimator(x, *(800,1400), *(1000,1000))}")
# print(f"estimate: {estimator(x, *(1600,2100), *(1000,1500))}")
# print(f"estimate: {estimator(*(500,), *(600,1000), *(1000,2000))}")
print(f"estimate: {estimator(*(1200,), *(700,1200), *(1000,2000))}")
