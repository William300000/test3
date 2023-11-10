print(f"猜数字游戏开始！目标数字在 {x1} 和 {x2} 之间。")

while attempts < max_attempts:
    guess = int(input("请输入你的猜测数字: "))

    if guess == target_number:
        print(f"恭喜！你猜对了，目标数字是 {target_number}。")
        break
    elif guess < target_number:
        print("你的猜测太低了，请再试一次。")
    else:
        print("你的猜测太高了，请再试一次。")

    attempts += 1

if attempts == max_attempts:
    print(f"很抱歉，你已经达到最大尝试次数 {max_attempts}，游戏结束。目标数字是 {target_number}。")