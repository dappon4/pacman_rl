from agent import Agent

class Ghost(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
    