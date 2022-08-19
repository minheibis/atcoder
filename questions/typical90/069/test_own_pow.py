def own_pow(x, n):
    ans = 1
    # n が 0 になるまで計算を続ける
    # これはビット化した
    while n:
        print("n: ", n)
        print("x: ", x)
        if n % 2:
            print("--mul x--")
            # 余りがないなら今までのものを２乗すれば良い？
            ans *= x
            # ans %= m # MODを計算
        else:
            print("--no mul x--")
        x *= x # 次のxの2乗を繰り返し計算する
        # x %= m # MODを計算
        print("ans: ", ans)
        print("")
        n >>= 1
    return ans

print(own_pow(2, 10))