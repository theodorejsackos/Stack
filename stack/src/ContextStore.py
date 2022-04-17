
from dataclasses import dataclass
import time

@dataclass
class StackContext():
    description: str
    timestamp: float

    def __init__(self, description: str):
        self.description = description
        self.timestamp = time.time()

class StackContextStore():
    def __init__(self):
        pass

    def push(self, context: StackContext):
        pass

    def pop(self) -> StackContext:
        pass

    def list(self, at_most: int = 5) -> StackContext:
        pass

class MemoryStackContextStore(StackContextStore):
    def __init__(self):
        super().__init__()
        self.stack = []

    def push(self, context: StackContext):
        # self.stack = [x for x in self.stack]
        self.stack.append(context)

    def pop(self) -> StackContext:
        if (len(self.stack) == 0):
            return None
        else:
            return self.stack.pop()

    def list(self, at_most: int = 5) -> StackContext:
        copy = self.stack.copy()
        copy.reverse()
        return copy[:at_most]

def create_ctx(in_memory: bool, location: str = None) -> StackContextStore:
    if (in_memory):
        return MemoryStackContextStore()
    elif (location != None):
        # TODO: Add an implementation with persistent storage
        # return SQLiteStackContextStore()
        return MemoryStackContextStore()
    else:
        raise Exception('Cannot create a context store with the provided arguments')
