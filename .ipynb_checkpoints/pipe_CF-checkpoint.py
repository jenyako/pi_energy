import streamlit as st
import math


st.set_page_config(page_title="Tape Length Calculation", layout="wide")
st.image('https://static.wixstatic.com/media/7a68aa_023f914caedb43e6b3377626233b3aaa~mv2.png/v1/fill/w_234,h_90,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/PI%20LOGO_PNG_transparency.png')
st.title("Wrapping Tape Length Calculator")

# === Диаметр трубы ===
col1, col2 = st.columns([1, 2])
with col1:
     st.subheader("Pipe D [in]: :red[*]")
with col2:
    diameter_options = ['4\"', '6\"', '8\"', '10\"', '12\"', "Custom Value"]
    selected_d = st.pills(
        label="Standard Diameters",
        options=diameter_options,
        format_func=str,
        selection_mode="single",
        key="d_pills",
        label_visibility="collapsed"
    )

    if selected_d == "Custom Value":
        pipe_d = st.number_input("Input Diameter", min_value=0.1, value=None, step=0.1, key="pipe_d", label_visibility="collapsed")
    elif selected_d is not None:
        pipe_d = float(selected_d.replace('"', ''))
    else:
        pipe_d = None

st.divider()

# === Длина трубы ===
# col5, col6 = st.columns([1, 2])
# with col5:
#     st.markdown("**Pipe L [mm]:**")
# with col6:
#     pipe_l = st.number_input("Input Length:", min_value=1, value=None, step=10, key="pipe_l", label_visibility="collapsed")


col5, col6 = st.columns([1, 2])
with col5:
     st.subheader("Pipe L [mm]: :red[*]")
with col6:
    length_options = ['300 mm', '400 mm', '500 mm', '600 mm', '800 mm', '1000 mm', "Custom Value"]
    selected_l = st.pills(
        label="Standard Lengths",
        options=length_options,
        format_func=str,
        selection_mode="single",
        key="l_pills",
        label_visibility="collapsed"
    )

    if selected_l == "Custom Value":
        pipe_l = st.number_input("Input Length", min_value=1, value=None, step=50, key="pipe_l", label_visibility="collapsed")
    elif selected_l is not None:
        pipe_l = float(selected_l.replace(' mm', ''))
    else:
        pipe_l = None

st.divider()

# === Ширина ленты ===
col3, col4 = st.columns([1, 2])
with col3:
    st.subheader("Tape Width [in]: :red[*]")
with col4:
    width_options = ['2\"', '4\"', '6\"', "Custom Value"]
    selected_w = st.pills(
        label="Standard Widths",
        options=width_options,
        format_func=str,
        selection_mode="multi",
        key="w_pills",
        default=['2\"', '4\"', '6\"'],
        label_visibility="collapsed"
    )

    custom_width = None
    if "Custom Value" in selected_w:
        custom_width = st.number_input("Input Width:", min_value=0.1, value=None, step=1, key="tape_w", label_visibility="collapsed")

    width_list = [float(w.replace('"', '')) for w in selected_w if isinstance(w, str) and w != "Custom Value"]
    if custom_width is not None:
        width_list.append(custom_width)

st.divider()

# === Перекрытие ===
col7, col8 = st.columns([1, 2])
with col7:
     st.subheader("Tape Overlap [%]: :red[*]")
with col8:
    overlap = st.number_input("Input Tape Overlap:", min_value=0, max_value=90, value=50, step=10, key="overlap", label_visibility="collapsed")

# === Проверка и расчёт ===
if pipe_d is None or pipe_l is None or not width_list:
    st.warning("Enter all Parameters")
    st.stop()


st.divider()

st.header("Results", divider=True)

for w in width_list:
    if w * (1 - overlap / 100) == 0:
        st.error(f"Wrong overlap value {w}" )
    else:
        tape_length = math.pi * pipe_d * 25.4 * pipe_l / (w * 25.4 * (1 - overlap / 100))
        
        #st.success(f"Tape {w:.0f}\" → {tape_length:.1f} mm")

        st.metric(label=f"Tape {w:.0f}\"", value=f"{format(tape_length, ',.1f')} mm", delta=f"Tape {w:.0f}\"", label_visibility="collapsed", border=True)

