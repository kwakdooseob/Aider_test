# 구구단 프로그램

def gugudan(n):
    print(f"{n}단")
    for i in range(1, 10):
        result = n * i
        print(f"{n} x {i} = {result}")

def main():
    num = input("단수를 입력하세요: ")
    try:
        num = int(num)
        gugudan(num)
    except ValueError:
        print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()
