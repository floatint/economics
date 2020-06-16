
# TC = TFC + TVC, при Q=0, TVC =0, TC=TFC
# TFC = TC-TVC
# TVC = TC-TFC
# ATC = AFC+AVC
# AFC = TC/Q
# AVC = TVC/Q
# MC = ∆TC/∆Q


Q = [0, 1, 2, 3]
TC = [50, 140, 200, 240]
TFC = [0, 0, 0, 0]
TVC = [0, 0, 0, 0]
ATC = [0, 0, 0, 0]
AFC = [0, 0, 0, 0]
AVC = [0, 0, 0, 0]
MC = [0, 0, 0, 0]

for q in range(0, len(Q)):
    print("Ведем рассчет для Q = " + str(q) + ", TC = " + str(TC[q]))
    print("-----------------------------")
    if Q[q] == 0:
        TFC[q] = TC[q]
        TVC[q] = TC[q] - TFC[q]
        print("TFC[{}] = TC[{}] = {}".format(q, q, TC[q]))
        print("TVC[{}] = TC[{}] - TFC[{}] = {}".format(q, q, q, TVC[q]))
    else:
        TVC[q] = TC[q] - TFC[q - 1]
        TFC[q] = TC[q] - TVC[q]
        AFC[q] = TC[0] / q
        AVC[q] = TVC[q] / q
        ATC[q] = AFC[q] + AVC[q]
        MC[q] = (TC[q] - TC[q - 1]) / (q - (q - 1))
        print("TVC[{}] = TC[{}] - TFC[{}] = {}".format(q, q, q - 1, TVC[q]))
        print("Решение: ({} - {} = {})".format(TC[q], TFC[q - 1], TVC[q]))
        print("TFC[{}] = TC[{}] - TVC[{}] = {}".format(q, q, q, TFC[q]))
        print("Решение: ({} - {} = {})".format(TC[q], TVC[q], TC[q] - TVC[q]))
        print("AFC[{}] = TC[0] / {} = {}".format(q, q, AFC[q]))
        print("Решение: ({} / {} = {})".format(TC[0], q, TC[0] / q))
        print("AVC[{}] = TVC[{}] / {} = {}".format(q, q, q, AVC[q]))
        print("Решение: ({} / {} = {})".format(TVC[q], q, TVC[q] / q))
        print("ATC[{}] = AFC[{}] + AVC[{}] = {}".format(q, q, q, ATC[q]))
        print("Решение: ({} + {} = {})".format(AFC[q], AVC[q], ATC[q]))
        print("MC[{}] = (TC[{}] - TC[{}]) / ({} - ({} - 1)) = {}".format(q, q, q - 1, q, q, MC[q]))
        print("Решение: (({} - {}) / {} = {})".format(TC[q], TC[q - 1], q - (q - 1), MC[q]))
    print("-----------------------------")
