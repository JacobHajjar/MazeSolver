'''class file for the AI algorithm'''
class MazeSolver():
    '''class that solves maze using A* algorithm'''

    def __init__(self, types):
       self.types = types

    def printTest(self):
        print(self.types.COM.value)