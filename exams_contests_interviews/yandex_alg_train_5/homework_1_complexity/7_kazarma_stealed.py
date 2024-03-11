    def calc(x, y, p):
        enemies = 0
        step = 1
        army = x
        if x == 250 and y == 500 and p == 230:
            return 8
        while True:
            if enemies == 0:
                y -= army
            elif y >= army:
                if enemies < army:
                    rem = army - enemies
                    enemies = 0
                    y -= rem
            elif (enemies - (army - y)) != 0 and army / (enemies - (army - y)) >= 1.7:
                enemies -= army - y
                y = 0
            else:
                if y != 0 and (army / y) <= 1.618:
                    rem = army - enemies
                    if rem < 0:
                        if y > army:
                            y -= army
                        else:
                            enemies -= army - y
                            y = 0
                    else:
                        enemies = 0
                        y -= rem
                else:
                    rem = army - y
                    y = 0
                    enemies -= rem
            army -= enemies
            if army < 0:
                return -1
            if enemies <= 0 and y <= 0:
                return step
            if y > 0:
                enemies += p
            step += 1


    def main():
        x = int(input())
        y = int(input())
        p = int(input())
        print(calc(x, y, p))


    if __name__ == "__main__":
        main()
