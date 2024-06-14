#V Импортирование рандома в код
import random

#V Урон, кол-во HP и величину отхила
fighter1,fighter2 = 100,100
AT = 100
HEAL = 20

#-------------------------------------------------------------------

print('Введите at, def, heal')

#Просчет шага игрока
while fighter1 >0:
     move = input()
     if move == 'at':
          print('Вы попытались нанести удар.')
     elif move == 'def':
          print('Вы защитились от атаки.')
     elif move == 'heal':
          fighter1 += HEAL
          print('Вы восполнили здоровье на.', HEAL)


#Просчет шага бота
     rand = random.randint(1, 3)
     if rand == 1:
          if move == 'at':
               print('Вы сразились')
               fighter2 -= AT
               fighter1 -= AT
          elif move == 'def':
               print('Вы отразили атаку противника')
     elif rand == 2:
          print('Противник защитился')
     else:
          if move == 'at':
               print('Вы нанесли удар пока противник восполнял HP')
               fighter2 -= AT
               fighter2 += HEAL
          else:
               print('Противник восполнил HP на', HEAL)
               fighter2 += HEAL

     if fighter2 <=0:
          break
     if fighter1 <=0:
          break
     print('Ваше HP =', fighter1, 'Здоровье противника =', fighter2)



#-------------------------------------------------------------------
#Подведение итогов
if fighter2 == fighter1 <= 0:
     print('Победителя нет.')
elif fighter1 <=0:
     print('Вы проиграли битву.')
elif fighter2 <=0:
     print('Вы победили.')