sayi = int(input ("satir sayisi giriniz:"))
if(int(sayi)%2 == 0):
 for i in range (1, sayi+1): 
   print (" "*(sayi -i),"*"*(i*2-1))


else:
  for i in range (1, sayi+1): 
   
   print(" "*(sayi -i),"*"*(i*2-1))
  
  for j in range(1,sayi+1):
   
   print(" "*(j),"*"*((sayi-j)*2-1))


