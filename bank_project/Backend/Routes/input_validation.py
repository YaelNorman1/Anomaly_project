class Validator():

    def no_input(self, input):
        if input==None or input=="":
            return True
        else:
            return False

    def is_string(self, input):
        return input.isalpha()

    def is_numeric(self, input):
        return input.isnumeric()

    def in_blacklist(self, input):
        pass
 
    def in_whitelist(self, input):
        pass               