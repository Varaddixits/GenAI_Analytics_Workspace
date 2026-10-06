import sqlite3
import pandas as pd 

# 1. Establish a secure localized handshake connection to your database file
database_connection = sqlite3.connect('market_data.db')

# 2. Use the Pandas framework to run an automated SQL read pass
query_string = "SELECT * FROM placements"
dataframe = pd.read_sql_query(query_string, database_connection)

print("-- RAW INTAKE FROM D : DRIVE SQL DATABASE --")
print(dataframe)


# 3. Clean and normalize the text metrics for the AI layer
dataframe['role'] = dataframe['role'].str.upper()

print("\n --- READY FOR AI PROCESSING")
print(dataframe)


# 4. Safely close the pipe connection link
database_connection.close()