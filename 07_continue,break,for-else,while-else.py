################################################
# beak 와 continue
################################################
for i in range(0, 10):
    print(i)
    if i > 8 : break
    if i > 5 : continue
    print("5 이하의 값")

################################################
# 반복문에서의 else
################################################
for i in range(0, 5):
    print(i)
else:
    print("반복문 종료")
