# System-specific parameters and functions. 
# This module provides access to some variables used 
# or maintained by the interpreter and to functions 
# that interact strongly with the interpreter. 
# It is always available. Unless explicitly noted 
# otherwise, all variables are read-only.

import sys 


def error_message_detail(error, error_detail:sys):
    _,_,exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    line_number = exec_tb.tb_lineno
    error_message = "Error occured in python scrip name [{0}] line number [{1}] error message[{2}]".format(file_name,line_number,str(error))
    
    return error_message


class CustomeException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)


    def __str__(self):
        return self.error_message   
    


