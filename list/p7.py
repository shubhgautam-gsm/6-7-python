list=['ram','shyam','jay','rakesh']
flipcart=['laptop','microphone','shoes']

list1=[1,2,3]
print(list1*4)
print(list1+list1+list1+list)
print(5 in list1)
print(2 in list1)

user = input('Enter a name from list : ')
user2 = input('Enter Email : ')
user3 = input('Enter comment : ')

if user in flipcart:
    print('you can buy ',user)

if '@gmail.com' in  user2 :
    print('welcome user ',user2)


if 'non sense' in  user3 :
    print('welcome user ',user3.replace('non sense', '**'))

# list=['ram','shyam','jay','rakesh']
# list1=[1,2,3]
# print(str(input('give name to check to know in list  having or not :')) in list )

