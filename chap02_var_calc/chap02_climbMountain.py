from math import *

flatStartTime = 10 / 20 # 평지의 거리는 10km이고, 속력은 20km/h
upHillTime = sqrt(3**2 + 4**2) / 10 # 오르막의 거리는 ~이고, 속력은 10km/h
downHillTime = sqrt(3**2 + 4**2) / 30 # 내리막의 거리는 ~이고, 속력은 30km/h
flatEndTime = 8 / 20 # 평지의 거리는 8km이고, 속력은 20km/h

print("자전거로 주행한 총 주행 시간:", flatStartTime + upHillTime + downHillTime + flatEndTime)
