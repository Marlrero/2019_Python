import pickle # 객체를 파일에 쓸 때 사용

movie = { 'superman vs batman': 9.8, 'ironman': 9.6 }

pickle.dump(movie, open('save.p', 'wb')) # 객체는 binary로 저장

readMovie = pickle.load(open('save.p', 'rb')) # 다시 읽어오기
print(readMovie)