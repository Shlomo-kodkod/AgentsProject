

class Menu:

    @staticmethod
    def display_menu() -> None:
        print("""
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
        
        -----------------------------------
        """)

    @staticmethod
    def is_valid_code_name(code_name: str):
        pass