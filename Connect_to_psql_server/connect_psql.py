#!/usr/bin/env python3.9
#!pip install pandas
#!pip install deepdiff

import psycopg2
import pandas as pd
import numpy as np
import csv
from deepdiff import DeepDiff

def get_engagements():
    
    sql = (
        """
        SELECT engagements.external_id 
                FROM att.engagements
                WHERE created_at 
                BETWEEN '2021-10-15 05:00:00' AND '2021-10-16 05:00:00';
                """
    )

    # Connect to postgreSQL database server
    conn = None
    try:
        print('Connecting to the PostgreSQL database... ')

        conn = psycopg2.connect(
        host="",
        database="",
        user="",
        port="5475",
        password=""
        )

        # create a cursor
        cur = conn.cursor()

        # confirmation message that you connected safely
        print('You are connected to the database!')

        # execute the sql query
        cur.execute(sql) 
        
        # fetchall() returns all response data from query
        # li1 = []
        rows = cur.fetchall()
        li1 = [row[0] for row in rows]
        print(li1)
        print(len(li1))

        
        #  close the communication with the server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

        

            col_list = ["date", "contact_id"]
            df = pd.read_csv("agent_roster_1015.csv", usecols=col_list)
            list_int = list(df["contact_id"])
            list_str = map(str, list_int)          
            li2 = list(list_str)
            print(li2)
    
            set_difference = set(li2) - set(li1)
            print(set_difference)
            print(len(set_difference))

if __name__ == '__main__':
    get_engagements()



# psql -U cobot_telco -p 5475 -h hiper-cobot-telco-prod.czcuzshnoikb.us-east-1.rds.amazonaws.com cobot_telco