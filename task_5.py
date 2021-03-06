# ДЛЯ ЗАДАНИЯ ВИДА:
# В таблице 1 заданы разные уровни располагаемого дохода и распределение его между
# потреблением и сбережением при каждом его значении.
# Определить для каждого уровня располагаемого дохода среднюю склонность к потреблению,
# среднюю склонность к сбережению, предельную склонность к потреблению,
# предельную склонность к сбережению.

# Формулы
# P(или Y) - распологаемый доход
# C - потребление
# S - сбережение
# APC(средняя склонность к потреблению) = C / P
# APS(средняя склонность к сбережению) = 1 - APC
# MPC(предельная склонность к потреблению) = ΔC / ΔP
# MPS(предельная склонность к сбережению) = 1 - MPC

P = [900, 1000, 1100]
C = [860, 924, 983]
S = [40, 76, 117]

# что считаем
APCfunc = lambda c,p: c / p
APSfunc = lambda apc: 1 - apc
MPCfunc = lambda dc, dp: dc / dp
MPSfunc = lambda mpc: 1 - mpc


# считаем
for i in range(0, len(P)):
    apc = APCfunc(C[i], P[i])
    aps = APSfunc(apc)
    if i != 0:
        mpc = MPCfunc(C[i] - C[i - 1], P[i] - P[i - 1])
        mps = MPSfunc(mpc)
    else:
        mpc = None
        mps = None
    print("APC = {}, APS = {}, MPC = {}, MPS = {}".format(apc, aps, mpc, mps))
