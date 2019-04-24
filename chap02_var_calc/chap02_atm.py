itemPrice = int(input("물건값을 입력하시오: "))
coin1000 = int(input("1000원 지폐개수: "))
coin500 = int(input("500원 지폐개수: "))
coin100 = int(input("100원 지폐개수: "))

# 줘야 할 거스름돈
charge = coin1000 * 1000 + coin500 * 500 + coin100 * 100 - itemPrice

return500 = charge // 500
charge = charge % 500

return100 = charge // 100
charge = charge % 100

return10 = charge // 10
charge = charge % 10

return1 = charge

print("500원 = %d 100원 = %d 10원 = %d 1원 = %d" %(return500, return100, return10, return1))