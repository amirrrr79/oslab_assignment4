n=int(input('Enter n:'))
m=int(input('Enter m:'))

for i in range(1,n+1):
    for j in range(1,m+1):
      multi=i*j
      print(multi,end=' ')
    print()
