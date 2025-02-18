


from turtle import *


# 1 rectangle


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)



for i in range(4):
    
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)



# 4 rectangle



forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)




# 2) შექმენით 4 სხვადასხვა ფუნქცია ერთი მიმატების მეორე გამოკლების მესამე გამრავლების მეოთხე გაყოფის, 
# თითოეულ ფუნქციაში უნდა მოხდეს შესაბამისი მოქმედება ორ რიცხვს შორის, 
# მაგ. მეტობის ფუნქციაში უნად დაიბეჭდოს ნებისმიერი ორი რიცხვის ჯამი, 
# გამრავლების ფუნქციაში ნებისმიერი ორი რიცხვი ნამრავლი და ასე შემდეგ საბოლოოდ გამოიძხეთ ყველა ფუნქცია



def add_num():
    print(c + c2)
    c = int(input(''))
    c2 = int(input(''))


add_num()

def subt_num():
    print(c3 + c4)
    c3 = int(input(''))
    c4 = int(input(''))

subt_num()

def mult_num():
    print(c5 + c6)

    c5 = int(input(''))
    c6 = int(input(''))
   
mult_num()

def dev_num():
    c7 = int(input(''))
    c8 = int(input(''))

    print(c7 + c8)
    
dev_num()

exitonclick()