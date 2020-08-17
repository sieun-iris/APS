T = int(10)


def listing(a):
    if a == 0:
        return

    print(a)
    a -= 1


    listing(a)

listing(T)