calc = input('Введите действие через пробел:  ') # Просим ввести у словие

namber = calc.split() #разделение 

a = int(namber[0]) #Присвоеник к разделам операнд
b = int(namber[2])
c = namber[1]  
print(a,c,b,'будет:')
if len(namber)>3:
    print('Формат данной математической операции не удовлетворяет \n заданию - два операнда и один оператор ( + , - , * , / )')
else:
    if (a > 10 or b > 10):
        print('Ввод только от 0 до 10 включительно!')
    else:
        if len(namber)<3:
            print('т.к. строка не является математической операцией') 
        elif c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c =='*':
            print(a * b)
        elif c== '/':
            print(a // b)
         
     
    # if (len(namber)>3):
    #   print('Формат данной математической операции не удовлетворяет \n заданию - два операнда и один оператор ( + , - , * , / )')
