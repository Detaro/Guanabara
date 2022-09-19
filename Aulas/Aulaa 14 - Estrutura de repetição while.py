for c in range(1, 10):
    print(c)
print('fim')
c = 1
while c < 10 : # msm resultado q o de cima usando while
    print(c)
    c = c + 1
print('fim')

r = "S"
while r == "S":
    r = str(input('Quer connituar? S/N')).upper()