



# 2) გააკეთეთ Reverse List და გამოიყენეთ while loop. შემოაბრუნეთ ყველა რიცხვი ლისტში. 
# ახსნა: [1, 2, 3, 4,  5] => [5, 4, 3, 2, 1]


list1 = [1, 2, 3, 4, 5,]

print(list1)



# 3) გააკეთეთ Filter Even Numbers. მიზანი: გაფილტრეთ ყველრა ლუწი რიცხვი და ჩაამატეთ ახალ სიაში და შემდეგ ეგ სია დაპრინტეთ 


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for i in range(1, 11):
    if i % 2 == 0:
        even_numbers.append(i)
        print(even_numbers)



# 4) გააკეთეთ Find Maximum და გამოიყენეთ for loop. 
# მიზანი: სიაში უნდა იპოვოთ მაქსიმუმი ინტეჯერი მაგალითად: [1, 546, 456 ,123] => [546]


list3 = [1, 33, 55, 23, 100]    

maximum = max(list3)

print(maximum)



# 5) გააკეთეთ Find Minimum და გამოიყენეთ for loop. 
# მიზანი: სიაში უნდა იპოვოთ მინიმალური ინტეჯერი მაგალითად: [1, 546, 456 ,123] => [1]


list4 = [1, 33, 55, 23, 100]

minimum = min(list4)

print(minimum)


# 6) გააკეთეთ Filter Odd Numbers. მიზანი: გაფილტრეთ ყველრა კენტი რიცხვი და ჩაამატეთ ახალ სიაში და შემდეგ ეგ სია დაპრინტეთ


list5 = [23, 24, 11, 777, 210, 489, 2234]

odd_numb = []

for i in range(1, 8):
     if i % 2 != 0:
         odd_numb.append(i)
         print(odd_numb)



# 7) გააკეთეთ Sum Of Even Numbers. 
# მიზანი: შეკრიბეთ ყველა ლუწი რიცხვი და შეინახეთ სიაში შემდეგ ეგ სია დაპრინტეთ 10 ჯერ


list6 = [22, 80, 14, 33, 66, 177]

sum_of_even_numb = 0

for i in range(len(list6)):
    if list6[i] % 2 == 0:
        sum_of_even_numb += list6[i]
print(sum_of_even_numb)



# 8) გააკეთეთ Sum Of Odd Numbers. 
# მიზანი: შეკრიბეთ ყველა კენტი რიცხვი და შეინახეთ სიაში შემდეგ ეგ სია დაპრინტეთ 10 ჯერ



list7 = [22, 80, 14, 33, 66, 177]

sum_of_odd_numb = 0

for i in range(len(list7)):
    if list7[i] % 2 != 0 :
        sum_of_odd_numb += list7[i]
print(sum_of_odd_numb)



# 9)  გააკეთეთ While Loop. 
# ეს loop-ი უნდა გაეშვას 50-ჯერ და ზუსტად 47 loop-ზე უნდა შეჩერდეს loop-ი, 
# თითოეულ loop-ის დატრიალებაზე უნდა დაპრინტოს მერამდენე დატრიალება მოხდა 
# ანუ: Loop 1 Loop 2 Loop 3 და ასე შემდეგ. 
# მინიშნება: შექმენით Counter ცვლადი და მასში შეინახეთ 0 ციფრი ყოველ loop-ის დატრიალებაზე უნდა მოიმატოს ერთით.




    

# Boss Level: გახსენით მაღაზია სახელად PC Parts, სადაც შეგიძლიათ შეიძინოთ სხვადასხვა კომპიუტერული ნაწილი 
# მაგალითად: პროცესორები, ვიდეო ბარათები, ოპერატიული მეხსიერება, კვების ბლოკები, კორპუსები და სხვა. 
# თითოეულ პროდუქტს მიანიჭეთ შესაბამისი ფასი. საბოლოოდ, დაპრინტეთ ჩეკი, სადაც ჩამოთვლილი იქნება შეძენილი ნივთები და ჯამური თანხა. 


product_list = 'video cards: 450', 'operating memory: 120', 'central processing: 440', 'power supply: 300'
product_list2 = 'video cards', 'operating memory', 'central processing', ' power supply'
product1 = 450
product2 = 120
product3 = 440
product4 = 300

cart = []


print('welcome at shop!')

print(product_list)


print('would you like to buy anything')
    

ans1 = input('')


if ans1 != 'yes' and 'no':
    print('sorry, I do not understand, please answer with yes or no.')


elif ans1 == 'yes':
    print('what would you like to buy')
elif ans1 == 'no':
    print('okay')




ans2 = input('')

# if ans2 == product_list2 [0]:
    

print('i would like to buy ' + ans2 )

print('add' + ' ' + ans2  + ' ' + 'in a cart ?')

c = input('')

if c == 'yes':
    cart.append(ans2)
    print(ans2 + " " + 'has been added in your cart.')




if ans2 == 'video cards, operating memory, central processing, power supply.' :
    print('your total is')
    print(product1 + product2 + product3 + product4)
elif ans2 == 'video cards':
    print('your total is ')
    print(product1)
elif ans2 == 'operating memory':
    print('your total is ')
    print(product2)
elif ans2 == 'central processing':
    print('your total is ')
    print(product3)
elif ans2 == 'power supply':
    print('your total is ')
    print(product4)


print('purchase' + cart + '?')

c2 = input('')

if c2 == 'yes':
    print('')