def count_graphs(n):
    # 無向簡單圖總數 = 2^(n*(n-1)//2)
    # C(n, 2) = n*(n-1)/2
    return 1 << (n * (n - 1) // 2)  # 位移等同於 2**...

if __name__ == "__main__":
    n = int(input().strip())
    print(count_graphs(n))
