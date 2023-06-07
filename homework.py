import random

# 正解の数字をランダムに生成
def generate_answer():
    digits = random.sample(range(10), 3)
    return ''.join(map(str, digits))

# ユーザーの解答を受け取り、正誤を判定する
def check_answer(answer, guess):
    if answer == guess:
        return True
    else:
        return False

# ヒントを生成する
def generate_hint(answer, guess):
    hint = []
    for i in range(len(answer)):
        if answer[i] == guess[i]:
            hint.append(answer[i])
        else:
            hint.append('*')
    return ' '.join(hint)

# ゲームの実行
def play_game():
    answer = generate_answer()
    attempts = 0
    max_attempts = 10

    print("=== 数字当てゲーム ===")
    print("3桁の数字を当ててください。")
    print("ヒント: *は数字のみ正解")
    print("====================")

    while attempts < max_attempts:
        guess = input("数字を入力してください: ")

        if len(guess) != 3 or not guess.isdigit():
            print("無効な入力です。3桁の数字を入力してください。")
            continue

        attempts += 1

        if check_answer(answer, guess):
            print("正解です！")
            break
        else:
            print("不正解です。")
            hint = generate_hint(answer, guess)
            print("ヒント:", hint)

    if attempts == max_attempts:
        print("解答回数の制限に達しました。正解は", answer, "でした。")
play_game()