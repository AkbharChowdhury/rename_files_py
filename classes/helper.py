class Helper:
    @staticmethod
    def valid_input(item):
        if not isinstance(item, str):
            print('Error: you must enter a valid file path and must not start with a number')
            return False
        if item == '':
            print('file directory cannot be empty')
            return False
        return True
