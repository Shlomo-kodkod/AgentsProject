from dal.agent_dal import AgentDal

class InputUtils:

    MENU_OPTIONS = ('1', '2', '3', '4', '5', '6', '0')

    @staticmethod
    def get_choice() -> int:
        choice = input("Enter your choice: ")
        while not choice.isdigit() or choice not in InputUtils.MENU_OPTIONS:
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")
        return int(choice)

    @staticmethod
    def get_unique_code_name():
        code_name = input("Enter code name: ")
        while AgentDal.is_code_name_exists(code_name):
            print("This code name already exists. Please choose another.")
            code_name = input("Enter code name: ")
        return code_name

    @staticmethod
    def get_existing_code_name():
        code_name = input("Enter code name: ")
        while not AgentDal.is_code_name_exists(code_name):
            print("This code name does not exist. Please try again")
            code_name = input("Enter code name: ")
        return code_name

    @staticmethod
    def get_missions_completed() -> int:
        missions_completed = input("Enter missions completed: ")
        while not missions_completed.isdigit():
            print("This must be a number. Please try again.")
            missions_completed = input("Enter missions completed: ")
        return int(missions_completed)


    @staticmethod
    def get_agent_info():
        code_name = InputUtils.get_unique_code_name()
        real_name = input("Enter real name: ")
        location = input("Enter location: ")
        status = input("Enter status: ")
        missions_completed = InputUtils.get_missions_completed()
        return code_name, real_name, location, status, missions_completed