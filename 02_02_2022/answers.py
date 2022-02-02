def get_result():
    answers = []
    for i in range(1, 3):
        answer = input(f"{i}. odpoved: ")
        answers.append(answer)

    return answers


if __name__ == "__main__":
    result = get_result()
    print(result)