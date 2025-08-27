#WE LEARN COMPARISION OPERATORS AND IF-ELSE STATEMENT and NESTED IF-ELSE
r_nationality='india'
y_nationality=str(input('your live in which country:'))

have_vpn=1
stdmark=int(input('Please enter'))

if stdmark<=40:
  print('you can play TIKTOK APP because you live in ',y_nationality)

elif 40>=stdmark:

  have_vpn=int(input('if you have vpn write 1 if you not have vpn  0: -->'))
  print(' you can play TIKTOK APP because you have vpn:')
else:
  print(' you cannot play TIKTOK APP because you live in :',y_nationality,' it is band in' ,y_nationality)



