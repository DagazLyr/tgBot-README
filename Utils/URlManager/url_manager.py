
class UrlParser:
    def __init__(self, url, params_list_substr='==pl==', params_substr='--_--') -> None:
        self.params=dict()

        for pair in (url.split(' ')[-1]).split(params_list_substr):
            parameter = pair.split(params_substr)

            if (len(parameter)>1):
                key = 0
                value = 1
                self.params[parameter[key]] = parameter[value]
        
    def __str__(self) -> str:
        return "|".join(self.params)
    
    def get(self,parameter_name):
        if parameter_name in self.params:
            return self.params[parameter_name]
        return None
    