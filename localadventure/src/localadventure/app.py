"""
App for travellers and qstreet quests lovers
"""
from toga import App, Window, Box, Button, Label, MainWindow
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class LocalAdventure(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = Box()
        label = Label('Hellow, word')
        button = Button('Next ->')
        main_box.add(label)
        main_box.add(button)

        self.main_window = MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return LocalAdventure()
