import pprint

n=10
d3 = [[[0 for col in range(n)]for row in range(n)] for x in range(n)]

def rotate(l, n):
    return l[n:] + l[:n]

def shift_and_print():
  i=1;a=[]
  while i<(n+1):
   j=1
   a = d3[i-1][0]
   print('Группа №', i)
   print('Человек №',((i-1)*10+j),' Список столов: ')
   pprint.pprint(a)
   print('')
   while j<(n+1):
     if j==1:
       j = j + 1
       continue
     elif(j>1)and(j<n):
        a[1:n+1] = rotate(a[1:n+1], 1)
        d3[i-1][j-1][1:n+1] = a[1:n+1]
     else:
       print('Человек №',((i-1)*10+j),' Список столов: ')
       pprint.pprint(d3[i-1][n-1])
       j = j + 1
       continue
     print('Человек №',((i-1)*10+j),' Список столов: ')
     pprint.pprint(a)
     j = j + 1
   i = i + 1
   print('_______________________________')
  return 0

def conference():
 i=1
 while i<(n+1):
   j=1
   while j<(n+1):
     d3[i-1][j-1][0] = i
     d3[i-1][n-1][j-1] = i
     if i==1:
       d3[i-1][0][j-1] = j+i-1
     else:
       d3[i-1][0] = rotate(d3[0][0], i-1)
     j = j + 1
   i = i + 1
 shift_and_print()

conference()