def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def process_item(x):
    while not is_prime(x):
        x += 1
    return x

if __name__ == "__main__":
    print(process_item(int(input())))