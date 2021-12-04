import curses
import time
from dataclasses import dataclass



@dataclass
class Data:
    height : int = 5
    width  : int = 20



class App(Data):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
        # curses init

    def screen_init(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()

    def restoreScreen(self):
        curses.nocbreak()
        curses.echo()
        curses.endwin()
    
    
    
    def draw(self):
        pass

    def run(self):
        pass



print("This is working....")






