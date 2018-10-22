try:
    from program import AbstractProgram
except:
    from database.program import AbstractProgram
    
class SquareProgram(AbstractProgram):
    PROGRAM_NAME = 'Square'
    DESCRIPTION = 'Squares a single number.'
    N_INPUTS = [int]
    N_OUTPUTS = [int]
    
    def execute(self, *args, **kwargs):
        # Returns the square of the passed number
        number = args[0]
        
        return number**2