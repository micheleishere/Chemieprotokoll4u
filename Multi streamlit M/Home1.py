import streamlit as st

import Notizen

# Logo/Name setzen für Tab in Google, so dass nicht "local" steht
st.set_page_config(
    page_title="Chemieprotokoll"
)

# Seitenleiste-Kommentar erstellen
import streamlit as st


# Seitenleiste-Kommentar erstellen
st.sidebar.success("Wähle ein Tab")



# Kolone erstellen, um den Titel links zu setzen und nicht in der Mitte
col1, col2, col3 = st.columns([1,2,1])
col1.markdown(' # :green[_Deine lieblings App für Chemieprotokolle!_] :test_tube:')

# Untertitel 
st.subheader('Das Chemieprotokoll unterstützt dich während deinen Labortpraktika bzw. Experimenten während deines Studiums. Hier kannst du deine Experimente dokumentieren, Notizen erstellen oder Berechnungen durchführen.')

#Bild in der 3. Kolone setzen
col3.image('https://synaigy-wbg-media-s3.s3.eu-central-1.amazonaws.com/media/image/6f/8f/42/Chemie-Kachel5cd3c9c0aaeff.jpg')

# Caption erstellen 
st.caption("Erstellt von der BMLD Studentin: Michèle Pfister")


import streamlit as st

options = ['Details', 'Experiment 1', 'Experiment 2', "Experiment 3", "Notizen", "Periodensystem", "Rechner"]
selected_option = st.selectbox('Wählen Sie eine Option aus:', options)

st.write('Sie haben die Option ausgewählt:', selected_option)

import streamlit as st

notiz = st.text_area('Tippen Sie hier Ihre Notizen zur Theoriebesprechung ein:', '', height=200, max_chars=1000)


import streamlit as st
import datetime 

# Kolone erstellen, dass Titel links und Emoji rechts
col1, col2, col3 = st.columns([1,2,1])
st.markdown(' # :green[_Dokumentation des Experiments_]')
col3.header(':test_tube:')

# Trennungslinie hinzufügen
st.write("---")

# Eingabe Titel 
title = st.text_input('Titel Experiment', ' ')

# Kalender hinzufügen
d = st.date_input(
    "Datum des Experiments",
    datetime.date(2023, 3, 31))

# Input Eingabe
title = st.text_input('Durchgeführt von', ' ')

title = st.text_input('Studiengang', ' ')

# Multiselektion 
options = st.multiselect(
    'Verwendetes Material',
    ['Erlenmeyerkolben', 'Messzylinder', 'Trichter', 'Polylöffel', 'Becherglas', 'Magnetstab mit Fischli', 'Messkolben', 'Bürette', 'Thermometer', 'Glasstab','Anderes'],
    ['Erlenmeyerkolben', 'Messzylinder'])

# Input Text 
txt = st.text_area('Verwendete Chemikalien: ')
st.write('Output:',txt)

txt = st.text_area('Ablauf des Experiments: ')
st.write('Ablauf Output:',txt)

txt = st.text_area('Schlussfolgerungen: ')
st.write('Schlussfolgerungen Output:',txt)


import streamlit as st

st.title("Taschenrechner")

num1 = st.number_input("Geben Sie die erste Zahl ein:")
num2 = st.number_input("Geben Sie die zweite Zahl ein:")

operation = st.selectbox("Wählen Sie eine Operation:", ["Addition", "Subtraktion", "Multiplikation", "Division"])

if st.button("Berechnen"):
    if operation == "Addition":
        result = num1 + num2
        st.write("Das Ergebnis von", num1, "+", num2, "ist", result)
    elif operation == "Subtraktion":
        result = num1 - num2
        st.write("Das Ergebnis von", num1, "-", num2, "ist", result)
    elif operation == "Multiplikation":
        result = num1 * num2
        st.write("Das Ergebnis von", num1, "*", num2, "ist", result)
    elif operation == "Division":
        if num2 == 0:
            st.write("Fehler: Division durch Null")
        else:
            result = num1 / num2
            st.write("Das Ergebnis von", num1, "/", num2, "ist", result)
            
import streamlit as st

notiz = st.text_area('Schreiben Sie hier Ihre Berechnungen auf:', '', height=200, max_chars=1000)

st.write("https://de.wikibooks.org/wiki/Formelsammlung_Chemie/_St%C3%B6chiometrie")

import streamlit as st

picture = st.camera_input("Mach ein Foto von deinem Experiment")

if picture:
    st.image(picture)
