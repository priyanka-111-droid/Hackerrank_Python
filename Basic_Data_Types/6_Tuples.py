if __name__ == '__main__':
    n = int(input())
    integer_tup = tuple(map(int, input().split()))
    print(hash(integer_tup))
