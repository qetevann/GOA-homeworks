

#  1) შექმენით ფუნქცია რომელიც მომხმარებელს მიესალმება

def hll():
    print('hello')
    
hll()



#  2) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება სახელს შემდეგ კი მას მიესალმება



def ask_name():
    q1 = input('')
    print(q1 + '! hello')


ask_name()



#  3) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს შემდეგ კი მათ დაუმატებთ ერთმანეთს 


def plus():
    c1 = int(input(''))
    c2 = int(input(''))
    print(c1 + c2)


plus()



#  4) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს შემდეგ კი მათ გამოაკლებს ერთმანეთს 

def minus():
    c3 = int(input(''))
    c4 = int(input(''))
    print(c3 - c4)


minus()



#  5) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს შემდეგ კი მათ გაამრავლებს ერთმანეთზე


def multiply():
    c5 = int(input(''))
    c6 = int(input(''))
    print(c5 * c6)


multiply()



#  6) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს შემდეგ კი მათ გაყოფს ერთმანეთზე 


def division():
    c7 = int( input(''))
    c8 = int(input(''))
    print(c7 / c8)



# 7) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი

def num4 ():
    c9 = int(input(''))
    if c9 % 2 == 0 :
        print('even')
    elif c9 % 2 != 0 :
        print('odd')
    elif c9 < 0:
        print('negative number')
    else:
        print('neither odd or even')


num4()




#  8) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიღხვს შემდეგ კი დაბეჭდავს დადებითია თუ უარყოფითი



def num():
    num6 = int(input(''))
    if num6 > 0:
        print('this number is positive')
    elif num6 < 0:
        print('this number is negative')
    else:
        print('neither negative or positive')

num()




#  9) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ასაკს თუ მისი ასაკი მეტია 18 ზე უთხრას რომ სრულწლოვანია თუარადა არარის


def age():
    ask_age = int(input("what's your age? "))
    if ask_age >= 18:
        print('you are an adult')
    elif ask_age < 18:
        print('you are underaged')

age()



# 10) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა რიცხვს


def random_number():
    rndm_numb = int(input(''))
    for i in range (1, rndm_numb):
        print(i)

random_number()



# 11) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა ლუწ რიცხვს


def random_number2():
    rndm_number2 = int(input(''))
    for i in range(1, rndm_number2):
        if i % 2 == 0 :
            print(i)

random_number2()



# 12) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა კენტ რიცხვს


def random_number3():
    rndm_number3 = int(input(''))
    for i in range(1, rndm_number3):
        if i % 2 != 0:
            print(i)

random_number3()




# 13) შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია შემდეგ კი დაბეჭდავს ამ სიაში არსებული რიცხვების ჯამს


def list():
    list1 = [4584, 12, 11, 77, 34, 90, 2325]
    print(sum(list1))



list()