# Call Center: Imagine you have a call center with three levels of employees: respondent, manager,
# and director. An incoming telephone call must be first allocated to a respondent who is free. If the
# respondent can't handle the call, he or she must escalate the call to a manager. If the manager is not
# free or not able to handle it, then the call should be escalated to a director. Design the classes and
# data structures for this problem. Implement a method dispatchCall() which assigns a call to
# the first available employee.

class Respondent(object):
    def __init__(self, call):
        self.call = call
    
    def takeCall(self):
        # determine if respondent can take the call
        # return true or false

class Manager(object):
    def __init__(self, call):
        self.call = call
    
    def takeCall(self):
        # determine if manager can take the call
        # return true or false

class Director(object):
    def __init__(self, call):
        self.call = call
    
    def takeCall(self):
        # determine if director can take the call
        # return true or false

class CallCenter(object):
    def __init__(self, call= None, employees = []):
        self.call = call
        self.employees = employees

    def dispatchCall(self):
        # dispatch calls to respondents
        # if false:
        # dispatch calls to managers
        # if false:
        # dispatch calls to directors

