students = []

FILE_NAME = "students.txt" # 상수 선언 (변경x)
SUBJECTS = ["국어", "영어", "수학"] # 상수 선언 (변경x)


def add_student():
    """학생 이름과 과목별 점수를 등록한다.""" # 이 함수에 대한 설명
    name = input("학생 이름: ").strip()

    if not name:
        print("이름을 입력하세요.")
        return # 함수 끝

    if any(student["name"] == name for student in students):
        print("이미 등록된 학생입니다.")
        return

    scores = {}

    for subject in SUBJECTS:
        while True:
            try:
                score = int(input(f"{subject} 점수(0~100): "))
                if 0 <= score <= 100:
                    scores[subject] = score
                    break # while문 종료
                print("점수는 0점 이상 100점 이하로 입력하세요.")
            except ValueError:
                print("점수는 숫자로 입력하세요.")

    students.append({"name": name, "scores": scores})
    print(f"{name} 학생 등록 완료!")


def show_students():
    """전체 학생의 과목별 점수를 출력한다."""
    if not students:
        print("등록된 학생이 없습니다.")
        return

    print("\n이름\t국어\t영어\t수학")
    print("-" * 35)

    for student in students:
        scores = student["scores"]
        print(
            f'{student["name"]}\t'
            f'{scores["국어"]}\t'
            f'{scores["영어"]}\t'
            f'{scores["수학"]}'
        )


def get_average(student): # 학생 한명씩
    """학생 한 명의 세 과목 평균을 반환한다."""
    scores = student["scores"]
    return sum(scores.values()) / len(scores)


def get_grade(average):
    """평균 점수에 해당하는 등급을 반환한다."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"


def show_student_results():
    """학생별 평균과 등급을 출력한다."""
    if not students:
        print("등록된 학생이 없습니다.")
        return

    for student in students:
        average = get_average(student)
        grade = get_grade(average)
        print(f'{student["name"]}: 평균 {average:.2f}점, 등급 {grade}')


def show_top_bottom():
    """평균 기준 최고점과 최저점 학생을 모두 출력한다."""
    if not students:
        print("등록된 학생이 없습니다.")
        return

    averages = [get_average(student) for student in students]
    highest = max(averages)
    lowest = min(averages)

    print(f"최고 평균: {highest:.2f}점")
    for student in students:
        if get_average(student) == highest:
            print(f'  {student["name"]}')

    print(f"최저 평균: {lowest:.2f}점")
    for student in students:
        if get_average(student) == lowest:
            print(f'  {student["name"]}')


def show_above_average():
    """전체 학생 평균 이상인 학생을 출력한다."""
    if not students:
        print("등록된 학생이 없습니다.")
        return

    class_average = sum(get_average(student) for student in students) / len(students)
    print(f"전체 학생 평균: {class_average:.2f}점")
    print("평균 이상 학생:")

    found = False # 한명도 없으면 False, 한명이라도 있으면 True
    for student in students:
        average = get_average(student)
        if average >= class_average:
            print(f'  {student["name"]}: {average:.2f}점')
            found = True

    if not found:
        print("평균 이상인 학생이 없습니다.")


def save_students():
    """현재 학생 정보를 TXT 파일에 저장한다."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for student in students:
                scores = student["scores"]
                line = (
                    f'{student["name"]},'
                    f'{scores["국어"]},'
                    f'{scores["영어"]},'
                    f'{scores["수학"]}\n'
                )
                file.write(line)

        print(f"{FILE_NAME} 저장 완료!")
    except OSError as error:
        print(f"파일 저장 중 오류가 발생했습니다: {error}")


def main():
    """메뉴를 반복해서 실행한다."""
    global students

    while True:
        print("\n===== 학생 성적 관리 프로그램 =====")
        print("1. 학생 등록")
        print("2. 전체 학생 성적 조회")
        print("3. 학생별 평균 및 등급 조회")
        print("4. 최고점·최저점 학생 조회")
        print("5. 평균 이상 학생 조회")
        print("6. 성적 파일 저장")
        print("0. 종료")

        try:
            menu = int(input("메뉴 선택: "))
        except ValueError:
            print("메뉴는 숫자로 입력하세요.")
            continue

        if menu == 1:
            add_student()
        elif menu == 2:
            show_students()
        elif menu == 3:
            show_student_results()
        elif menu == 4:
            show_top_bottom()
        elif menu == 5:
            show_above_average()
        elif menu == 6:
            save_students()
        elif menu == 0:
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴 번호를 선택하세요.")


if __name__ == "__main__":
    main()
