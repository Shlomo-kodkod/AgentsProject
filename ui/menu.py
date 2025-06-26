from ui.manager import Manager
from ui.input_utilities import InputUtils

class Menu:

    MENU_SCREEN = """
-----------------------------------
          ***************          
           Agents manager
          ***************
 
 1. Add a new agent
 2. View agent details
 3. Update agent location
 4. Update agent status
 5. Update agent missions completed
 6. Delete an agent
 0. Exit
-----------------------------------
        """


    @staticmethod
    def display_menu() -> None:
        print(Menu.MENU_SCREEN)

    @staticmethod
    def run():
        user_choice = -1
        while user_choice != 0:
            Menu.display_menu()
            user_choice = InputUtils.get_choice()
            if user_choice == 0:
                break
            Manager.execute_choice(user_choice)
        print("Exit...")
