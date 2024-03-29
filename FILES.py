from deta import Deta
import streamlit as st
st.title(":rainbow[NEWSIFY]")
st.header(":blue[Explore the World]")
tab1, tab2, tab3 = st.tabs([":red[HOME]", ":red[SEARCH]", ":red[HELP]"])
with tab1:
    st.header("WHY NEWSIFY")
    st.write(
            """
            Nowadays NEWS companies develop a model which manipulated data for their gains. 
            so we developed our own model and feed our model with the well- optimized dataset. 
            we create our dataset by extracting data which are already segregated by multiple companies 
            and performing tasks like  data cleaning, Data mining, features engineering, NLP, sentiment analysis, 
            Feature selection and so and so... every time we feed our model it learns from the different dataset 
            and provides accurate and meaningful data to user""")
    st.snow()
with tab2:
   select = st.text_input("Enter the Word")
   submit = st.button("Search")
   if submit:
      DETA_KEY ="huijhuigthjdrggfkujh"


      deta = Deta(DETA_KEY)
      db = deta.Base("Workshop")
      res = db.fetch(query={"category?contains": select})
      data=res.items
      for news in data:
          st.header(news["headlines"])
          with st.container():
            left,right = st.columns(2)
          with left:
                st.image(news["images"])
          with right:
                st.write(news["news"])
                st.write(news["authors"])
                st.write(news["Date"])
                st.write(news["country"])
st.balloons()
with tab3:
    st.write("Here ask your problems while using the app")
    col1, col2= st.columns(2)
    with col1:
        st.header("REPORT YOUR PROBLEMS THROUGH GMAIL")
        st.image("https://www.pngegg.com/en/png-twaud")
    with col2:
        st.header("call support")
    




       








