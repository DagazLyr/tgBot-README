class EnumStatuses:
    SUCCESS = "SUCESS"
    ERROR = "ERROR"
    NONE = None

class ResultType:
    def __init__(self, status: EnumStatuses, description : str = "", **kwargs) -> None:
        self.status = status
        self.data = kwargs
        self.description = description

    def __str__(self) -> str:
        return f"Status: {self.status} | data: {self.data} | description: {self.description}"
    
    def get(self,key: str):
        if key in self.data:
            return self.data[key]
        return None
    
    def set(self, key, value):
        self.data[key] = value