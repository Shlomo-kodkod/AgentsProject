import mysql.connector
from models.agent import Agent

class AgentDal:
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eagleEyeDB"
    )

    def add_agent(self, code_name: str, real_name: str, location: str, status: str, missions_completed: int):
        try:
            with self.db.cursor() as cursor:
                sql = "INSERT INTO agents (codeName, realName, location, status, missionsCompleted) VALUES (%s, %s, %s, %s, %s)"
                val = (code_name, real_name, location, status, missions_completed)
                cursor.execute(sql, val)
                self.db.commit()
                print("Agent added successfully")
        except mysql.connector.Error as e:
            print(f"Error adding agent: {e}")

    def get_agent(self, code_name: str) -> Agent | None:
        try:
            with self.db.cursor() as cursor:
                sql = "SELECT * FROM agents WHERE  codeName = %s"
                val = (code_name, )
                cursor.execute(sql, val)
                result = cursor.fetchall()[0]
                agent = Agent(result[0], result[1], result[2], result[3], result[4], result[5])
                return agent
        except mysql.connector.Error as e:
            print(f"Error getting agent: {e}")







