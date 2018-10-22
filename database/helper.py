import sys
import inspect
try:
    import programs
except:
    import database.programs

class ProgramLoader(object):
      
    try:
        PROGRAM_MODULE = programs
    except:
        PROGRAM_MODULE = database.programs 
    
    def __init__(self, *args, **kwargs):
        self.program_list = self._generateProgramList()

    def _program_list(self):
        program_list = inspect.getmembers(self.PROGRAM_MODULE, inspect.isclass)
        return program_list[1:]

    def _getProgramClass(self, program_name):
        program_class = self.program_list[program_name]
        return program_class

    def _generateProgramList(self, *args, **kwargs):
        program_list_raw = self._program_list()
        program_list = {}
        
        for (program_class_name, program_class) in program_list_raw:
            program_instance = program_class()
            program_list.update({
                program_instance.program_name: program_class
            })
        return program_list


    @staticmethod
    def programInfoDict(program_instance):
        return {
                'name': program_instance.program_name,
                'description': program_instance.description,
                'inputs': program_instance.inputs,
                'outputs': program_instance.outputs
            }

    def programInfo(self, program_name, *args, **kwargs):
        program_instance = self._getProgramClass(program_name)()
        inputs = program_instance.inputs
        outputs = program_instance.outputs

        return (program_instance, inputs, outputs)        

    def programInfoText(self, program_name, *args, **kwargs):
        program_instance, inputs, outputs = self.programInfo(program_name)
        program_info_dict = self.programInfoDict(program_instance)
        program_info_dict['inputs']['types'] = [typ.__name__ for typ in inputs['types']]
        program_info_dict['outputs']['types'] = [typ.__name__ for typ in outputs['types']]
        
        return program_info_dict

    def programsInfoList(self, *args, **kwargs):
        program_list = []
        
        for program_name, _ in self.program_list.items():
            program_info = self.programInfoText(program_name)
            program_list.append(program_info)
        return program_list

    def runProgram(self, program_name, *args, **kwargs):
        program_instance = self._getProgramClass(program_name)()

        output = program_instance.execute(*args, **kwargs)
        
        return output