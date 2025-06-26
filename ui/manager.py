from dal.agent_dal import AgentDal
from dal.agent_field import AgentField
from ui.input_utilities import InputUtils


class Manager:
    @staticmethod
    def create_agent():
        info = InputUtils.get_agent_info()
        AgentDal.add_agent(info[0], info[1], info[2], info[3], info[4])


    @staticmethod
    def delete_agent():
        code_name = InputUtils.get_existing_code_name()
        AgentDal.delete_agent(code_name)


    @staticmethod
    def get_agent():
        code_name = InputUtils.get_existing_code_name()
        agent = AgentDal.get_agent(code_name)
        print(agent) if agent else print("Agent not found.")


    @staticmethod
    def update_agent(column: AgentField):
        code_name = InputUtils.get_existing_code_name()
        new_data = input("Enter the new value: ")
        AgentDal.update_agent(code_name, column, new_data)


    @staticmethod
    def execute_choice(user_choice):
        match user_choice:
            case 1: Manager.create_agent()
            case 2: Manager.get_agent()
            case 3: Manager.update_agent(AgentField.LOCATION)
            case 4: Manager.update_agent(AgentField.STATUS)
            case 5: Manager.update_agent(AgentField.MISSIONS_COMPLETED)
            case 6: Manager.delete_agent()

