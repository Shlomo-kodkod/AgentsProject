
from dal.agent_dal import AgentDal

class Menu:

    MENU_SCREEN = """
-----------------------------------
          ***************
           Agent manager
          ***************
 
 1. Add new agent
 2. Get agent details
 3. Update agent location
 4. Update agent status
 5. Update agent missions completed
 6. Delete agent
 0. Exit
-----------------------------------
        """

    @staticmethod
    def display_menu() -> None:
        print(Menu.MENU_SCREEN)

    @staticmethod
    def get_choice() -> int:
        options = ('1', '2', '3', '4', '5', '6', '0')
        choice = input("Enter your choice: ")
        while not choice.isdigit() or choice not in options:
            print("Invalid choice. Try again.")
            choice = input("Enter your choice: ")
        return int(choice)

    @staticmethod
    def get_code_name(validate_existence: bool = False) -> str:
        code_name = input("Enter code name: ")
        if validate_existence:
            while not AgentDal.is_code_name_exist(code_name):
                print("Is not exist. Try with other code name.")
                code_name = input("Enter code name: ")
        else:
            while AgentDal.is_code_name_exist(code_name):
                print("Is already exist. Try with other code name.")
                code_name = input("Enter code name: ")
        return  code_name


    @staticmethod
    def get_missions_completed() -> int:
        missions_completed = input("Enter missions completed: ")
        while not missions_completed.isdigit():
            print("This must to be a number. Please try again.")
            missions_completed = input("Enter missions completed: ")
        return int(missions_completed)

    @staticmethod
    def get_agent_info():
        code_name = Menu.get_code_name()
        real_name = input("Enter real name: ")
        location = input("Enter location: ")
        status = input("Enter status: ")
        missions_completed = Menu.get_missions_completed()
        return code_name, real_name, location, status, missions_completed

    @staticmethod
    def create_agent():
        info = Menu.get_agent_info()
        AgentDal.add_agent(info[0],info[1],info[2],info[3], info[4])

    @staticmethod
    def delete_agent():
        code_name = Menu.get_code_name(True)
        AgentDal.delete_agent(code_name)

    @staticmethod
    def get_agent():
        code_name = Menu.get_code_name(True)
        agent = AgentDal.get_agent(code_name)
        print(agent)

    @staticmethod
    def update_agent(d_type: int):
        code_name = Menu.get_code_name(True)
        new_data = input("Enter the new value: ")
        AgentDal.update_agent(code_name, d_type, new_data)

    @staticmethod
    def execute_choice(user_choice):
        options = {1: Menu.create_agent, 2: Menu.get_agent,
                   3: lambda: Menu.update_agent(0), 4: lambda: Menu.update_agent(1),
                   5: lambda: Menu.update_agent(2), 6: lambda: Menu.delete_agent}
        return options[user_choice]()

    @staticmethod
    def run():
        user_choice = -1
        while user_choice != 0:
            Menu.display_menu()
            user_choice = Menu.get_choice()
            if user_choice == 0:
                break
            Menu.execute_choice(user_choice)
        print("Exit")
