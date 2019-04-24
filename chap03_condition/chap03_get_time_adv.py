import time

now = time.localtime()
print("현재 시간은", time.asctime())

if now.tm_mon >= 3 and now.tm_mon <= 5:
    print("따뜻한 봄이네요~")
elif now.tm_mon >= 6 and now.tm_mon <= 8:
    print("더운 여름이네요~")
elif now.tm_mon >= 9 and now.tm_mon <= 11:
    print("청명한 가을이네요~")
else:
    print("추운 겨울이네요~")

if now.tm_hour < 11 :
    print("좋은 아침이에요~")
elif now.tm_hour < 15 :
    print("낮이에요~")
elif now.tm_hour < 20 :
    print("저녁이에요~")
else:
    print("잘 자요~")