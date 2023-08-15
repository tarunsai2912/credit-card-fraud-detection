# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 22:34:39 2023

@author: tarun
"""

import numpy as np
import pickle
import streamlit as st

pickled_model = pickle.load(open("C:/Users/tarun/Downloads/credit card fraud detection/creditcard.pkl","rb"))

def fraud_detection(input_data):
    input_array = np.asarray(input_data)
    input_reshaped_data = input_array.reshape(1,-1)
    output = pickled_model.predict(input_reshaped_data)
    
    if output==1:
        return("This is a Fraud Transaction")
    elif output==0:
        return("This is a Legal Transaction")
        
    
def main():
    
    st.title("CREDIT CARD FRAUD TRANSACTION DETECTION")
    st.write("Please Enter The Following Values")
    st.image("https://static3.businessinsider.com/image/5bbd145294750c2c154ff237-2400/best-credit-cards-4x3-1.png")
    
    
    Time=st.text_input("Enter The Time of Transaction") 
    V1=st.text_input("Enter The 1st Principal component of PCA")
    V2=st.text_input("Enter The 2nd Principal component of PCA")
    V3=st.text_input("Enter The 3rd Principal component of PCA")
    V4=st.text_input("Enter The 4th Principal component of PCA")
    V5=st.text_input("Enter The 5th Principal component of PCA")
    V6=st.text_input("Enter The 6th Principal component of PCA")
    V7=st.text_input("Enter The 7th Principal component of PCA")
    V8=st.text_input("Enter The 8th Principal component of PCA")
    V9=st.text_input("Enter The 9th Principal component of PCA")
    V10=st.text_input("Enter The 10th Principal component of PCA")
    V11=st.text_input("Enter The 11th Principal component of PCA")
    V12=st.text_input("Enter The 12th Principal component of PCA")
    V13=st.text_input("Enter The 13th Principal component of PCA")
    V14=st.text_input("Enter The 14th Principal component of PCA")
    V15=st.text_input("Enter The 15th Principal component of PCA")
    V16=st.text_input("Enter The 16th Principal component of PCA")
    V17=st.text_input("Enter The 17th Principal component of PCA")
    V18=st.text_input("Enter The 18th Principal component of PCA")
    V19=st.text_input("Enter The 19th Principal component of PCA")
    V20=st.text_input("Enter The 20th Principal component of PCA")
    V21=st.text_input("Enter The 21st Principal component of PCA")
    V22=st.text_input("Enter The 22nd Principal component of PCA")
    V23=st.text_input("Enter The 23rd Principal component of PCA")
    V24=st.text_input("Enter The 24th Principal component of PCA")
    V25=st.text_input("Enter The 25th Principal component of PCA")
    V26=st.text_input("Enter The 26th Principal component of PCA")
    V27=st.text_input("Enter The 27th Principal component of PCA")
    V28=st.text_input("Enter The 28th Principal component of PCA")
    Amount=st.text_input("Enter Amount")
    
    ans = ''
    
    if st.button("Test For Detection"):
        ans = fraud_detection([Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount])
        
    st.success(ans)
    
    st.image("https://th.bing.com/th/id/OIP.f2AB-DruupotqySlfPwhWgHaHV?pid=ImgDet&w=480&h=475&rs=1")
if __name__ == "__main__":
    main()  