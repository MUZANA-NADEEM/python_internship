import random
characters=[ 'a', 'b', 'c', 'd', 'e' ,'f' ,'g' ,'h', 'i', 'j' ,'k' ,'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't' ,'u' ,'v' ,'w' ,'x' ,'y' ,'z ' ,'A' ,'B' ,'C', 'D' ,'E' ,'F', 'G' ,'H' ,'I' ,'J' ,'K' ,'L', 'M', 'N', 'O', 'P' ,'Q' ,'R', 'S' ,'T', 'U' ,'V', 'W' ,'X', 'Y' ,'Z']

digits = ['0','1','2','3','4','5','6','7','8','9']

symbols=['!','@','$','%','&','*','/']
print (" ------ PASSWORD GENERATOR ------------")
number_of_characters=int(input("Enter number of character you want in your password : "))
number_of_digits=int(input("Enter number of numbers you want in your password : "))
number_of_symbols=int(input("Enter number of symbols you want in your password : "))

password=''

for i in range(1,number_of_characters+1):
    letter = random.choice(characters)
    password=password+letter
   
for i in range(1,number_of_digits+1):
    letter = random.choice(digits)
    password=password+letter
   
for i in range(1,number_of_symbols+1):
    letter = random.choice(symbols)
    password=password+letter
   
print(password)
