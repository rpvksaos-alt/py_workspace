import random

quiz = {
    "Python에서 화면에 출력하는 함수는?": "print",
    "리스트를 만드는 기호는?": "[]",
    "반복문에서 사용하는 키워드는?": "for",
    "함수를 정의할 때 사용하는 키워드는?": "def",
    "참과 거짓을 표현하는 자료형은?": "bool"
}

def play_quiz():
    questions = list(quiz.items())

    random.shuffle(questions)

    correct_count = 0
    wrong_answers = []

    print("===== 랜덤 퀴즈 게임 =====")

    for i, (question,answer) in enumerate(questions, start=1):
        print(f'\n{i}번 문제: {question}')

        try:
            user_answer = input('정답 입력 :').strip()

            if user_answer.lower() == answer.lower():
                print('정답입니다!')
                correct_count += 1
            else:
                print('오답입니다!')
                print(f'정답: {answer}')
                wrong_answers.append({
                    "question": question,
                    "user_answer": user_answer,
                    "answer": answer
                })
        except (KeyboardInterrupt, EOFError):
            print('\n게임을 종료합니다!')
            return

    total = len(questions)
    worng_count = total - correct_count
    score = round(correct_count / total * 100)

    print("\n===== 게임 종료 =====")
    print(f'전체 문제:{total}')
    print(f'정답:{correct_count}')
    print(f'오답:{worng_count}')
    print(f'점수:{score}')

    print("\n===== 오답 목록 =====")
    if not wrong_answers:
        print('모든 문제를 맞췄습니다.')
    else:
        for item in wrong_answers:
            print(f'문제:{item['question']}')
            print(f'내 답:{item['user_answer']}')
            print(f'정답:{item['answer']}')
            print("-" * 30)

play_quiz()