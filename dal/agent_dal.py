import mysql.connector
from models.agent import Agent
from dal.agent_field import AgentField

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
        db = AgentDal.get_db()
        try:
            with db.cursor() as cursor:
                sql = "INSERT INTO agents (codeName, realName, location, status, missionsCompleted) VALUES (%s, %s, %s, %s, %s)"
                val = (code_name, real_name, location, status, missions_completed)
                cursor.execute(sql, val)
                db.commit()
                print("Agent added successfully")
                return True
        except mysql.connector.Error as e:
            print(f"Error while adding agent: {e}")
            return False
        finally:
            db.close() if db else None


    @staticmethod
    def get_agent(code_name: str) -> Agent | None:
        db = AgentDal.get_db()
        try:
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
            print(f"Error while retrieving agent: {e}")
            return None
        finally:
            db.close() if db else None

    @staticmethod
    def update_agent(code_name: str, column: AgentField , new_value) -> bool:
        db = AgentDal.get_db()
        try:
            with db.cursor() as cursor:
                sql = f"UPDATE agents SET {column} = %s WHERE codeName = %s"
                val = (new_value, code_name)
                cursor.execute(sql, val)
                db.commit()
                print("Agent updated successfully")
                return True
        except mysql.connector.Error as e:
            print(f"Error while updating agent: {e}")
            return False
        finally:
            db.close() if db else None

    @staticmethod
    def delete_agent(code_name: str) -> bool:
        db = AgentDal.get_db()
        try:
            with db.cursor() as cursor:
                sql = f"DELETE FROM agents WHERE codeName = %s"
                val = (code_name, )
                cursor.execute(sql, val)
                db.commit()
                print("Agent deleting successfully")
                return True
        except mysql.connector.Error as e:
            print(f"Error while deleting agent: {e}")
            return False
        finally:
            db.close() if db else None

    @staticmethod
    def is_code_name_exists(code_name: str) -> bool:
        db = AgentDal.get_db()
        try:
            with db.cursor() as cursor:
                sql = "SELECT codeName FROM agents WHERE  codeName = %s"
                val = (code_name,)
                cursor.execute(sql, val)
                result = cursor.fetchall()
                if not result:
                    return False
                return True
        except mysql.connector.Error as e:
            print(f"Error while checking code name: {e}")
            return True
        finally:
            db.close() if db else None
