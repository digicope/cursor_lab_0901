"""
BMI(체질량지수) 계산기
키와 몸무게를 입력받아 비만도를 계산하는 프로그램
"""

def calculate_bmi(height, weight):
    """
    BMI를 계산하는 함수
    
    Args:
        height (float): 키 (cm)
        weight (float): 몸무게 (kg)
    
    Returns:
        float: BMI 값
    """
    # 키를 cm에서 m로 변환
    height_m = height / 100
    # BMI 계산: 몸무게(kg) / 키(m)²
    bmi = weight / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    """
    BMI 값에 따른 비만도 분류
    
    Args:
        bmi (float): BMI 값
    
    Returns:
        str: 비만도 분류
    """
    if bmi < 18.5:
        return "저체중"
    elif 18.5 <= bmi < 23:
        return "정상체중"
    elif 23 <= bmi < 25:
        return "과체중"
    elif 25 <= bmi < 30:
        return "경도비만"
    elif 30 <= bmi < 35:
        return "중등도비만"
    else:
        return "고도비만"

def main():
    """메인 함수"""
    print("=" * 50)
    print("           BMI(체질량지수) 계산기")
    print("=" * 50)
    
    try:
        # 사용자로부터 키와 몸무게 입력받기
        height = float(input("키를 입력하세요 (cm): "))
        weight = float(input("몸무게를 입력하세요 (kg): "))
        
        # 입력값 검증
        if height <= 0 or weight <= 0:
            print("키와 몸무게는 0보다 큰 값을 입력해주세요.")
            return
        
        # BMI 계산
        bmi = calculate_bmi(height, weight)
        
        # 비만도 분류
        category = get_bmi_category(bmi)
        
        # 결과 출력
        print("\n" + "=" * 50)
        print("              계산 결과")
        print("=" * 50)
        print(f"키: {height}cm")
        print(f"몸무게: {weight}kg")
        print(f"BMI: {bmi:.2f}")
        print(f"비만도: {category}")
        
        # 추가 정보 제공
        print("\n" + "-" * 30)
        print("BMI 분류 기준:")
        print("저체중: 18.5 미만")
        print("정상체중: 18.5 ~ 22.9")
        print("과체중: 23.0 ~ 24.9")
        print("경도비만: 25.0 ~ 29.9")
        print("중등도비만: 30.0 ~ 34.9")
        print("고도비만: 35.0 이상")
        print("-" * 30)
        
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
