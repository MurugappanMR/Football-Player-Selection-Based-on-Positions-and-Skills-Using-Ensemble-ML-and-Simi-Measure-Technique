#!/usr/bin/env python
# coding: utf-8
# importing required libraries
import numpy as np
import pickle
import pandas as pd
import streamlit as st
from   scipy.spatial import distance

# import image to load images using functions
from PIL import Image

# def welcome():
#     return "Welcome All"

def custom_func(Similarity,name):
    Similarity1=Similarity.drop(["Name"],axis=1)
    player_name=name #"neymar da Silva Santos Jr.
    p_ind=Similarity[Similarity["Name"]==player_name].index[0]
    sn=Similarity["Name"].to_list()
    cossim=[]
    for i in range (0,len(Similarity1.index)):
        cossim.append(1 - distance.cosine(Similarity1.iloc[p_ind].values,Similarity1.iloc[i].values))
    # pd.Series(cossim)
    sim2={"name":sn,"cossim":cossim}
    sim2=pd.DataFrame(sim2)
    re = sim2.iloc[sim2["cossim"].sort_values(ascending=False).index].head(10)
    re = re.reset_index(drop=True)
    print(re)
    return re
    print(type(re))
# defining main function will call sub function above
def main():
    st.title("Player Selection")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Player Selection ML Web App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    df=pd.read_csv("Similarity.csv")
    name = st.text_input("Enter Player Name","")
    result=""
    
#     'Region_Code','Previously_Insured','Vehicle_Damage','Policy_Sales_Channel'
    if st.button("Predict"):
#         result=predict_note_authentication(name)
        result = custom_func(df,name)
    st.write(result)

if __name__=='__main__':
    main()

