# recursion을 이용한 directory size 계산
import os

def calcDirSize(name):
    totalSize = 0

    if os.path.isfile(name): # 파일이면
        totalSize += os.path.getSize(name)
    else:
        fileList = os.listdir(name) # 서브 디렉터리들에 대해
        for subDir in fileList: # 서브 디렉터리 하나씩
            totalSize += calcDirSize(name + "\\" + subDir)

    return totalSize

name = input("디렉터리 이름을 입혁하시오:")
print(calcDirSize(name))