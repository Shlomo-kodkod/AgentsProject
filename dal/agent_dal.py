import mysql.connector
from models.agent import Agent

class AgentDal:

    @staticmethod
    def get_db():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="eagleEyeDB")

    @staticmethod
    def add_agent(code_name: str, real_name: str, location: str, status: str, missions_completed: int) -> bool:
        try:
            db = AgentDal.get_db()
            with db.cursor() as cursor:
                sql = "INSERT INTO agents (codeName, realName, location, status, missionsCompleted) VALUES (%s, %s, %s, %s, %s)"
                val = (code_name, real_name, location, status, missions_completed)
                cursor.execute(sql, val)
                db.commit()
                print("Agent added successfully")
                return True
        except mysql.connector.Error as e:
            print(f"Error adding agent: {e}")
            return False

    @staticmethod
    def get_agent(code_name: str) -> Agent | None:
        try:
            db = AgentDal.get_db()
            with db.cursor() as cursor:
                sql = "SELECT * FROM agents WHERE  codeName = %s"
                val = (code_name, )
                cursor.execute(sql, val)
                result = cursor.fetchone()
                if not result:
                    return None
                agent = Agent(result[0], result[1], result[2], result[3], result[4], result[5])
                return agent
        except mysql.connector.Error as e:
            print(f"Error getting agent: {e}")
            return None

    @staticmethod
    def get_column_name(column_type: int) -> str:
        options = ("location", "status", "missionsCompleted")
        return options[column_type]

    @staticmethod
    def update_agent(code_name: str, column_num: int , new_value) -> bool:
        try:
            db = AgentDal.get_db()
            with db.cursor() as cursor:
                column = AgentDal.get_column_name(column_num)
                sql = f"UPDATE agents SET {column} = %s WHERE codeName = %s"
                val = (new_value, code_name)
                cursor.execute(sql, val)
                db.commit()
                print("Agent update successfully")
                return True
        except mysql.connector.Error as e:
            print(f"Error update agent: {e}")
            return False

    @staticmethod
    def delete_agent(code_name: str) -> bool:
        try:
            db = AgentDal.get_db()
            with db.cursor() as cursor:
                sql = f"DELETE FROM agents WHERE codeName = %s"
                val = (code_name, )
                cursor.execute(sql, val)
                db.commit()
                print("Agent delete successfully")
                return True
        except mysql.connector.Error as e:
            print(f"Error delete agent: {e}")
            return False

    @staticmethod
    def is_code_name_exist(code_name: str) -> bool:
        try:
            db = AgentDal.get_db()
            with db.cursor() as cursor:
                sql = "SELECT codeName FROM agents WHERE  codeName = %s"
                val = (code_name,)
                cursor.execute(sql, val)
                result = cursor.fetchall()
                if not result:
                    return False
                return True
        except mysql.connector.Error as e:
            print(f"Error getting agent: {e}")
            return True
