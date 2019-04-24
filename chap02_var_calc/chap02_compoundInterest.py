money = int(input("원금을 입력하세요: "))
interest_rate = float(input("이자율을 입력하세요: "))
year = int(input("예치 기간(년)을 입력하세요: "))

print("원리금 합계:", money * (1 + interest_rate)**year)