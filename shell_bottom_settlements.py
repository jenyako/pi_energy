import streamlit as st
import math


st.set_page_config(page_title="Shell Bottom Calculation", layout="wide")
st.image('https://static.wixstatic.com/media/7a68aa_023f914caedb43e6b3377626233b3aaa~mv2.png/v1/fill/w_234,h_90,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/PI%20LOGO_PNG_transparency.png')
st.title("Shell Bottom Settlements Calculator")


col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("Tank Diameter [mm]: :red[*]")
with col2:
    tank_d = st.number_input("Input Tank Diameter", value=None, step=1, key="tank_d", label_visibility="collapsed")

st.divider()

# === Number Of Shell Stations ===
col5, col6 = st.columns([1, 2])
with col5:
     st.subheader("Number of Shell Stations: :red[*]")
with col6:
    station_num_options = [8,10,12,14,16,18,20,22,24,26, "Custom Value"]
    selected_n = st.pills(
        label="Standard Numbers",
        options=station_num_options,
        format_func=str,
        selection_mode="single",
        key="n_pills",
        default=8,
        label_visibility="collapsed"
    )

    if selected_n == "Custom Value":
        stations_num = st.number_input("Stations Number", min_value=8, value=None, step=2, key="st_num", label_visibility="collapsed")
    elif selected_n is not None:
        stations_num = float(selected_n)
    else:
        stations_num = None

st.divider()


# === Number Of Bottom Stations ===
col3, col4 = st.columns([1, 2])
with col3:
     st.subheader("Number of Bottom Stations (on Radius): :red[*]")
with col4:
    bot_num_options = [2,3,4,5,6,7,8,9,10,11,12, "Custom Value"]
    selected_b = st.pills(
        label="Standard Numbers",
        options=bot_num_options,
        format_func=str,
        selection_mode="single",
        key="b_pills",
        default=3,
        label_visibility="collapsed"
    )

    if selected_b == "Custom Value":
        bot_stations_num = st.number_input("Stations Number", min_value=2, value=None, step=2, key="bot_st_num", label_visibility="collapsed")
    elif selected_b is not None:
        bot_stations_num = float(selected_b)
    else:
        bot_stations_num = None

if tank_d is None or stations_num is None or bot_stations_num is None:
    st.warning("Enter all Parameters")
    st.stop()


st.divider()

#st.header("Results", divider=True)

tank_len = math.pi*tank_d
max_dist = 32*304.8
arc_len = tank_len / stations_num
R = tank_d / 2
theta = arc_len / R
chord_len = 2 * R * math.sin(theta / 2)

bot_st_distance = R / (bot_stations_num + 1)

st.metric(label=f"Arc Between Stations", value=f"{format(arc_len, ',.0f')} mm", delta=f"Arc Between Shell Stations (L)", label_visibility="collapsed", border=True)

if arc_len > max_dist:
    st.error('Distance is more than 32 ft', icon="🚨")

st.metric(label=f"Chord Between Stations", value=f"{format(chord_len, ',.0f')} mm", delta=f"Chord Between Shell Stations (W)", label_visibility="collapsed", border=True)

st.metric(label=f"Distance Between Stations (R)", value=f"{format(bot_st_distance, ',.0f')} mm", delta=f"Distance Between Bottom Stations (R)", label_visibility="collapsed", border=True)

