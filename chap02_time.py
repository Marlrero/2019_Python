second = int(input("초를 입력하세요: "))
print("%d시간 %d분 %d초 입니다." %(second // 3600, (second % 3600) // 60, (second % 3600) % 60))