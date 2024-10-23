import pandas as pd
from sqlalchemy import create_engine

# Define your database connection parameters
username = 'root'
password = '1043'
host = 'localhost'  # or your database host
database = 'employee_data'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')


# Load CSV data into a DataFrame
df = pd.read_csv('D:/github/Generative-AI/SpeakDB/Employee.csv')

# Load DataFrame into the SQL table
df.to_sql('employee_data', con=engine, if_exists='replace', index=False)
