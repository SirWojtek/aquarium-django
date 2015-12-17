
class Status():
    def __init__(self, temperature, manual_mode):
        self.temperature = temperature
        self.manual_mode = bool(manual_mode)
        self.heating_status = None
        self.filter_status = None
        self.light_status = None
        self.last_update = None

class Settings():
    def __init__(self, temperature):
        self.temperature = temperature
        self.heating_status = None
        self.filter_status = None
        self.light_status = None
        self.last_update = None
