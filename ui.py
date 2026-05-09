import streamlit as st
import core.cluster as clr
import core.parser as prs
import core.plotter as plt


st.header("Euclidian Hierarchical Clusters\n")

myDf = clr.defineCluster()

st.html('<h2>Our Data</h2>')

file = st.file_uploader("CSV", type="csv", max_upload_size=10, help="only 2 columns")
text = st.file_uploader("Text", type="txt", max_upload_size=10, help="in x,y format for each line")

if file:
    df = prs.csv(file)
    myDf = clr.defineCluster(df)

if text:
    df = prs.text(text)
    myDf = clr.defineCluster(df)


df2 = st.data_editor(myDf)

display = st.button("Display")

if display:
    plot = plt.plotDots(myDf)
    st.pyplot(plot)
