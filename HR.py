import streamlit as st
import pandas as pd

# Sidebar options
st.sidebar.title("MLB Home Run Leaders")
option = st.sidebar.selectbox("Choose an option", ["Home", "2024", "2023", "2022", "Postseason 2022-2024"])

# Main content
if option == "Home":
    st.header("Welcome to the MLB Home Run Leaders App")
    st.write("This app showcases the top 10 home run leaders for the 2022, 2023, and 2024 MLB seasons, as well as the combined postseason home run leaders from 2022-2024.")
    st.image("https://s.abcnews.com/images/Sports/aaron-judge_hpMain_20220922-164531.jpg", use_container_width=True)

elif option == "2024":
    st.header("2024 MLB Home Run Leaders")
    data = {
        "Player": ["Aaron Judge", "Shohei Ohtani", "Anthony Santander", "Juan Soto", "Marcell Ozuna", "Jose Ramirez", "Brent Rooker", "Kyle Schwarber", "Gunnar Henderson", "Ketel Marte"],
        "HR": [58, 54, 44, 41, 39, 39, 39, 38, 37, 36],
    }
    df = pd.DataFrame(data)
    st.table(df)
    st.write("Aaron Judge hit 58 homers in 2024, en route to his 2nd American League MVP Award in 3 years.")

elif option == "2023":
    st.header("2023 MLB Home Run Leaders")
    data = {
        "Player": ["Matt Olson", "Kyle Schwarber", "Pete Alonso", "Shohei Ohtani", "Ronald Acuña Jr.", "Marcell Ozuna", "Mookie Betts", "Adolis Garcia", "Luis Robert Jr.", "Aaron Judge"],
        "HR": [54, 47, 46, 44, 41, 40, 39, 39, 38, 37],
    }
    df = pd.DataFrame(data)
    st.table(df)
    st.write("In his 2nd season with the Braves after being traded from the Oakland A's, Matt Olson made his mark in Atlanta with 54 homers.")

elif option == "2022":
    st.header("2022 MLB Home Run Leaders")
    data = {
        "Player": ["Aaron Judge", "Kyle Schwarber", "Pete Alonso", "Austin Riley", "Yordan Alvarez", "Christian Walker", "Paul Goldschmidt", "Mookie Betts", "Rowdy Tellez", "Matt Olson"],
        "HR": [62, 46, 40, 38, 37, 36, 35, 35, 35, 34],
    }
    df = pd.DataFrame(data)
    st.table(df)
    st.write("Aaron Judge broke the longstanding American League home run record, beating Roger Maris' previous record of 61. He also took home his first AL MVP award.")

elif option == "Postseason 2022-2024":
    st.header("2022 MLB Home Run Leaders")
    data = {
        "Player": ["Bryce Harper", "Kyle Schwarber", "Giancarlo Stanton", "Yordan Alvarez", "Adolis Garcia", "Alex Bregman", "Nick Castellanos", "JT Realmuto", "Corey Seager", "Rhys Hoskins"],
        "HR": [12, 12, 9, 9, 8, 7, 6, 6, 6, 6],
    }
    df = pd.DataFrame(data)
    st.table(df)
    st.write("Despite not winning a World Series title during this time frame, the Phillies dominate this list with 5 of the top 10.")