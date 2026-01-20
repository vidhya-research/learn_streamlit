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

    lst_grocery = []
    dict_lunch = {}
    dict_fruits = {}
    dict_breakfast = {}
    dict_dinner = {}    
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    for i in range(7):
        r_curries = random.choice(range(len_curries))
        r_chutney = random.choice(range(len_chutney))
        if lst_breakfast[i] >=4 and lst_breakfast[i] <=6:                                           #Change if change in breakfast.txt 
            dict_breakfast[days[i]] = breakfast[lst_breakfast[i]].strip() + ", " + curries[r_curries].strip()
            lst_grocery.append(curries[r_curries].strip())
        elif lst_breakfast[i] <= 3:                                                                 #Change if change in breakfast.txt
            dict_breakfast[days[i]] = breakfast[lst_breakfast[i]].strip() + ", " + chutney[r_chutney].strip()
            lst_grocery.append(chutney[r_chutney].strip())
        else:
            dict_breakfast[days[i]] = breakfast[lst_breakfast[i]].strip()
        dict_lunch[days[i]] = lunch[lst_lunch[i]].strip() + ", " + veggies[lst_veggies[i]].strip()
        lst_grocery.append(lunch[lst_lunch[i]].strip())
        lst_grocery.append(veggies[lst_veggies[i]].strip())
        dict_fruits[days[i]] = fruits[random.choice(lst_fruits)].strip()
        lst_grocery.append(fruits[random.choice(lst_fruits)].strip())
        r_dinner = random.choice(range(len_dinner) )
        if r_dinner >= 2 and r_dinner <= 3:                                                                      #Change if change in dinner.txt
            dict_dinner[days[i]] = dinner[r_dinner].strip() + ", " + curries[r_curries].strip()
            lst_grocery.append(curries[r_curries].strip())
        elif r_dinner <= 1:                                                                                     #Change if change in dinner.txt
            dict_dinner[days[i]] = dinner[r_dinner].strip() + ", " + chutney[r_chutney].strip()
            lst_grocery.append(chutney[r_chutney].strip())
        else:
            dict_dinner[days[i]] = dinner[r_dinner].strip()
    lst_of_dict = [dict_breakfast,dict_lunch,dict_fruits,dict_dinner]
    df = pd.DataFrame(data=lst_of_dict, index=["Breakfast","Lunch","Snack","Dinner"])
    set_grocery = set(lst_grocery)
    result_string = "\n".join(set_grocery)
    str_sun = dict_breakfast["Sunday"]+"<br>"+dict_lunch["Sunday"]+"<br>"+dict_fruits["Sunday"]+"<br>"+dict_dinner["Sunday"]
    str_mon = dict_breakfast["Monday"]+"<br>"+dict_lunch["Monday"]+"<br>"+dict_fruits["Monday"]+"<br>"+dict_dinner["Monday"]
    str_tue = dict_breakfast["Tuesday"]+"<br>"+dict_lunch["Tuesday"]+"<br>"+dict_fruits["Tuesday"]+"<br>"+dict_dinner["Tuesday"]
    str_wed = dict_breakfast["Wednesday"]+"<br>"+dict_lunch["Wednesday"]+"<br>"+dict_fruits["Wednesday"]+"<br>"+dict_dinner["Wednesday"]
    str_thu = dict_breakfast["Thursday"]+"<br>"+dict_lunch["Thursday"]+"<br>"+dict_fruits["Thursday"]+"<br>"+dict_dinner["Thursday"]
    str_fri = dict_breakfast["Friday"]+"<br>"+dict_lunch["Friday"]+"<br>"+dict_fruits["Friday"]+"<br>"+dict_dinner["Friday"]
    str_sat = dict_breakfast["Saturday"]+"<br>"+dict_lunch["Saturday"]+"<br>"+dict_fruits["Saturday"]+"<br>"+dict_dinner["Saturday"]
    
    str_daily = f"""
    <!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<head>
<title>Flavours of Home!</title>
</head>

<body>

<h1 style="text-align: center;"><b>Flavours of Home!</b></h1>
<br>
<img src="https://github.com/vidhya-research/learn_streamlit/blob/main/bg.JPG?raw=true" width="400" height="524">
<br>
<br>
<label for="h_lb_day" style="text-align: center;font-size: 20px;font-family:'Courier New';">Today is: </label>
<select name="s_day" id="h_sel_day" style="text-align: center;font-size: 16px;font-family:'Courier New';">
    <option value="Sunday">Sunday</option>
    <option value="Monday">Monday</option>
    <option value="Tuesday">Tuesday</option>
    <option value="Wednesday">Wednesday</option>
    <option value="Thursday">Thursday</option>
    <option value="Friday">Friday</option>
    <option value="Saturday">Saturday</option>
</select>

<button type="button" onclick="display()" style="font-size: 16px;font-family:'Courier New';">Let's see!</button>

<p id="disp" style="font-size: 20px;font-family:'Courier New'; "></p>

<script>
function display() {{
	if (document.getElementById("h_sel_day").value == "Sunday")
	{{
		document.getElementById("disp").innerHTML = "{str_sun}";
	}}
	else if (document.getElementById("h_sel_day").value == "Monday")
	{{
		document.getElementById("disp").innerHTML = "{str_mon}";

	}}
	else if (document.getElementById("h_sel_day").value == "Tuesday")
	{{
		document.getElementById("disp").innerHTML = "{str_tue}";

	}}
	else if (document.getElementById("h_sel_day").value == "Wednesday")
	{{
		document.getElementById("disp").innerHTML = "{str_wed}";

	}}
	else if (document.getElementById("h_sel_day").value == "Thursday")
	{{
		document.getElementById("disp").innerHTML = "{str_thu}";

	}}
	else if (document.getElementById("h_sel_day").value == "Friday")
	{{
		document.getElementById("disp").innerHTML = "{str_fri}";

	}}
	else
	{{
		document.getElementById("disp").innerHTML = "{str_sat}";

	}}

}}
</script>


</body>
</html>


    """
    return df, result_string, str_daily
    