import os, config
import streamlit as st
import pinecone_api, database
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper



# App framework
st.set_page_config(page_title='YourNextStep', page_icon=':book:')

prompt = st.text_area('Enter your career path')


def side():
    print( "Sidebar")

sidebar = st.sidebar.markdown("<span class='note'>Operations</span></br>",unsafe_allow_html=True)
id = st.sidebar.text_input("Enter Your ID")

st.sidebar.selectbox("SeLect Ops",['Read','Update'])

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
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #4267B2;">
    <a class="navbar-brand" href="#"  target="_blank">YourNextStep</a>  
    </nav>
""",
    unsafe_allow_html=True,
)
# Embed Bootstrap CSS
st.markdown(
    '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">',
    unsafe_allow_html=True
)

# Prompt templates
title_template = PromptTemplate(
    input_variables=['topic'],
    template='Recommend {topic}'
)

script_template = PromptTemplate(
    input_variables=['title', 'wikipedia_research'],
    template='Write me a recommendation on my career path about {title} while leveraging this Wikipedia research: {wikipedia_research}'
)

# Memory
# title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
# script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')



title_memory = pinecone_api.memory(input_key='topic', memory_key='chat_history')
script_memory = pinecone_api.memory(input_key='title', memory_key='chat_history')

# Llms
llm = OpenAI(api_key=config.OPENAI_KEY, temperature=0.9)
title_chain = LLMChain(llm=llm,  prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

wiki = WikipediaAPIWrapper()

if prompt: 
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt) 
    script = script_chain.run(title=title, wikipedia_research=wiki_research)
    
    # Store in DB like this
    database.title_memory.append(title)
    database.script_memory.append(script)
    database.wiki_memory.append(wiki_research)

    # st.write(title) 
    # st.write(script) 

    with st.expander('Title History'): 
        st.info(database.title_memory)

    with st.expander('Script History'): 
        st.info(database.script_memory)

    with st.expander('Wikipedia Research'): 
        st.info(database.wiki_memory)