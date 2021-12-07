"""
This module defines classes for parameters needed to respond to conversational queries.
"""

__version__ = '0.1'
__author__ = 'Davide L'

class Parameter():

    def __init__(self, name, required, value, is_list, prompts, default):
        self.name = name
        self.required = required
        self.value = value
        self.is_list = is_list
        self.prompts = prompts
        self.default = default


class Date(Parameter):

    def __init__(self, name, required, value, is_list, prompts, default):
        Parameter.__init__(name, required, value, is_list, prompts, default)
        # here you can add more things for the constructor of the child class

    def parse_date(self):
        pass