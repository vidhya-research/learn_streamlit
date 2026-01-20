from helper_functions import plan
import streamlit as st

#https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded - Refer this website for the icons used.

if 'ss_btn_view' not in st.session_state:
    st.session_state['ss_btn_view'] = False
if 'ss_sel_view' not in st.session_state:
    st.session_state['ss_sel_view'] = False
if 'ss_btn_update' not in st.session_state:
    st.session_state['ss_btn_update'] = False
if 'ss_sel_update' not in st.session_state:
    st.session_state['ss_sel_update'] = False
if 'ss_text_update' not in st.session_state:
    st.session_state["ss_text_update"]=False
if 'ss_btn_plan' not in st.session_state:
    st.session_state['ss_btn_plan'] = False

def btn_view():
    st.session_state['ss_btn_view'] = True
    st.session_state['ss_btn_update'] = False
    st.session_state['ss_sel_update'] = False
    st.session_state['ss_btn_plan'] = False
    st.session_state['ss_text_update'] = False
def sel_view():
    st.session_state['ss_btn_view'] = True
    st.session_state['ss_sel_view'] = True
def btn_update():
    st.session_state['ss_btn_view'] = False
    st.session_state['ss_btn_update'] = True
    st.session_state['ss_btn_plan'] = False
def sel_update():
    st.session_state['ss_btn_update'] = True
    st.session_state['ss_sel_update'] = True
def text_update():
    st.session_state['ss_btn_update'] = True
    st.session_state['ss_sel_update'] = True
    st.session_state['ss_text_update'] = True
def btn_plan():
    st.session_state['ss_btn_view'] = False
    st.session_state['ss_btn_update'] = False
    st.session_state['ss_btn_plan'] = True
    
st.set_page_config(layout="wide")
st.title('Flavours of home')

st.image("https://github.com/vidhya-research/learn_streamlit/blob/main/bg.JPG?raw=true",width=400)

files = ['breakfast','lunch','veggies','fruits','dinner','curries','chutney']

st.button(label="Let's view the menu!",help="Please click this button to view the menu!",icon=":material/multimodal_hand_eye:",on_click=btn_view)

if st.session_state['ss_btn_view'] == True:
    option1 = st.selectbox(label="Please select the menu!",options=files,index=None,on_change=sel_view)
    if option1!=None:
        st.write("Menu for ",option1)
        file_name = option1+".txt"
        with open(file_name,"r") as f:
            lst = f.readlines()
        s=""
        for i in lst:
            s += "- "+i+"\n"
        st.markdown(s)

st.button(label="Let's Plan for the week!", help="Please click this button to plan the flavours for the week!", icon=":material/chef_hat:",on_click=btn_plan)

if st.session_state['ss_btn_plan'] == True:
    df, str_grocery, str_daily = plan()
    st.dataframe(df)
    st.download_button("Daily Plan", data = str_daily, file_name="plan.html", mime="text/html", icon=":material/calendar_today:", on_click = "ignore")
    st.download_button("Grocery Shopping List", data = str_grocery, file_name="grocery.txt", icon=":material/shopping_cart:", on_click = "ignore")





