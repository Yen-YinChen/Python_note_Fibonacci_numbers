while True:
    try:
        h = input("Enter Hours: ")
        hours = float(h)
        if hours > 0:
            r = input("Enter Rate: ")
            rate = float(r)
            if rate > 0:
                if hours <= 40:
                    tot = hours * rate
                    print("Pay", tot)
                elif hours > 40:
                    tot = ((hours - 40) * 1.5 * rate) + (40 * rate)
                    print("Pay", tot)
            else:
                print("Error, please enter numneric input")
                continue
        else:
            print("Error, please enter numneric input")
            continue
    except:
        print("Error, please enter numneric input")
        continue
    break
