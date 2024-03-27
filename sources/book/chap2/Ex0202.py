def calcExp(x, err = 1.0E-7):
    nMax = 100
    exp = 0.0
    np = 1.0
    nf = 1.0
    term = np / nf
    exp = term 

    print(f"항번호      항      합계")
    print("{0:3d}   {1:12.8f}   {2:12.8f}".format(0, term, exp))

    for i in range(1, 100):
        np = np * x         # 분모 멱승 계산
        nf = nf * i         # 분자 계승 계산
        term = np / nf      # i 번째 항
        exp = exp + term 
        print("{0:3d}   {1:12.8f}   {2:12.8f}".format(i, term, exp))

        if term <= err: 
            break

if __name__ == "__main__":
    calcExp(1.0) 