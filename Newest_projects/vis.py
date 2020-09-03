import pygame
import sys
from pygame.locals import *
import csv
import pandas as pd
import statistics as s
import random as r
import textwrap
    
# num_cars = int(input("How many cars do you want to try to fit the reservations into " ))
# num_res = int(input(" How many People are reserving?"))
# y = int(input("How many hours in advance can people book? (Random Start Time)"))
# z = int(input("How many hours can people reserve a car for? (Random Length of Reservation)"))
# number_hours = int(input("How many hours do you want to be included in the trial? (Chart Width must be larger than the number of hours in advance)"))

num_cars = 39
num_res = 99
y = 50
z = 20
number_hours = 70
##
st = []
nh = []   
index = []
car_type = ['a','b','c','d']
garage = ['1', '2', '3', '4']
ct =[]
ct1 = []
g = []
##
st1 = []
nh1 = []
index1 = []
ct2 = []
garage1 = ['1', '2', '3', '4']
g1 = []
s= []
##
st2 = []
nh2 = []
ct2 = []
g2 = []
##
st3 = []
nh3 = []
ct3 = []
g3 = []
##
st4 = []
nh4 = []
ct4 = []
g4 = []
##
st5 = []
nh5 = []
ct5 = []
g5 = []
##
st6 = []
nh6 = []
ct6 = []
g6 = []
##
st7 = []
nh7 = []
ct7 = []
g7 = []
##
cartype = ['a','a','a','a','a','a','a','a','a','a','b','b','b','b','b','b','b','b','b','b','c','c','c','c','c','c','c','c','c','d','d','d','d','d','d','d','d','d','d']
##
pygame.init()
BLACK =   (0,   0,   0)
WHITE = (255, 255, 255)
BLUE =   (73,   124, 150)
GREEN =   (0, 153,   76)
PINK =   (200,   155,   200)
GRAY = (200, 200, 200)
LIGHT_BLUE =(102, 178, 255)
LIGHT_GREEN = (150, 220, 179)
YELLOW = (255,255,0)
DARK_GRAY = (120,120,120)
DARK_BLUE = (0,0,255)
BLUE2 = (25,10,112)
BLUE3 = (33,191,194)
width= 1700
height = 1080
SIZE = (width, height)
##
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
pygame.display.update()
pygame.display.set_caption("Rental Request Sort")


for i in range(num_res):
    TYPE_OF_CAR = r.choice(car_type)
    RANDOM_START_TIME = r.randint(1,(y))
    NUMBER_OF_HOURS = r.randint(1,(z))
    garage_type = r.choice(garage)
    st.append(RANDOM_START_TIME)
    nh.append(NUMBER_OF_HOURS)
    index.append(i)
    ct.append(TYPE_OF_CAR)
    g.append(garage_type)
    s.append('0')

for i in range(num_res):
    TYPE_OF_CAR1 = r.choice(car_type)
    RANDOM_START_TIME1 = r.randint(1,(y))
    NUMBER_OF_HOURS1 = r.randint(1,(z))
    garage_type1 = r.choice(garage1)
    st1.append(RANDOM_START_TIME1)
    nh1.append(NUMBER_OF_HOURS1)
    index1.append(i)
    ct1.append(TYPE_OF_CAR1)
    g1.append(garage_type1)
    
for i in range(num_res):
    TYPE_OF_CAR = r.choice(car_type)
    RANDOM_START_TIME = r.randint(1,(y))
    NUMBER_OF_HOURS = r.randint(1,(z))
    garage_type1 = r.choice(garage1)
    st2.append(RANDOM_START_TIME)
    nh2.append(NUMBER_OF_HOURS)
    ct2.append(TYPE_OF_CAR)
    g2.append(garage_type1)   
    
for i in range(num_res):
    TYPE_OF_CAR = r.choice(car_type)
    RANDOM_START_TIME = r.randint(1,(y))
    NUMBER_OF_HOURS = r.randint(1,(z))
    garage_type1 = r.choice(garage1)
    st3.append(RANDOM_START_TIME)
    nh3.append(NUMBER_OF_HOURS)
    ct3.append(TYPE_OF_CAR)
    g3.append(garage_type1)  
    
for i in range(num_res):
    TYPE_OF_CAR = r.choice(car_type)
    RANDOM_START_TIME = r.randint(1,(y))
    NUMBER_OF_HOURS = r.randint(1,(z))
    garage_type1 = r.choice(garage1)
    st4.append(RANDOM_START_TIME)
    nh4.append(NUMBER_OF_HOURS)
    ct4.append(TYPE_OF_CAR)
    g4.append(garage_type1)  
    
for i in range(num_res):
    TYPE_OF_CAR = r.choice(car_type)
    RANDOM_START_TIME = r.randint(1,(y))
    NUMBER_OF_HOURS = r.randint(1,(z))
    garage_type1 = r.choice(garage1)
    st5.append(RANDOM_START_TIME)
    nh5.append(NUMBER_OF_HOURS)
    ct5.append(TYPE_OF_CAR)
    g5.append(garage_type1)  
    
for i in range(num_res):
    TYPE_OF_CAR = r.choice(car_type)
    RANDOM_START_TIME = r.randint(1,(y))
    NUMBER_OF_HOURS = r.randint(1,(z))
    garage_type1 = r.choice(garage1)
    st6.append(RANDOM_START_TIME)
    nh6.append(NUMBER_OF_HOURS)
    ct6.append(TYPE_OF_CAR)
    g6.append(garage_type1)  
    
for i in range(num_res):
    TYPE_OF_CAR = r.choice(car_type)
    RANDOM_START_TIME = r.randint(1,(y))
    NUMBER_OF_HOURS = r.randint(1,(z))
    garage_type1 = r.choice(garage1)
    st7.append(RANDOM_START_TIME)
    nh7.append(NUMBER_OF_HOURS)
    ct7.append(TYPE_OF_CAR)
    g7.append(garage_type1)  
    
# print(st, nh, index, ct, g)

dat = pd.DataFrame(
{'Start': st,
    'Number_hours' : nh,
    'ID' : index,
    'Type' : ct, 
    'Garage' : g,
    'Status' : s
})

second_dataset = pd.DataFrame(
    {'Start': st1,
     'Number_hours' : nh1,
     'ID' : index1,
     'Type' : ct1,
     'Garage' : g1,
     'Status' : s
     
})


g2_data = pd.DataFrame(
    {'Start': st2,
     'Number_hours' : nh2,
     'ID' : index1,
     'Type' : ct2,
     'Garage' : g2,
     'Status' : s
     
})

g2_second_data = pd.DataFrame(
    {'Start': st3,
     'Number_hours' : nh3,
     'ID' : index1,
     'Type' : ct3,
     'Garage' : g3,
     'Status' : s
     
})

g3_data = pd.DataFrame(
    {'Start': st4,
     'Number_hours' : nh4,
     'ID' : index1,
     'Type' : ct4,
     'Garage' : g4,
     'Status' : s
     
})

g3_second_data = pd.DataFrame(
    {'Start': st5,
     'Number_hours' : nh5,
     'ID' : index1,
     'Type' : ct5,
     'Garage' : g5,
     'Status' : s
     
})

g4_data = pd.DataFrame(
    {'Start': st6,
     'Number_hours' : nh6,
     'ID' : index1,
     'Type' : ct6,
     'Garage' : g6,
     'Status' : s
     
})

g4_second_data = pd.DataFrame(
    {'Start': st7,
     'Number_hours' : nh7,
     'ID' : index1,
     'Type' : ct7,
     'Garage' : g7,
     'Status' : s
     
})


data_chart=dat.sort_values(by =['Start'])
data_chart2 = second_dataset.sort_values(by = ['Start'])    
garage2_data = g2_data.sort_values(by = ['Start'])
garage2_seconddata = g2_second_data.sort_values(by= ['Start'])
garage3_data = g3_data.sort_values(by = ['Start'])
garage3_seconddata = g3_second_data.sort_values(by= ['Start'])
garage4_data = g4_data.sort_values(by = ['Start'])
garage4_seconddata = g4_second_data.sort_values(by= ['Start'])




columns = []
count = 0
for number in range(number_hours):
    count +=1
    columns.append(count)
    
for num in range(num_res):
    car_type2 = r.choice(car_type)
    ct1.append(car_type2)
    datf1 = pd.DataFrame ({
        "Type": cartype
    })
    datf2 = pd.DataFrame ({
        "Type" : cartype
    })
    garage2 = pd.DataFrame ({
        "Type": cartype
    })
    garage3 = pd.DataFrame ({
        "Type": cartype
    })
    garage4 = pd.DataFrame ({
        "Type": cartype
    })
    
for col in range(count):
    datf1[col] = -1
    datf2[col] = -1
    garage2[col] = -1
    garage3[col] = -1
    garage4[col] = -1
    
df1 = datf1.sort_values(by = ['Type'])
df2 = datf2.sort_values(by = ['Type'])
g2 = garage2.sort_values(by = ['Type'])
g3 = garage3.sort_values(by = ['Type'])
g4 = garage4.sort_values(by = ['Type'])
    
# print(df1)


grid = []
for row in range(num_res):
    grid.append([])
    for column in range(number_hours):
        grid[row].append(0)   
        

def __main__():
    
    def new_res_g1c1():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '1'
        TYP = 'a'

        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        print(new_res_g1c1)
        for i in range(new_resv):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if df1.iloc[Cars,Start_Slot] == -1 and df1.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if df1.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            df1.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
                                                (MARGIN + HEIGHT) * Cars + MARGIN,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * Cars + MARGIN))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
    def new_res_g1c2():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        TYPE_OF_CAR = 'b'
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = '1'
        st8.append(RANDOM_START_TIME)
        index.append('1')
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv1):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if df1.iloc[Cars,Start_Slot] == -1 and df1.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if df1.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            df1.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
                                                (MARGIN + HEIGHT) * Cars + MARGIN,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * Cars + MARGIN))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass  
    def new_res_g1c3():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        TYPE_OF_CAR = 'c'
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = '1'
        st8.append(RANDOM_START_TIME)
        index.append('1')
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv2):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if df1.iloc[Cars,Start_Slot] == -1 and df1.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if df1.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            df1.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
                                                (MARGIN + HEIGHT) * Cars + MARGIN,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * Cars + MARGIN))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
    def new_res_g1c4():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        TYPE_OF_CAR = 'd'
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = '1'
        st8.append(RANDOM_START_TIME)
        index.append('1')
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv3):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if df1.iloc[Cars,Start_Slot] == -1 and df1.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if df1.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            df1.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
                                                (MARGIN + HEIGHT) * Cars + MARGIN,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * Cars + MARGIN))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
    
    def new_res_g2c1():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '2'
        TYP = 'a'

        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv4):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g2.iloc[Cars,Start_Slot] == -1 and g2.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g2.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g2.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+950,
                                                (MARGIN + HEIGHT) * Cars + MARGIN,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+950 ,(MARGIN + HEIGHT) * Cars + MARGIN))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass                 
    def new_res_g2c2():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '2'
        TYP = 'b'

        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv5):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g2.iloc[Cars,Start_Slot] == -1 and g2.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g2.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g2.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+950,
                                                (MARGIN + HEIGHT) * Cars + MARGIN,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+950 ,(MARGIN + HEIGHT) * Cars + MARGIN))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
    def new_res_g2c3():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '2'
        TYP = 'c'

        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv6):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g2.iloc[Cars,Start_Slot] == -1 and g2.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g2.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g2.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+950,
                                                (MARGIN + HEIGHT) * Cars + MARGIN,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+950 ,(MARGIN + HEIGHT) * Cars + MARGIN))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
    def new_res_g2c4():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '2'
        TYP = 'd'

        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv7):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g2.iloc[Cars,Start_Slot] == -1 and g2.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g2.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g2.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+950,
                                                (MARGIN + HEIGHT) * Cars + MARGIN,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+950 ,(MARGIN + HEIGHT) * Cars + MARGIN))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
                    
    def new_res_g3c1():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '3'
        TYP = 'a'

        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv8):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g3.iloc[Cars,Start_Slot] == -1 and g3.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g3.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g3.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
                                                (MARGIN + HEIGHT) * Cars + MARGIN +500,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * Cars + MARGIN+500))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass                
    def new_res_g3c2():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '3'
        TYP = 'b'
        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv9):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g3.iloc[Cars,Start_Slot] == -1 and g3.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g3.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g3.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
                                                (MARGIN + HEIGHT) * Cars + MARGIN + 500,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * Cars + MARGIN+500) )
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
    def new_res_g3c3():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '3'
        TYP = 'c'
        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv10):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g3.iloc[Cars,Start_Slot] == -1 and g3.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g3.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g3.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
                                                (MARGIN + HEIGHT) * Cars + MARGIN + 500,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * Cars + MARGIN+500) )
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
    def new_res_g3c4():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '3'
        TYP = 'd'
        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv11):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g3.iloc[Cars,Start_Slot] == -1 and g3.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g3.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g3.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
                                                (MARGIN + HEIGHT) * Cars + MARGIN + 500,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * Cars + MARGIN+500) )
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
    
    def new_res_g4c1():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '4'
        TYP = 'a'
        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv12):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g4.iloc[Cars,Start_Slot] == -1 and g4.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g4.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g4.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+950,
                                                (MARGIN + HEIGHT) * Cars + MARGIN + 500,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+950 ,(MARGIN + HEIGHT) * Cars + MARGIN+500) )
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
    def new_res_g4c2():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '4'
        TYP = 'b'
        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv13):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g4.iloc[Cars,Start_Slot] == -1 and g4.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g4.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g4.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+950,
                                                (MARGIN + HEIGHT) * Cars + MARGIN + 500,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+950 ,(MARGIN + HEIGHT) * Cars + MARGIN+500) )
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
    def new_res_g4c3():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '4'
        TYP = 'c'
        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv14):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g4.iloc[Cars,Start_Slot] == -1 and g4.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g4.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g4.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+950,
                                                (MARGIN + HEIGHT) * Cars + MARGIN + 500,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+950 ,(MARGIN + HEIGHT) * Cars + MARGIN+500) )
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
    def new_res_g4c4():
        st8 = []
        nh8 = []
        ct8 = []
        g8 = []
        s= []
        index = []
        new_res = 0
        GT = '4'
        TYP = 'd'
        TYPE_OF_CAR = TYP
        RANDOM_START_TIME = r.randint(1,(y))
        NUMBER_OF_HOURS = r.randint(1,(z))
        garage_type1 = GT
        st8.append(RANDOM_START_TIME)
        index.append("1")
        nh8.append(NUMBER_OF_HOURS)
        ct8.append(TYPE_OF_CAR)
        g8.append(garage_type1)  
        s.append('0')
        new_res = pd.DataFrame(
        {'Start': st8,
        'Number_hours' : nh8,
        'ID' : index,
        'Type' : ct8,
        'Garage' : g8,
        'Status' : s})
        print(new_res)
        function.count_num = 0
        failure_count = 0
        total_scheduled = 0
        for i in range(new_resv15):
            Success = False
            Start_Slot = new_res.iloc[i,0]
            Number_of_Slots = new_res.iloc[i,1]
            Res_ID = new_res.iloc[i,2]
            type_of_car = new_res.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g4.iloc[Cars,Start_Slot] == -1 and g4.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g4.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                    

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g4.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                        
                    
                    
                            pygame.draw.rect(screen,
                                                BLUE3,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+950,
                                                (MARGIN + HEIGHT) * Cars + MARGIN + 500,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+950 ,(MARGIN + HEIGHT) * Cars + MARGIN+500) )
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
        
    data_gen ='GENERATE DATA'
    
    
    font = pygame.font.SysFont("Arial",10)
    font1 = pygame.font.SysFont("Arial", 18)
    font0 = pygame.font.SysFont("Arial", 12)
    font9 = pygame.font.SysFont("Arial", 8)
    clock = pygame.time.Clock()
    MARGIN = 2.5
    pygame.display.update()
    clock.tick(60)
    WIDTH = 8
    HEIGHT = 10
    screen.fill(WHITE)

    for row in range(num_cars):
        color = GRAY
        for column in range(number_hours):
            pygame.draw.rect(screen,
                            color,
                        [((MARGIN + WIDTH) * column + MARGIN)+950,
                        (MARGIN + HEIGHT) * row + MARGIN,
                        WIDTH,
                        HEIGHT])
                
    for row in range(num_cars):
            color = GRAY
            for column in range(number_hours):
                pygame.draw.rect(screen,
                                color,
                            [((MARGIN + WIDTH) * column + MARGIN)+200,
                            (MARGIN + HEIGHT) * row + MARGIN+500,
                            WIDTH,
                            HEIGHT])

    for row in range(num_cars):
            color = GRAY
            for column in range(number_hours):
                pygame.draw.rect(screen,
                                color,
                            [((MARGIN + WIDTH) * column + MARGIN)+950,
                            (MARGIN + HEIGHT) * row + MARGIN+500,
                            WIDTH,
                            HEIGHT])
    for row in range(num_cars):
        color = GRAY
        for column in range(number_hours):
            pygame.draw.rect(screen,
                        color,
                        [((MARGIN + WIDTH) * column + MARGIN)+200,
                        (MARGIN + HEIGHT) * row + MARGIN,
                        WIDTH,
                        HEIGHT])
                
    input_rect1 = pygame.draw.rect(screen,
                    BLUE,
                    [5,
                    0,
                    195,
                    40])    

    input_rect3 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    50,
                    195,
                    25])    
    
    input_rect4 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    80,
                    195,
                    25])    
    
    input_rect5 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    110,
                    195,
                    25])
    input_rect6 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    140,
                    195,
                    25])     
    
    rectangle = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    170,
                    195,
                    25])
    rectangle1 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    200,
                    195,
                    25])
    rectangle2 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    230,
                    195,
                    25])
    rectangle3 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    260,
                    195,
                    25])
    rectangle4 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    290,
                    195,
                    25])
    rectangle5 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    320,
                    195,
                    25])
    rectangle6 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    350,
                    195,
                    25])
    rectangle7 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    380,
                    195,
                    25])
    rectangle8 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    410,
                    195,
                    25])
    rectangle9 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    440,
                    195,
                    25])
    rectangle10 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    470,
                    195,
                    25])
    rectangle11 = pygame.draw.rect(screen,
                    DARK_GRAY,
                    [5,
                    500,
                    195,
                    25])
    rectangle12 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        530,
                        195,
                        40])
            
        
    input_rect9 = pygame.draw.rect(screen,
                     DARK_GRAY,
                     [5,
                     750,
                     195,
                     72.5])  
    data_button = pygame.draw.rect(screen,
                     BLUE2,
                     [5,
                      827.5,
                      195,
                      36.25]) 
    data_button2 = pygame.draw.rect(screen,
                     BLUE2,
                     [5,
                      868.75,
                      195,
                      36.25])  
    Line1 = pygame.draw.rect(screen,
                     BLACK,
                     [200,
                      125,
                      1800,
                      2.5])   
    Line2 = pygame.draw.rect(screen,
                    BLACK,
                    [200,
                    250,
                    1800,
                    2.5])   
    Line3 = pygame.draw.rect(screen,
                    BLACK,
                    [200,
                    363,
                    1800,
                    2.5])      
    Line4 = pygame.draw.rect(screen,
                                 BLACK,
                                 [0,
                                  165,
                                  200,
                                  5])
    Line5 = pygame.draw.rect(screen,
                                BLACK,
                                [0,
                                285,
                                200,
                                5])
    Line6 = pygame.draw.rect(screen,
                                BLACK,
                                [0,
                                405,
                                200,
                                5])
    Line7 = pygame.draw.rect(screen,
                     BLACK,
                     [200,
                      625,
                      1800,
                      2.5])   
    Line8 = pygame.draw.rect(screen,
                    BLACK,
                    [200,
                    750,
                    1800,
                    2.5])   
    Line9 = pygame.draw.rect(screen,
                    BLACK,
                    [200,
                    863,
                    1800,
                    2.5])  
    
    
    count = 0
    count1= -1
    
    col_list= ['Start', 'Number_hours', 'ID', 'Type', 'Garage', 'Status']
    df = pd.read_csv("algorithm.csv", usecols= col_list)
    

    
    for i in range (number_hours-1):
        count += 1    
        # screen.blit(font.render(str(df.iloc[i,0]),True,(0,0,0)),(((MARGIN +4 ) * 1 )+200,(((HEIGHT + MARGIN) * count)+5) * 1 ))    

        for i in range(number_hours):
            count1 +=1 
            screen.blit(font9.render(str(count),True,(0,0,0)),((((MARGIN +WIDTH ) * count)+4 )+200,(((HEIGHT ) * 1)-8) * 1 ))
            screen.blit(font9.render(str(count),True,(0,0,0)),((((MARGIN +WIDTH ) * count)+204 ),((HEIGHT -8+500  ))))                                              
            screen.blit(font9.render(str(count),True,(0,0,0)),((((MARGIN +WIDTH ) * count)+954 ),((HEIGHT -8 +500 ))))                                             
            screen.blit(font9.render(str(count),True,(0,0,0)),((((MARGIN +WIDTH ) * count)+954 ),((HEIGHT -8  ))))
            
    
    
    total_slots = number_hours * num_cars
            
    state = True
    def function():
        col_list= ['Start', 'Number_hours', 'ID', 'Type', 'Garage', 'Status']
        df = pd.read_csv("algorithm.csv", usecols= col_list)
        

        function.count_num = 0
        
        failure_count = 0
        total_scheduled = 0
        for i in range(num_res):
            Success = False
            Start_Slot = df.iloc[i,0]
            Number_of_Slots = df.iloc[i,1]
            Res_ID = df.iloc[i,2]
            type_of_car = df.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if df1.iloc[Cars,Start_Slot] == -1 and df1.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if df1.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                        car_color = BLUE
                        if Cars % 2 == 0:
                            car_color = BLUE 
                            if car_slots > 0 and df2.iloc[Cars,Start_Slot - 1] == 1:
                                car_color = PINK  #2                      
                        else:
                            car_color = GREEN 
                            if car_slots > 0 and df2.iloc[Cars,Start_Slot - 1] == 3:
                                car_color = LIGHT_GREEN #4

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            df1.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                            if car_color == BLUE:
                                df2.iloc[Cars,car_slots] = 1
                            elif car_color == PINK:
                                df2.iloc[Cars,car_slots] = 2
                            elif car_color == GREEN:
                                df2.iloc[Cars,car_slots] = 3
                            elif car_color == LIGHT_GREEN:
                                df2.iloc[Cars,car_slots] = 4
                        
                    
                    
                            pygame.draw.rect(screen,
                                                car_color,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
                                                (MARGIN + HEIGHT) * Cars + MARGIN,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * Cars + MARGIN))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
                
                
                            #print (Success) #No, I cannot Schedule this car
            # if Success == False:
            #     for car_slots in range(Start_Slot, Start_Slot+Number_of_Slots):
            #         pygame.draw.rect(screen,
            #                         PINK,
            #                         [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
            #                         (MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN,
            #                         ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
            #                         HEIGHT])
            #         screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #         screen.blit(font.render(str(type_of_car),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+193 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #     failure_count+=1                
        print("Total number of people successfully scheduled:" , total_scheduled)
        print('Ratio of filled to non-filled slots:', function.count_num/ total_slots)
        num_scheduled = "successfully scheduled"
        text_surface6 = font1.render(str(num_scheduled), True, BLACK)
        text_surface5 = font1.render(str(total_scheduled), True, BLACK)
        screen.blit(text_surface5, (rectangle12.x+5, rectangle12.y +5+18))
        screen.blit(text_surface6, (rectangle12.x +5, rectangle12.y+5))
        
    def garage2_function():
        col_list= ['Start', 'Number_hours', 'ID', 'Type', 'Garage', 'Status']
        df = pd.read_csv("garage2_data.csv", usecols= col_list)
        

        
        failure_count = 0
        total_scheduled = 0
        for i in range(num_res):
            Success = False
            Start_Slot = df.iloc[i,0]
            Number_of_Slots = df.iloc[i,1]
            Res_ID = df.iloc[i,2]
            type_of_car = df.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g2.iloc[Cars,Start_Slot] == -1 and g2.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g2.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                        car_color = BLUE
                        if Cars % 2 == 0:
                            car_color = BLUE 
                            if car_slots > 0 and df2.iloc[Cars,Start_Slot - 1] == 1:
                                car_color = PINK  #2                      
                        else:
                            car_color = GREEN 
                            if car_slots > 0 and df2.iloc[Cars,Start_Slot - 1] == 3:
                                car_color = LIGHT_GREEN #4

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g2.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                            if car_color == BLUE:
                                df2.iloc[Cars,car_slots] = 1
                            elif car_color == PINK:
                                df2.iloc[Cars,car_slots] = 2
                            elif car_color == GREEN:
                                df2.iloc[Cars,car_slots] = 3
                            elif car_color == LIGHT_GREEN:
                                df2.iloc[Cars,car_slots] = 4
                        
                    
                    
                            pygame.draw.rect(screen,
                                                car_color,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+950,
                                                (MARGIN + HEIGHT) * Cars + MARGIN,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+950 ,(MARGIN + HEIGHT) * Cars + MARGIN))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
                
                
                            #print (Success) #No, I cannot Schedule this car
            # if Success == False:
            #     for car_slots in range(Start_Slot, Start_Slot+Number_of_Slots):
            #         pygame.draw.rect(screen,
            #                         PINK,
            #                         [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
            #                         (MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN,
            #                         ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
            #                         HEIGHT])
            #         screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #         screen.blit(font.render(str(type_of_car),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+193 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #     failure_count+=1                
        print("Total number of people successfully scheduled:" , total_scheduled)
        print('Ratio of filled to non-filled slots:', function.count_num/ total_slots)
        num_scheduled = "successfully scheduled"
        text_surface6 = font1.render(str(num_scheduled), True, BLACK)
        text_surface5 = font1.render(str(total_scheduled), True, BLACK)
        screen.blit(text_surface5, (rectangle12.x+5, rectangle12.y +5+18))
        screen.blit(text_surface6, (rectangle12.x +5, rectangle12.y+5))
    
    def garage2_second_data():
        col_list= ['Start', 'Number_hours', 'ID', 'Type', 'Garage', 'Status']
        df = pd.read_csv("garage2_data.csv", usecols= col_list)
        second_df = pd.read_csv("garage2_second_data.csv", usecols = col_list)
        t = df.append(second_df)
        
        result = t.sort_values(by = ['Start'])
        columns = []
        count = 0
        for number in range(number_hours):
            count +=1
            columns.append(count)
            
        for num in range(num_res):
            car_type2 = r.choice(car_type)
            ct1.append(car_type2)
            datf8 = pd.DataFrame ({
                "Type": cartype
            })
            datf9 = pd.DataFrame ({
                "Type" : cartype
            })
            
        for col in range(count):
            datf8[col] = -1
            datf9[col] = -1

        df8 = datf8.sort_values(by = ['Type'])
        
        df9 = datf9.sort_values(by = ['Type'])
        
        count_num1 = 0
        scheduled = 0
        failure_count = 0
        for i in range(num_res * 2):
            Success = False
            Start_Slot = result.iloc[i,0]
            Number_of_Slots = result.iloc[i,1]
            Res_ID = result.iloc[i,2]
            type_of_car = result.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if df8.iloc[Cars,Start_Slot] == -1 and df8.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
                    #print (df8.iloc[Cars])
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        # print   (df8.iloc[Cars,car_slots])
                        if df8.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                        
                        scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                        car_color = BLUE
                        if Cars % 2 == 0:
                            car_color = BLUE 
                            if car_slots > 0 and df9.iloc[Cars,Start_Slot - 1] == 1:
                                car_color = PINK  #2                      
                        else:
                            car_color = GREEN 
                            if car_slots > 0 and df9.iloc[Cars,Start_Slot - 1] == 3:
                                car_color = LIGHT_GREEN #4

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            df8.iloc[Cars,car_slots] = Res_ID
                            count_num1 += 1
                            if car_color == BLUE:
                                df9.iloc[Cars,car_slots] = 1
                            elif car_color == PINK:
                                df9.iloc[Cars,car_slots] = 2
                            elif car_color == GREEN:
                                df9.iloc[Cars,car_slots] = 3
                            elif car_color == LIGHT_GREEN:
                                df9.iloc[Cars,car_slots] = 4
                          
                        
                        pygame.draw.rect(screen,
                                            car_color,
                                            [((MARGIN + WIDTH) * Start_Slot + MARGIN)+950,
                                            (MARGIN + HEIGHT) * Cars + MARGIN,
                                            ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                            HEIGHT])
                        screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+950 ,(MARGIN + HEIGHT) * Cars + MARGIN))
                        pygame.time.delay(10)
                        pygame.display.update()
                        
                        
                        break
                    elif Success == False:
                        pass
                            #print (Success) #No, I cannot Schedule this car
                else:
                    Success = False
                    #failed to find empty start slot
            # if Success == False:
            #     for car_slots in range(Start_Slot, Start_Slot+Number_of_Slots):
            #         pygame.draw.rect(screen,
            #                         PINK,
            #                         [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
            #                         (MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN,
            #                         ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
            #                         HEIGHT])
            #         screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #         screen.blit(font.render(str(type_of_car),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+193 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #     failure_count+=1
        # print(df8)
        ratio = (count_num1 )/ total_slots
        print("Total number of people successfully scheduled:" , scheduled)
        print('Ratio of filled to non-filled slots:', ratio)
        print("Number failed =", failure_count)
    
    def garage3_function():
        col_list= ['Start', 'Number_hours', 'ID', 'Type', 'Garage', 'Status']
        df = pd.read_csv("garage3_data.csv", usecols= col_list)
        

        function.count_num = 0
        
        failure_count = 0
        total_scheduled = 0
        for i in range(num_res):
            Success = False
            Start_Slot = df.iloc[i,0]
            Number_of_Slots = df.iloc[i,1]
            Res_ID = df.iloc[i,2]
            type_of_car = df.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g3.iloc[Cars,Start_Slot] == -1 and g3.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g3.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                        car_color = BLUE
                        if Cars % 2 == 0:
                            car_color = BLUE 
                            if car_slots > 0 and df2.iloc[Cars,Start_Slot - 1] == 1:
                                car_color = PINK  #2                      
                        else:
                            car_color = GREEN 
                            if car_slots > 0 and df2.iloc[Cars,Start_Slot - 1] == 3:
                                car_color = LIGHT_GREEN #4

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g3.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                            if car_color == BLUE:
                                df2.iloc[Cars,car_slots] = 1
                            elif car_color == PINK:
                                df2.iloc[Cars,car_slots] = 2
                            elif car_color == GREEN:
                                df2.iloc[Cars,car_slots] = 3
                            elif car_color == LIGHT_GREEN:
                                df2.iloc[Cars,car_slots] = 4
                        
                    
                    
                            pygame.draw.rect(screen,
                                                car_color,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
                                                (MARGIN + HEIGHT) * Cars + MARGIN +500,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN+200) ,(MARGIN + HEIGHT) * Cars + MARGIN+500))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
                
                
                            #print (Success) #No, I cannot Schedule this car
            # if Success == False:
            #     for car_slots in range(Start_Slot, Start_Slot+Number_of_Slots):
            #         pygame.draw.rect(screen,
            #                         PINK,
            #                         [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
            #                         (MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN,
            #                         ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
            #                         HEIGHT])
            #         screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #         screen.blit(font.render(str(type_of_car),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+193 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #     failure_count+=1                
        print("Total number of people successfully scheduled:" , total_scheduled)
        print('Ratio of filled to non-filled slots:', function.count_num/ total_slots)
        num_scheduled = "successfully scheduled"
        text_surface6 = font1.render(str(num_scheduled), True, BLACK)
        text_surface5 = font1.render(str(total_scheduled), True, BLACK)
        screen.blit(text_surface5, (rectangle12.x+5, rectangle12.y +5+18))
        screen.blit(text_surface6, (rectangle12.x +5, rectangle12.y+5))
    
    def garage3_second_data():
        
        col_list= ['Start', 'Number_hours', 'ID', 'Type', 'Garage', 'Status']
        df = pd.read_csv("garage3_data.csv", usecols= col_list)
        second_df = pd.read_csv("garage3_second_data.csv", usecols = col_list)
        t = df.append(second_df)
        
        result = t.sort_values(by = ['Start'])
        columns = []
        count = 0
        for number in range(number_hours):
            count +=1
            columns.append(count)
            
        for num in range(num_res):
            car_type2 = r.choice(car_type)
            ct1.append(car_type2)
            datf8 = pd.DataFrame ({
                "Type": cartype
            })
            datf9 = pd.DataFrame ({
                "Type" : cartype
            })
            
        for col in range(count):
            datf8[col] = -1
            datf9[col] = -1

        df8 = datf8.sort_values(by = ['Type'])
        
        df9 = datf9.sort_values(by = ['Type'])
        
        count_num1 = 0
        scheduled = 0
        failure_count = 0
        for i in range(num_res * 2):
            Success = False
            Start_Slot = result.iloc[i,0]
            Number_of_Slots = result.iloc[i,1]
            Res_ID = result.iloc[i,2]
            type_of_car = result.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if df8.iloc[Cars,Start_Slot] == -1 and df8.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
                    #print (df8.iloc[Cars])
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        # print   (df8.iloc[Cars,car_slots])
                        if df8.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                        
                        scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                        car_color = BLUE
                        if Cars % 2 == 0:
                            car_color = BLUE 
                            if car_slots > 0 and df9.iloc[Cars,Start_Slot - 1] == 1:
                                car_color = PINK  #2                      
                        else:
                            car_color = GREEN 
                            if car_slots > 0 and df9.iloc[Cars,Start_Slot - 1] == 3:
                                car_color = LIGHT_GREEN #4

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            df8.iloc[Cars,car_slots] = Res_ID
                            count_num1 += 1
                            if car_color == BLUE:
                                df9.iloc[Cars,car_slots] = 1
                            elif car_color == PINK:
                                df9.iloc[Cars,car_slots] = 2
                            elif car_color == GREEN:
                                df9.iloc[Cars,car_slots] = 3
                            elif car_color == LIGHT_GREEN:
                                df9.iloc[Cars,car_slots] = 4
                          
                        
                        pygame.draw.rect(screen,
                                            car_color,
                                            [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
                                            (MARGIN + HEIGHT) * Cars + MARGIN+500,
                                            ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                            HEIGHT])
                        screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN+200) ,(MARGIN + HEIGHT) * Cars + MARGIN+500))
                        pygame.time.delay(10)
                        pygame.display.update()
                        
                        
                        break
                    elif Success == False:
                        pass
                            #print (Success) #No, I cannot Schedule this car
                else:
                    Success = False
                    #failed to find empty start slot
            # if Success == False:
            #     for car_slots in range(Start_Slot, Start_Slot+Number_of_Slots):
            #         pygame.draw.rect(screen,
            #                         PINK,
            #                         [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
            #                         (MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN,
            #                         ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
            #                         HEIGHT])
            #         screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #         screen.blit(font.render(str(type_of_car),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+193 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #     failure_count+=1
        # print(df8)
        ratio = (count_num1 )/ total_slots
        print("Total number of people successfully scheduled:" , scheduled)
        print('Ratio of filled to non-filled slots:', ratio)
        print("Number failed =", failure_count)
   
    def second_data():
        col_list= ['Start', 'Number_hours', 'ID', 'Type', 'Garage', 'Status']
        df = pd.read_csv("algorithm.csv", usecols= col_list)
        second_df = pd.read_csv("algorithm1.csv", usecols = col_list)
        t = df.append(second_df)
        
        result = t.sort_values(by = ['Start'])
        columns = []
        count = 0
        for number in range(number_hours):
            count +=1
            columns.append(count)
            
        for num in range(num_res):
            car_type2 = r.choice(car_type)
            ct1.append(car_type2)
            datf8 = pd.DataFrame ({
                "Type": cartype
            })
            datf9 = pd.DataFrame ({
                "Type" : cartype
            })
            
        for col in range(count):
            datf8[col] = -1
            datf9[col] = -1

        df8 = datf8.sort_values(by = ['Type'])
        
        df9 = datf9.sort_values(by = ['Type'])
              
        screen.fill(WHITE)
        for row in range(num_cars):
            color = GRAY
            for column in range(number_hours):
                pygame.draw.rect(screen,
                                color,
                            [((MARGIN + WIDTH) * column + MARGIN)+950,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
            
        for row in range(num_cars):
            color = GRAY
            for column in range(number_hours):
                pygame.draw.rect(screen,
                                color,
                            [((MARGIN + WIDTH) * column + MARGIN)+200,
                            (MARGIN + HEIGHT) * row + MARGIN+500,
                            WIDTH,
                            HEIGHT])

        for row in range(num_cars):
            color = GRAY
            for column in range(number_hours):
                pygame.draw.rect(screen,
                                color,
                            [((MARGIN + WIDTH) * column + MARGIN)+950,
                            (MARGIN + HEIGHT) * row + MARGIN+500,
                            WIDTH,
                            HEIGHT])
        for row in range(num_cars):
            color = GRAY
            for column in range(number_hours):
                pygame.draw.rect(screen,
                            color,
                            [((MARGIN + WIDTH) * column + MARGIN)+200,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
            count = 0
            count1= -1
        
        for i in range (number_hours-1):
            count += 1    
            for i in range(number_hours):
                count1 +=1 
                screen.blit(font9.render(str(count),True,(0,0,0)),((((MARGIN +WIDTH ) * count)+4 )+200,(((HEIGHT ) * 1)-8) * 1 ))
                screen.blit(font9.render(str(count),True,(0,0,0)),((((MARGIN +WIDTH ) * count)+204 ),((HEIGHT -8+500  ))))                                              
                screen.blit(font9.render(str(count),True,(0,0,0)),((((MARGIN +WIDTH ) * count)+954 ),((HEIGHT -8 +500 ))))                                             
                screen.blit(font9.render(str(count),True,(0,0,0)),((((MARGIN +WIDTH ) * count)+954 ),((HEIGHT -8  ))))
                
        input_rect1 = pygame.draw.rect(screen,
                        BLUE,
                        [5,
                        0,
                        195,
                        40])    

        input_rect3 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        50,
                        195,
                        25])    
        
        input_rect4 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        80,
                        195,
                        25])    
        
        input_rect5 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        110,
                        195,
                        25])
        input_rect6 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        140,
                        195,
                        25])     
        
        rectangle = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        170,
                        195,
                        25])
        rectangle1 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        200,
                        195,
                        25])
        rectangle2 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        230,
                        195,
                        25])
        rectangle3 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        260,
                        195,
                        25])
        rectangle4 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        290,
                        195,
                        25])
        
        rectangle5 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        320,
                        195,
                        25])
        rectangle6 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        350,
                        195,
                        25])
        rectangle7 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        380,
                        195,
                        25])
        rectangle8 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        410,
                        195,
                        25])
        rectangle9 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        440,
                        195,
                        25])
        rectangle10 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        470,
                        195,
                        25])
        rectangle11 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        500,
                        195,
                        25])
        rectangle12 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        530,
                        195,
                        40])
        
        
        
        input_rect9 = pygame.draw.rect(screen,
                        DARK_GRAY,
                        [5,
                        750,
                        195,
                        72.5])  
        data_button = pygame.draw.rect(screen,
                        BLUE2,
                        [5,
                        827.5,
                        195,
                        36.25]) 
        data_button2 = pygame.draw.rect(screen,
                        BLUE2,
                        [5,
                        868.75,
                        195,
                        36.25]) 
        Line1 = pygame.draw.rect(screen,
                     BLACK,
                     [200,
                      125,
                      1800,
                      2.5])   
        Line2 = pygame.draw.rect(screen,
                        BLACK,
                        [200,
                        250,
                        1800,
                        2.5])   
        Line3 = pygame.draw.rect(screen,
                        BLACK,
                        [200,
                        363,
                        1800,
                        2.5])   
        
        Line4 = pygame.draw.rect(screen,
                                 BLACK,
                                 [0,
                                  165,
                                  200,
                                  5])
        Line5 = pygame.draw.rect(screen,
                                 BLACK,
                                 [0,
                                  285,
                                  200,
                                  5])
        Line6 = pygame.draw.rect(screen,
                                 BLACK,
                                 [0,
                                  405,
                                  200,
                                  5])
        Line7 = pygame.draw.rect(screen,
                     BLACK,
                     [200,
                      625,
                      1800,
                      2.5])   
        Line8 = pygame.draw.rect(screen,
                        BLACK,
                        [200,
                        750,
                        1800,
                        2.5])   
        Line9 = pygame.draw.rect(screen,
                        BLACK,
                        [200,
                        863,
                        1800,
                        2.5])
        count_num1 = 0
        scheduled = 0
        failure_count = 0
        for i in range(num_res * 2):
            Success = False
            Start_Slot = result.iloc[i,0]
            Number_of_Slots = result.iloc[i,1]
            Res_ID = result.iloc[i,2]
            type_of_car = result.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if df8.iloc[Cars,Start_Slot] == -1 and df8.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
                    #print (df8.iloc[Cars])
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        # print   (df8.iloc[Cars,car_slots])
                        if df8.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                        
                        scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                        car_color = BLUE
                        if Cars % 2 == 0:
                            car_color = BLUE 
                            if car_slots > 0 and df9.iloc[Cars,Start_Slot - 1] == 1:
                                car_color = PINK  #2                      
                        else:
                            car_color = GREEN 
                            if car_slots > 0 and df9.iloc[Cars,Start_Slot - 1] == 3:
                                car_color = LIGHT_GREEN #4

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            df8.iloc[Cars,car_slots] = Res_ID
                            count_num1 += 1
                            if car_color == BLUE:
                                df9.iloc[Cars,car_slots] = 1
                            elif car_color == PINK:
                                df9.iloc[Cars,car_slots] = 2
                            elif car_color == GREEN:
                                df9.iloc[Cars,car_slots] = 3
                            elif car_color == LIGHT_GREEN:
                                df9.iloc[Cars,car_slots] = 4
                          
                        
                        pygame.draw.rect(screen,
                                            car_color,
                                            [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
                                            (MARGIN + HEIGHT) * Cars + MARGIN,
                                            ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                            HEIGHT])
                        screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * Cars + MARGIN))
                        pygame.time.delay(10)
                        pygame.display.update()
                        
                        
                        break
                    elif Success == False:
                        pass
                            #print (Success) #No, I cannot Schedule this car
                else:
                    Success = False
                    #failed to find empty start slot
            # if Success == False:
            #     for car_slots in range(Start_Slot, Start_Slot+Number_of_Slots):
            #         pygame.draw.rect(screen,
            #                         PINK,
            #                         [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
            #                         (MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN,
            #                         ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
            #                         HEIGHT])
            #         screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #         screen.blit(font.render(str(type_of_car),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+193 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #     failure_count+=1
        # print(df8)
        ratio = (count_num1 )/ total_slots
        print("Total number of people successfully scheduled:" , scheduled)
        print('Ratio of filled to non-filled slots:', ratio)
        print("Number failed =", failure_count)
        
    def garage4_function():    
        col_list= ['Start', 'Number_hours', 'ID', 'Type', 'Garage', 'Status']
        df = pd.read_csv("garage4_data.csv", usecols= col_list)
        

        function.count_num = 0
        
        failure_count = 0
        total_scheduled = 0
        for i in range(num_res):
            Success = False
            Start_Slot = df.iloc[i,0]
            Number_of_Slots = df.iloc[i,1]
            Res_ID = df.iloc[i,2]
            type_of_car = df.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if g4.iloc[Cars,Start_Slot] == -1 and g4.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
            
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        #print   (df1.iloc[Cars,car_slots])
                        if g4.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                    
                        total_scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                        car_color = BLUE
                        if Cars % 2 == 0:
                            car_color = BLUE 
                            if car_slots > 0 and df2.iloc[Cars,Start_Slot - 1] == 1:
                                car_color = PINK  #2                      
                        else:
                            car_color = GREEN 
                            if car_slots > 0 and df2.iloc[Cars,Start_Slot - 1] == 3:
                                car_color = LIGHT_GREEN #4

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            g4.iloc[Cars,car_slots] = Res_ID
                            function.count_num += 1
                            if car_color == BLUE:
                                df2.iloc[Cars,car_slots] = 1
                            elif car_color == PINK:
                                df2.iloc[Cars,car_slots] = 2
                            elif car_color == GREEN:
                                df2.iloc[Cars,car_slots] = 3
                            elif car_color == LIGHT_GREEN:
                                df2.iloc[Cars,car_slots] = 4
                        
                    
                    
                            pygame.draw.rect(screen,
                                                car_color,
                                                [((MARGIN + WIDTH) * Start_Slot + MARGIN)+950,
                                                (MARGIN + HEIGHT) * Cars + MARGIN +500,
                                                ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                                HEIGHT])
                            screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN+950) ,(MARGIN + HEIGHT) * Cars + MARGIN+500))
                        pygame.time.delay(10)
                        pygame.display.update()    
                        break
                    else:
                        pass
                
                
                            #print (Success) #No, I cannot Schedule this car
            # if Success == False:
            #     for car_slots in range(Start_Slot, Start_Slot+Number_of_Slots):
            #         pygame.draw.rect(screen,
            #                         PINK,
            #                         [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
            #                         (MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN,
            #                         ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
            #                         HEIGHT])
            #         screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #         screen.blit(font.render(str(type_of_car),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+193 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #     failure_count+=1                
        print("Total number of people successfully scheduled:" , total_scheduled)
        print('Ratio of filled to non-filled slots:', function.count_num/ total_slots)
        num_scheduled = "successfully scheduled"
        text_surface6 = font1.render(str(num_scheduled), True, BLACK)
        text_surface5 = font1.render(str(total_scheduled), True, BLACK)
        screen.blit(text_surface5, (rectangle12.x+5, rectangle12.y +5+18))
        screen.blit(text_surface6, (rectangle12.x +5, rectangle12.y+5))
   
    def garage4_second_data():
        col_list= ['Start', 'Number_hours', 'ID', 'Type', 'Garage', 'Status']
        df = pd.read_csv("garage4_data.csv", usecols= col_list)
        second_df = pd.read_csv("garage4_second_data.csv", usecols = col_list)
        t = df.append(second_df)
        
        result = t.sort_values(by = ['Start'])
        columns = []
        count = 0
        for number in range(number_hours):
            count +=1
            columns.append(count)
            
        for num in range(num_res):
            car_type2 = r.choice(car_type)
            ct1.append(car_type2)
            datf8 = pd.DataFrame ({
                "Type": cartype
            })
            datf9 = pd.DataFrame ({
                "Type" : cartype
            })
            
        for col in range(count):
            datf8[col] = -1
            datf9[col] = -1

        df8 = datf8.sort_values(by = ['Type'])
        
        df9 = datf9.sort_values(by = ['Type'])
        
        count_num1 = 0
        scheduled = 0
        failure_count = 0
        for i in range(num_res * 2):
            Success = False
            Start_Slot = result.iloc[i,0]
            Number_of_Slots = result.iloc[i,1]
            Res_ID = result.iloc[i,2]
            type_of_car = result.iloc [i,3]
            for Cars in range (1,num_cars): #resources to schedule
                if df8.iloc[Cars,Start_Slot] == -1 and df8.iloc[Cars, 0] == type_of_car:
                #if df1.iloc[Cars,Start_Slot] == 0:
                    Success = True
                    #print (df8.iloc[Cars])
                    for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                        # print   (df8.iloc[Cars,car_slots])
                        if df8.iloc[Cars,car_slots] !=-1:
                            Success = False
                            break
                    if Success == True:
                        
                        scheduled += 1
                        Success = True
                        #print (Success) #Yes, I can Schedule this Car
                        car_color = BLUE
                        if Cars % 2 == 0:
                            car_color = BLUE 
                            if car_slots > 0 and df9.iloc[Cars,Start_Slot - 1] == 1:
                                car_color = PINK  #2                      
                        else:
                            car_color = GREEN 
                            if car_slots > 0 and df9.iloc[Cars,Start_Slot - 1] == 3:
                                car_color = LIGHT_GREEN #4

                                
                        for car_slots in range (Start_Slot,Start_Slot+Number_of_Slots):
                            df8.iloc[Cars,car_slots] = Res_ID
                            count_num1 += 1
                            if car_color == BLUE:
                                df9.iloc[Cars,car_slots] = 1
                            elif car_color == PINK:
                                df9.iloc[Cars,car_slots] = 2
                            elif car_color == GREEN:
                                df9.iloc[Cars,car_slots] = 3
                            elif car_color == LIGHT_GREEN:
                                df9.iloc[Cars,car_slots] = 4
                          
                        
                        pygame.draw.rect(screen,
                                            car_color,
                                            [((MARGIN + WIDTH) * Start_Slot + MARGIN)+950,
                                            (MARGIN + HEIGHT) * Cars + MARGIN+500,
                                            ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
                                            HEIGHT])
                        screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN+950) ,(MARGIN + HEIGHT) * Cars + MARGIN+500))
                        pygame.time.delay(10)
                        pygame.display.update()
                        
                        
                        break
                    elif Success == False:
                        pass
                            #print (Success) #No, I cannot Schedule this car
                else:
                    Success = False
                    #failed to find empty start slot
            # if Success == False:
            #     for car_slots in range(Start_Slot, Start_Slot+Number_of_Slots):
            #         pygame.draw.rect(screen,
            #                         PINK,
            #                         [((MARGIN + WIDTH) * Start_Slot + MARGIN)+200,
            #                         (MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN,
            #                         ((WIDTH* Number_of_Slots ) + (MARGIN * Number_of_Slots) - MARGIN ),
            #                         HEIGHT])
            #         screen.blit(font.render(str(Res_ID),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+200 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #         screen.blit(font.render(str(type_of_car),True,(0,0,0)),(((MARGIN + WIDTH) * car_slots + MARGIN)+193 ,(MARGIN + HEIGHT) * (num_cars + failure_count) + 20  + MARGIN))
            #     failure_count+=1
        # print(df8)
        ratio = (count_num1 )/ total_slots
        print("Total number of people successfully scheduled:" , scheduled)
        print('Ratio of filled to non-filled slots:', ratio)
        print("Number failed =", failure_count)
       
    def draw():
        text_surface = font0.render(data_gen, True, BLACK)
        screen.blit(text_surface, (input_rect1.x +50, (input_rect1.y+10)))
                    
        ########################################################################
        text = "Click to Run"
        text_surface9 = font1.render(str(text), True, BLUE2)
        screen.blit(text_surface9, (input_rect9.x + 50, input_rect9.y +20))
        
        text1 = "CHANGE DATA"
        ts1 = font1.render(str(text1), True, WHITE)
        screen.blit(ts1, (data_button.x +40, data_button.y +5))
        
        text2 = "Add Second Dataset"
        ts2 = font1.render(str(text2), True, WHITE)
        screen.blit(ts2, (data_button2.x +30, data_button2.y +5))
        
        t = "Garage 1 car type 1"
        t1 = "Garage 1 car type 2"
        t2 = "Garage 1 car type 3"
        t3 = "Garage 1 car type 4"
        t4 = "Garage 2 car type 1"
        t5 = "Garage 2 car type 2"
        t6 = "Garage 2 car type 3"
        t7 = "Garage 2 car type 4"
        t8 = "Garage 3 car type 1"
        t9 = "Garage 3 car type 2"
        t10 = "Garage 3 car type 3"
        t11 = "Garage 3 car type 4"
        t12 = "Garage 4 car type 1"
        t13 = "Garage 4 car type 2"
        t14 = "Garage 4 car type 3"
        t15 = "Garage 4 car type 4"
        
        surface = font1.render(str(t), True, BLACK)
        surface1 = font1.render(str(t1), True, BLACK)
        surface2 = font1.render(str(t2), True, BLACK)
        surface3 = font1.render(str(t3), True, BLACK)
        surface4 = font1.render(str(t4), True, BLACK)
        surface5 = font1.render(str(t5), True, BLACK)
        surface6 = font1.render(str(t6), True, BLACK)
        surface7 = font1.render(str(t7), True, BLACK)
        surface8 = font1.render(str(t8), True, BLACK)
        surface9 = font1.render(str(t9), True, BLACK)
        surface10 = font1.render(str(t10), True, BLACK)
        surface11 = font1.render(str(t11), True, BLACK)
        surface12 = font1.render(str(t12), True, BLACK)
        surface13 = font1.render(str(t13), True, BLACK)
        surface14 = font1.render(str(t14), True, BLACK)
        surface15 = font1.render(str(t15), True, BLACK)
        
        screen.blit(surface, (input_rect3.x + 50, input_rect3.y + 3))
        screen.blit(surface1, (input_rect4.x + 50, input_rect4.y + 3))
        screen.blit(surface2, (input_rect5.x + 50, input_rect5.y + 3))
        screen.blit(surface3, (input_rect6.x + 50, input_rect6.y + 3))
        screen.blit(surface4, (rectangle.x + 50, rectangle.y + 3))
        screen.blit(surface5, (rectangle1.x + 50, rectangle1.y + 3))
        screen.blit(surface6, (rectangle2.x + 50, rectangle2.y + 3))
        screen.blit(surface7, (rectangle3.x + 50, rectangle3.y + 3))
        screen.blit(surface8, (rectangle4.x + 50, rectangle4.y + 3))
        screen.blit(surface9, (rectangle5.x + 50, rectangle5.y + 3))
        screen.blit(surface10, (rectangle6.x + 50, rectangle6.y + 3))
        screen.blit(surface11, (rectangle7.x + 50, rectangle7.y + 3))
        screen.blit(surface12, (rectangle8.x + 50, rectangle8.y + 3))
        screen.blit(surface13, (rectangle9.x + 50, rectangle9.y + 3))
        screen.blit(surface14, (rectangle10.x +50, rectangle10.y +3))
        screen.blit(surface15, (rectangle11.x +50, rectangle11.y +3))
        
    while True:
        new_resv = 0
        new_resv1 = 0
        new_resv2 = 0
        new_resv3 = 0
        new_resv4 = 0
        new_resv5 = 0
        new_resv6 = 0
        new_resv7 = 0
        new_resv8 = 0
        new_resv9 = 0
        new_resv10 = 0
        new_resv11 = 0
        new_resv12 = 0
        new_resv13 = 0
        new_resv14 = 0
        new_resv15 = 0
        
        pygame.display.update()
        draw()
        
            
       
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if state == True:
                    
                    if input_rect1.collidepoint(mouse_pos):
                        data_chart.to_csv("algorithm.csv")
                        data_chart2.to_csv("algorithm1.csv")
                        
                        garage2_data.to_csv("garage2_data.csv")
                        garage2_seconddata.to_csv("garage2_second_data.csv")
                        
                        garage3_data.to_csv("garage3_data.csv")
                        garage3_seconddata.to_csv("garage3_second_data.csv")
                        
                        garage4_data.to_csv("garage4_data.csv")
                        garage4_seconddata.to_csv("garage4_second_data.csv")
                    if input_rect9.collidepoint(mouse_pos):
                        function()
                        garage2_function()
                        garage3_function()
                        garage4_function()
                        pygame.display.flip() 
                    elif data_button.collidepoint(mouse_pos):
                        data_chart.to_csv("algorithm.csv")
                        data_chart2.to_csv("algorithm1.csv")
                    elif data_button2.collidepoint(mouse_pos):
                        second_data()
                        garage2_second_data()
                        garage3_second_data()
                        garage4_second_data()
                        # result.to_csv("dump.csv")
                    elif input_rect3.collidepoint(mouse_pos):
                        new_resv += 1
                        new_res_g1c1()
                    elif input_rect4.collidepoint(mouse_pos):
                        new_resv1 += 1
                        new_res_g1c2()
                    elif input_rect5.collidepoint(mouse_pos):
                        new_resv2 += 1
                        new_res_g1c3()
                    elif input_rect6.collidepoint(mouse_pos):
                        new_resv3 += 1
                        new_res_g1c4()
                    elif rectangle.collidepoint(mouse_pos):
                        new_resv4 += 1
                        new_res_g2c1()
                    elif rectangle1.collidepoint(mouse_pos):
                        new_resv5 += 1
                        new_res_g2c2()
                    elif rectangle2.collidepoint(mouse_pos):
                        new_resv6 += 1
                        new_res_g2c3()
                    elif rectangle3.collidepoint(mouse_pos):
                        new_resv7 += 1
                        new_res_g2c4()
                    elif rectangle4.collidepoint(mouse_pos):
                        new_resv8 += 1
                        new_res_g3c1()
                    elif rectangle5.collidepoint(mouse_pos):
                        new_resv9 += 1
                        new_res_g3c2()
                    elif rectangle6.collidepoint(mouse_pos):
                        new_resv10 += 1
                        new_res_g3c3()
                    elif rectangle7.collidepoint(mouse_pos):
                        new_resv11 += 1
                        new_res_g3c4()
                    elif rectangle8.collidepoint(mouse_pos):
                        new_resv12 += 1
                        new_res_g4c1()
                    elif rectangle9.collidepoint(mouse_pos):
                        new_resv13 += 1
                        new_res_g4c2()
                    elif rectangle10.collidepoint(mouse_pos):
                        new_resv14 += 1
                        new_res_g4c3()
                    elif rectangle11.collidepoint(mouse_pos):
                        new_resv15 += 1
                        new_res_g4c4()
                    
                    else:
                        print('no')
                        
                else:
                    pass                   
                    
               
                            
                
                # print(active, active1, active2, active3)
                    
if __name__ == "__main__":
    __main__()       
    