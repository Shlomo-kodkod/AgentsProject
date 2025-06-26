import mysql.connector

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



