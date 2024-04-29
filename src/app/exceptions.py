class catchable(Exception):
    status_code:int
    message:str
    def get_status_code(self):
        return self.status_code
    def get_message(self):
        return self.message