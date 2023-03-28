import sys #provide various fns and variables that are usef to manipulate different parts of the python runtime environemt.
#from src.logger import logging

def error_mess_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #this will return you the three values, we ignore the first two values and we consider only the third value(consist of which file,line the exception has occured)
    file_name = exc_tb.tb_frame.f_code.co_filename 
    error_message = "Error occured in python script name : {0}, line number: {1} , error message: {2}".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_mess_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message 
    
