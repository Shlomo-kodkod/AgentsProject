import mysql.connector

class AgentDal:
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eagleEyeDB"
    )



