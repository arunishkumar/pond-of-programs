"""
    AbstractProgram for building a custom program.

    To build a custom program for execution via the REST API:
        - Open `programs.py` for editing.
        - Extend the AbstractProgram class for your program. Follow the example program
"""

class AbstractProgram(object):
    """
        AbstractProgram
        Defaults:
            Program Name: Class Name
            Inputs: 1 Integer
            Outputs: 1 Integer

        To create a new program:
            - Extend this class i.e AbstractProgram
            - Define the `PROGRAM_NAME`
            - Define the no of inputs `N_INPUTS`
            - Define the no of outputs `N_OUTPUTS`
            
            Example Program:

                class MyProgram(AbstractProgram):
                    PROGRAM_NAME = 'MyProgram'
                    N_INPUTS = [int]
                    N_OUTPUTS = [int]
                    
                    def execute(self, *args, **kwargs):
                        # Returns the square of the passed number
                        number = args[0]
                        
                        return number**2
    """
    
    PROGRAM_NAME = ''
    DESCRIPTION = ''
    N_INPUTS = [int]
    N_OUTPUTS = [int]

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    @property
    def description(self, *args, **kwargs):
        """
            Returns DESCRIPTION
        """
        return self.DESCRIPTION

    @property
    def program_name(self, *args, **kwargs):
        """
            Returns PROGRAM_NAME if it is defined 
            else the name of the class.
        """
        if self.PROGRAM_NAME is not '':
            return self.PROGRAM_NAME
        else:
            return self.__class__.__name__

    @property
    def inputs(self):        
        """
            Get a dictionary containing information of type of 
            inputs and no of inputs required for the program.
        """
        return {
            'n': len(self.N_INPUTS),
            'types': self.N_INPUTS
        }
    @property
    def outputs(self):
        """
            Get a dictionary containing information of type of 
            ouputs and no of outputs required for the program.
        """
        return {
            'n': len(self.N_OUTPUTS),
            'types': self.N_OUTPUTS
        }

    def execute(self, *args, **kwargs):
        """
            Execute the program.
        """
        raise NotImplementedError
