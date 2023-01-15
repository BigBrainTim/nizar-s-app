import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd

st.set_page_config(page_title="N mz", layout="wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css("style/style.css")

# ------ load assets ----
lottie_coding = load_lottie("https://assets9.lottiefiles.com/packages/lf20_b7t4ylgj.json")

with st.container():
    st.title("Hi, i'm Nizar mouzrii :wave:")

#------ About me ------

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me")
        st.write("##")
        st.write("""
        - My name is Nizar. I have always been passionate about education. From a young age, I knew that I wanted to pursue a career in science.I was a good student in school. I worked hard and always strived to do my best.
        - then I was accepted into a prestigious university to study science. It was a dream come true.I loved the hands-on approach of the university and was able to conduct research in my field of interest.
        - But it hasn't been easy. The workload is intense and I often feel overwhelmed. But I know that it will all be worth it in the end.
        """)
    with right_column:
        st_lottie(lottie_coding)

#------ Skills ---------

with st.container():
    st.write("---")
    st.header("Skills")
    st.write("##")
    data = {"language":["Science", "maths", "Frensh", "Arabic", "English"], "rate":[5,4,4,5,5]}

    data=pd.DataFrame(data)

    data = data.set_index("language")

    st.bar_chart(data)

# ------ Contact form -------

with st.container():
    st.write("---")
    st.subheader("Contact me")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/nizarelmazria@gmail.com" method="POST">
        <input type="text" name="name" placeholder="name" required>
        <input type="email" name="email" placeholder="e-mail" required>
        <textarea name="message" placeholder="enter your message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

