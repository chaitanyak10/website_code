from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title='My Webpage', page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_zhlilvp4mj.json")
img_contact_form = Image.open(r"C:\Users\chait\images\my_profile.png")

st.subheader("Hi, I am Chaitanya Kulkarni :wave:")
st.title("A Data Analyst from India")
st.write("I am passionate about finding ways to use Python and Data Visualization for making business decisions based "
         "on data")
st.write("[Learn More >](https://pythonandtableau.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(

            """I'm a Developer Analyst BI Engineer who works as :
            - Interacting with stake-holders and gather the business requirements
            - Fetch the data from multiple data sources by writing SQL queries
            - Use ETL tool like SSIS to stage and clean the data
            - Use python for data science projects
            - Create analytical dashboards using tableau
            
            If this sounds interesting to you, consider hiring me!!!
            """
        )
        st.write("[Tableau Public Profile >](https://public.tableau.com/app/profile/ckvisualization)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("My Tableau Journey presentation at Tableau Fringe Festival")
        st.write(
            """
            Chaitanya shares the experience of creating a Tableau dashboard for measuring the warehouse KPI's, analysing trends and breaking them down by different dimensions, 
            which led to needing to understanding data granularity, link the data from multiple data sources, dealing with data and time calculations, learning about LOD calculations, and so much more!  
            This talk is great for any Tableau beginner.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=DehE7_rroUk)")

with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/chaitanya.ukulkarni@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your email ID" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
