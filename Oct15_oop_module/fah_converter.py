# 사용자 정의 모듈 (내가 만든 거)
# py파일로 생성

# 섭씨를 화씨로 변환
def convert_c_to_f(celcius_value:float) -> float:
    return celcius_value * 9.0 / 5 + 32

# import 하면 해당 모듈 파일 실행(한번만)
# 함수, 변수 -> 메모리에 올라감
# 모듈 확인용으로 print 코드가 있으면 실행되어버림

# 파일을 직접 실행할때만 테스트 코드 동작하고 싶다면
# 1. 직접 실행 -> __name__의 값 -> "__main__"
# 2. 모듈로 다른 파일에서 import해서 실행했다면
# __name__의 값 -> "실행한 파일명"

# 직접 파일을 실행했을때만 동작
#(모듈이 잘 만들어졌는지 확인하는 용도의 코드)
if __name__=="__main__":
    print('모듈 테스트',convert_c_to_f(10))