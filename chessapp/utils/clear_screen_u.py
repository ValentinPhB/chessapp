import os


class Clear:
    """
    Clear screen.
    """
    @staticmethod
    def screen():
        os.system('cls' if os.name == 'nt' else 'clear')
