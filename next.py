import os
from dotenv import load_dotenv,find_dotenv
import streamlit as st
load_dotenv(find_dotenv())
apikey = os.environ["API_KEY"] 


# App framework
st.set_page_config(page_title='Bot', page_icon=':bot:')

st.markdown(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css" rel="stylesheet">',
    unsafe_allow_html=True,
)
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
st.markdown("""""", unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
                header{visibility:hidden;}
                .main {
                    margin-top: -20px;
                    padding-top:10px;
                }
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
               
.main-timeline-5 {
  position: relative;
  max-width: 50%;
  margin: 0 auto;
}


.main-timeline-5::after {
  content: "";
  position: absolute;
  width: 3px;
  background-color: #fff;
  top: 0;
  bottom: 0;
  left: auto;
  margin-left: -3px;
}

/* Container around content */
.timeline-5 {
  position: relative;
  background-color: inherit;
  width: 100%;
}

/* The circles on the timeline */
.timeline-5::after {
  content: "";
  position: absolute;
  width: 17px;
  height: 17px;
  right: 1px;
  background-color: #fff;
  top: 18px;
  border-radius: 50%;
  z-index: 1;
}

/* Place the container to the right */
.right-5 {
  padding: 0px 0px 20px 40px;
  left: auto;
}

/* Add arrows to the right container (pointing left) */
.right-5::before {
  content: " ";
  position: absolute;
  top: 18px;
  z-index: 1;
  left: 30px;
  border: medium solid #fff;
  border-width: 10px 10px 10px 0;
  border-color: transparent #fff transparent transparent;
}

/* Fix the circle for containers on the right side */
.right-5::after {
  left: -10px;
}

@media (max-width: 991px) {
  .main-timeline-5 {
    max-width: 100%;
  }
}
.gradient-custom-5 {
  /* fallback for old browsers */
  background: #ebbba7;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(
    to right,
    rgba(235, 187, 167, 1),
    rgba(207, 199, 248, 1)
  );

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(
    to right,
    rgba(235, 187, 167, 1),
    rgba(207, 199, 248, 1)
  );
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: purple;">
    <a class="navbar-brand" href="#"  target="_blank">Bot</a>  
    </nav>
""",
    unsafe_allow_html=True,
)
# Embed Bootstrap CSS
st.markdown(
    '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">',
    unsafe_allow_html=True
)

import numpy as np

with st.chat_message("assistant"):
    st.write("Hello human")
    st.bar_chart(np.random.randn(30, 3))