import random
import pandas as pd

def plan():
    with open("lunch.txt","r") as f:
        lunch = f.readlines()
    with open("veggies.txt","r") as f:
        veggies = f.readlines()
    with open("fruits.txt","r") as f:
        fruits = f.readlines()
    with open("breakfast.txt","r") as f:
        breakfast = f.readlines()
    with open("dinner.txt","r") as f:
        dinner = f.readlines()
    with open("curries.txt","r") as f:
        curries = f.readlines()
    with open("chutney.txt","r") as f:
        chutney = f.readlines()
    len_lunch = len(lunch)
    len_veggies = len(veggies)
    len_fruits = len(fruits)
    len_breakfast = len(breakfast)
    len_dinner = len(dinner)  
    len_curries = len(curries)  
    len_chutney = len(chutney)
    lst_lunch = random.sample(range(0,len_lunch),7)
    lst_veggies = random.sample(range(0,len_veggies),7)
    lst_fruits = random.sample(range(0,len_fruits),3)
    lst_breakfast = random.sample(range(0,len_breakfast),7)
    
    dict_lunch = {}
    dict_fruits = {}
    dict_breakfast = {}
    dict_dinner = {}    
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    for i in range(7):
        r_curries = random.choice(range(len_curries))
        r_chutney = random.choice(range(len_chutney))
        if lst_breakfast[i] >=4 and lst_breakfast[i] <=6:                                           #Change if change in breakfast.txt 
            dict_breakfast[days[i]] = breakfast[lst_breakfast[i]] + ", " + curries[r_curries]
        elif lst_breakfast[i] <= 3:                                                                 #Change if change in breakfast.txt
            dict_breakfast[days[i]] = breakfast[lst_breakfast[i]] + ", " + chutney[r_chutney]
        else:
            dict_breakfast[days[i]] = breakfast[lst_breakfast[i]]
        dict_lunch[days[i]] = lunch[lst_lunch[i]] + ", " + veggies[lst_veggies[i]]
        dict_fruits[days[i]] = fruits[random.choice(lst_fruits)]
        r_dinner = random.choice(range(len_dinner) )
        if r_dinner >= 2 and r_dinner <= 3:                                                                      #Change if change in dinner.txt
            dict_dinner[days[i]] = dinner[r_dinner] + ", " + curries[r_curries]
        elif r_dinner <= 1:                                                                                     #Change if change in dinner.txt
            dict_dinner[days[i]] = dinner[r_dinner] + ", " + chutney[r_chutney]
        else:
            dict_dinner[days[i]] = dinner[r_dinner]
    lst_of_dict = [dict_breakfast,dict_lunch,dict_fruits,dict_dinner]
    df = pd.DataFrame(data=lst_of_dict, index=["Breakfast","Lunch","Snack","Dinner"])
    return df
    