class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.store:
            self.store[key] = []

        if (timestamp, value) not in self.store[key]:
            self.store[key].append((timestamp, value))


        
        

    def get(self, key: str, timestamp: int) -> str:


        if not key in self.store:
            return ""

        values = self.store[key]

        result = ""

        for t,v in values:
            if t <= timestamp:
                result = v
            else:
                break


        
        return result

        
