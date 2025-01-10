import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

st.title("Analysis of Data")
csv1 = st.file_uploader("Upload Your File",type="csv")

if csv1 is not None:
    st.write("Success...")
    st.subheader("Data Preview")
    df = pd.read_csv(csv1)
    st.write(df)

    st.subheader("Filter Data")

    option1 = st.selectbox("Altering Data Based on Request.",("Graph","Order"),index = None,placeholder = "Select Method to Filter")
    if option1 == "Graph":
        st.subheader("Graphical Representation")
        option2 = st.selectbox("Choose Your Presentation",("Line","Bar"),index=None,placeholder = "Choose Display Style")
        if option2 == "Line":
            x1 = st.selectbox("Select X-Axis",df.columns,index=None,placeholder = "Select a Column")
            y1 = st.selectbox("Select Y-Axis",df.columns,index = None,placeholder = "Select a Column")
            if x1 and y1 is not None :
                chart1 = df[[x1, y1]].rename(columns={x1: "col1", y1: "col2"})
                st.line_chart(chart1, x="col1", y="col2")

        if option2 == "Bar":
            x1 = st.selectbox("Select X-Axis",df.columns,index=None,placeholder = "Select a Column")
            y1 = st.selectbox("Select Y-Axis",df.columns,index = None,placeholder = "Select a Column")
            if x1 and y1 is not None:
                chart1 = df[[x1,y1]].rename(columns={x1:"col1",y1:"col2"})
                st.bar_chart(chart1,x="col1",y="col2")
            
            
    elif option1 == "Order":
        st.subheader("Order By")
        response = st.selectbox("Choose Order Column",df.columns,index = None,placeholder = "Select Order By Column")
        if response is not None:
            st.subheader("Sorted Data")
            d1 = df.sort_values(by = response)
            st.write(d1)


else:
    st.write("Waiting for Upload...")


feedback = st.slider("Give us a Feedback",1.0,5.0)
if st.button("Submit"): 
    if feedback <= 1.0:
        st.title("😔")
    elif feedback <= 2:
        st.title("😞")
    elif feedback <= 3:
        st.title("🙂‍↔️")
    elif feedback <= 4:
        st.title("😏")
    else:
        st.title("😁")
