
import random

quiz = {
    "Python에서 화면에 출력하는 함수는?": "print",
    "리스트를 만드는 기호는?": "[]",
    "반복문에서 사용하는 키워드는?": "for",
    "함수를 정의할 때 사용하는 키워드는?": "def",
    "참과 거짓을 표현하는 자료형은?": "bool"
}


def play_quiz():
    # 1. 문제 목록을 리스트로 변환
    questions = list(quiz.items())

    # 2. 문제 순서 무작위로 섞기
    random.shuffle(questions)

    # 3. 정답 개수와 오답 목록 초기화
    correct_count = 0
    wrong_answers = []

    print("===== 랜덤 퀴즈 게임 =====")

    # 4. 반복문으로 문제 출제
    for i, (question, answer) in enumerate(questions, start=1):
        print(f"\n{i}번 문제: {question}")

        # 예외 처리
        try:
            user_answer = input("정답 입력: ").strip()

            # 5. 사용자 답과 정답 비교
            if user_answer.lower() == answer.lower():
                print("정답입니다!")
                correct_count += 1
            else:
                print("오답입니다.")
                print(f"정답: {answer}")

                wrong_answers.append({
                    "question": question,
                    "user_answer": user_answer,
                    "answer": answer
                })

        except (KeyboardInterrupt, EOFError):
            print("\n게임을 종료합니다.")
            return

    # 6. 최종 결과 출력
    total = len(questions)
    wrong_count = total - correct_count
    score = round(correct_count / total * 100)

    print("\n===== 게임 종료 =====")
    print(f"전체 문제: {total}개")
    print(f"정답: {correct_count}개")
    print(f"오답: {wrong_count}개")
    print(f"점수: {score}점")

    # 오답 목록 출력
    print("\n===== 오답 목록 =====")

    if not wrong_answers:
        print("모든 문제를 맞혔습니다!")
    else:
        for item in wrong_answers:
            print(f"문제: {item['question']}")
            print(f"내 답: {item['user_answer']}")
            print(f"정답: {item['answer']}")
            print("-" * 30)


play_quiz()

