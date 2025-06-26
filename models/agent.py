

class Agent:

    def __init__(self, agent_id: int, code_name: str, real_name: str, location: str, status: str, missions_completed: int):
        self.__agent_id = agent_id
        self.__code_name = code_name
        self.__real_name = real_name
        self.__location = location
        self.__status = status
        self.__missions_completed = missions_completed

    def __str__(self):
        info = (f"Agent ID: {self.__agent_id}. \nCode name: {self.__code_name}.\n" +
                f"Real name: {self.__real_name}. \nLocation: {self.__location}.\n" +
                f"Status: {self.__status}. \nMissions completed:{self.__missions_completed}"
                )
        return info






