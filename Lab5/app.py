import utils

def main():
    while True : 
        x = input()
        if x == "q" :
            break
        print(utils.process_item(int(x)))

if __name__ == "__main__" :
    main()