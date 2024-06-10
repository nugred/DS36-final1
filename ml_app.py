import streamlit as st
import numpy as np

# import ml package
import joblib
import os

attribute_info = """
                 Anggota Data Wizards Gengs:
                  - Fathimah Az Zahra Sanjani **
                  - Fredrich Naik Christian
                  - Edy Widarto
                  - (Gabriel Gracia Theresia Betrys) 
                  - (Fuad Ahsani)
                  - (Atikah Nur Hafizhah *)
                 """

dep = {'Sales & Marketing':1, 'Operations':2, 'Technology':3, 'Analytics':4,
       'R&D':5, 'Procurement':6, 'Finance':7, 'HR':8, 'Legal':9}
edu = {'Below Secondary':1, "Bachelor's":2, "Master's & above":3}
rec = {'referred':1, 'sourcing':2, 'others':3}
gen = {'m':1, 'f':2}
reg = {'region_1':1,'region_2':2,'region_3':3,'region_4':4,'region_5':5,
       'region_6':6,'region_7':7,'region_8':8,'region_9':9,'region_10':10,
       'region_11':11,'region_12':12,'region_13':13,'region_14':14,'region_15':15,
       'region_16':16,'region_17':17,'region_18':18,'region_19':19,'region_20':20,
       'region_21':21,'region_22':22,'region_23':23,'region_24':24,'region_25':25,
       'region_26':26,'region_27':27,'region_28':28,'region_29':29,'region_30':30,
       'region_31':31,'region_32':32,'region_33':33,'region_34':34}

def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value
        
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), 'rb'))
    return loaded_model

def run_ml_app():
    st.subheader("DS36 - Kelompok 2")
    with st.expander("Attribute Info"):
        st.markdown(attribute_info)

    st.subheader("Input Song's Data")
    song_name = st.text_input("Song Name" )
    song_duration_ms = st.number_input("Song Duration (ms)", 1, 1000000)
    acousticness = st.number_input("Acousticness", 1, 1000000)
    danceability = st.number_input("Danceability", 1, 1000000)
    energy = st.number_input("Energy", 1, 1000000)
    instrumentalness = st.number_input("Instrumentalness", 1, 1000000)
    key = st.number_input("Key", 1, 100)
    liveness = st.number_input("Liveness", 1, 1000000)
    loudness = st.number_input("Loudness", 1, 1000000)
    audio_mode = st.number_input("Audio Mode", 1, 10)
    speechiness = st.number_input("Speechiness", 1, 1000000)
    tempo = st.number_input("Tempo", 1, 1000)
    time_signature = st.number_input("Time Signature", 1, 100)
    audio_valence = st.number_input("Audio Valence", 1, 1000000)

    with st.expander("Your Selected Options"):
        result = {
            'Song Name':song_name,
            'Song Duration (ms)':song_duration_ms,
            'Acousticness':acousticness,
            'Danceability':danceability,
            'Energy':energy,
            'Instrumentalness':instrumentalness,
            'Key':key,
            'Liveness':liveness,
            'loudness':loudness,
            'Audio Mode':audio_mode,
            'Speechiness':speechiness,
            'Tempo':tempo,
            'Time Signature':time_signature,
            'Audio Valence':audio_valence,
        }
    
    # st.write(result)

    encoded_result = []
    for i in result.values():
        if type(i) == int:
            encoded_result.append(i)
        elif i in ['Sales & Marketing', 'Operations', 'Technology', 'Analytics', 'R&D', 'Procurement', 'Finance', 'HR', 'Legal']:
            res = get_value(i, dep)
            encoded_result.append(res)
        elif i in ['region_1','region_2','region_3','region_4','region_5', 'region_6','region_7',
                                    'region_8','region_9','region_10','region_11','region_12',
                                    'region_13','region_14','region_15','region_16','region_17','region_18','region_19',
                                    'region_20','region_21','region_22','region_23','region_24','region_25','region_26',
                                    'region_27','region_28','region_29','region_30','region_31','region_32','region_33',
                                    'region_34']:
            res = get_value(i, reg)
            encoded_result.append(res)
        elif i in ["Below Secondary", "Bachelor's", "Master's & above"]:
            res = get_value(i, edu)
            encoded_result.append(res)
        elif i in ['m','f']:
            res = get_value(i, gen)
            encoded_result.append(res)
        elif i in ["referred", "sourcing", "others"]:
            res = get_value(i, rec)
            encoded_result.append(res)
    
    # st.write(encoded_result)
    # prediction section
    st.subheader('Prediction Result')
    single_array = np.array(encoded_result).reshape(1, -1)
    # st.write(single_array)

    model = load_model("model_song_pred.pkl")

    prediction = model.predict(single_array)
    pred_proba = model.predict_proba(single_array)

    pred_probability_score = {'Promoted':round(pred_proba[0][1]*100,4),
                              'Not Promoted':round(pred_proba[0][0]*100,4)}
    
    if prediction == 1:
        st.success("Congratulation, you get promotion")

        st.write(pred_probability_score)
    else:
        st.warning('Need to improve')
        st.write(pred_probability_score)