class Logger:
    """Object to encapsulate logging methods for a given name."""

    def __init__(self, name: str, root: str) -> None:
        self.name = name
        self.root_route = root

    async def debug(self, message: str) -> None:
        print(message)
