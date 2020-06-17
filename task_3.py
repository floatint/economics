# ДЛЯ ЗАДАНИЯ ВИДА:
# В таблице приведены разные уровни располагаемого дохода.
# Рассчитайте величину потребления и сбережения при разных уровнях дохода, если АPC = 0,65

# средняя склонность потребления (ACP)
APC = 0.65

# функция потребления
Cfunc = lambda d: d * APC

# Фунция сбережения
Sfunc = lambda d: d - Cfunc(d)

# доход
D = [0, 1000, 2000, 3000]

# MPC - предельная склонность потребления
MPC = [None, 0, 0, 0]
# MPS - предельная склонность сбережения
MPS = [None, 0, 0, 0]

# потребление
C = [0, 0, 0, 0]
# сбережение
S = [0, 0, 0, 0]

print("Потребление: " + str(list(map(Cfunc, D))))
print("Сбережение: " + str(list(map(Sfunc, D))))
print("APC = " + str(APC))
print("APS = " + str(1 - APC))
for i in range(1, len(MPC)):
    MPC[i] = (Cfunc(D[i]) - Cfunc(D[i - 1])) / (D[i] - D[i - 1])
    MPS[i] = 1 - MPC[i]
print("MPC = " + str(MPC))
print("MPS = " + str(MPS))
