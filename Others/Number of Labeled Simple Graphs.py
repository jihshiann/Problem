def count_graphs(n):
    # �L�V²����`�� = 2^(n*(n-1)//2)
    # C(n, 2) = n*(n-1)/2
    return 1 << (n * (n - 1) // 2)  # �첾���P�� 2**...

if __name__ == "__main__":
    n = int(input().strip())
    print(count_graphs(n))
