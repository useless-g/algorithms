def gcd_AE(a: int, b: int):
    return gcd_AE(b, a % b) if b else a


if __name__ == "__main__":
    print(gcd_AE(45, 931))
