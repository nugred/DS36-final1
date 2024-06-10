import streamlit as st
import streamlit.components.v1 as stc

from ml_app import run_ml_app

html_temp = """
            <div style="background-color:#3872fb;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">Song Popularity Prediction App </h1>
		    <h4 style="color:white;text-align:center;">by Data Wizards Geng </h4>
		    </div>
            """

desc_temp = """
            # Project: Song Popularity Prediction Application
            Aplikasi Prediction Appllication ini dimaksudkan untuk memprediksi seberapa Populer sebuah lagu berdasarkan beberapa parameter yang mempengaruhinya
            #### Data Source
            - https://www.kaggle.com/datasets/yasserh/songpopularity-dataset

            #### Application Content
            - Exploratory Data Analysis
            - Machine Learning Section
            - Application Deployment
            """

def main():

    stc.html(html_temp)
    
    menu = ['Preview', 'Popularity Prediction']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Preview':
        st.subheader("Terima kasih saat ini Anda sedang berkunjung di DataWizard's Project")
        st.markdown(desc_temp)
    elif choice == "Popularity Prediction":
        # st.subheader("Song Popularity Prediction")
        run_ml_app()


if __name__ == '__main__':
    main()
