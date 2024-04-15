Y,M,D = map(int, input().split())

def season(Y,M,D):
    if M==3 or M==5:
        print("Spring")
    elif M==7 or M==8:
        print("Summer")
    elif M==10:
        print("Fall")
    elif M==1 or M==12:
        print("Winter")
    elif M==2:
        if Y%400 == 0:
            if D<=29:
                print("Winter")
            else:
                print(-1)
        elif Y%100 == 0:
            if D<=28:
                print("Winter")
            else:
                print(-1)
        elif Y%4 == 0:
            if D<=29:
                print("Winter")
            else:
                print(-1)
        else:
            if D<=28:
                print("Winter")
            else:
                print(-1)
    elif D != 31:
        if M=4:
            print("Spring")
        elif M=6:
            print("Summer")
        else:
            print("Fall")
    else:
        print(-1)

season(Y,M,D)