'''
Created on Feb 23, 2013

@author: nino
'''

class WorkflowException(Exception):
    pass

class Abort(WorkflowException):
    pass


