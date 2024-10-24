import streamlit as st 
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq


st.set_page_config(page_title="SPEAKDB",page_icon="🗣️")
st.title("SPEAK WITH YOUR DATABASE")

LOCALDB="USE_LOCALDB"
MYSQL="USE_MYSQL"


radio_opt=["Use SQLlite 3 Database","Connect To Your SQL Database"]
selected_opt=st.sidebar.radio(label="Choose the DB Which You want to CHAT WITH")


if radio_opt.Index(selected_opt)==1:
    db_uri=MYSQL
    mysql_host=st.sidebar.text_input("Provide MYSQL Host")
    mysql_user=st.sidebar.text_input("MYSQL User")
    mysql_password=st.sidebar.text_input("MYSQL Password",type="password")
    mysql_db=st.sidebar.text_input("MySQL Database")
else:
    db_uri=LOCALDB    
    
    
api_key=st.sidebar.text_input(label="GROQ_API_KEY",type="password")