import os
import utilities

class Document:
    def __init__(self, docName:str, autoInc:bool=True) -> None:
        self.docName = docName
        self.location = os.getcwd()
        self.autoInc = autoInc
        self.docExists = utilities.validate(self.location, self.docName)
        self.data = []

    def fileContents(self) -> None:
        if self.docExists:
            self.data = open(os.path.join(self.location, self.docName), 'r').read().split(' ')

    def displayDocument(self) -> None:
        if self.docExists:
            for i in self.data:
                print(i)
            return
            
    def saveDocument(self, newData:str) -> None:
        if self.docExists:
            self.data.append(newData)
        return




class DatabaseManager:
    '''CRUD Ops'''

    def __init__(self) -> None:
        self.homePath = os.getcwd()
        self.database = None
        self.activeDb = {}
    
    def addNewFile(self) -> None:
        pass
    
    def readFromStored(self) -> None:
        # Check for a stored file.
        file = os.path.join(self.homePath, 'dbFile.txt')
        if os.path.exists(file):
            self.database = file
            print(f'DB opened')
        else:
            print(f'No saved databases available to load.')
    
    def writeToDB(self, data:str) -> None:

        if self.database:
            with open(self.database, 'w') as f:
                f.write(data)
        return


x = Document('dbFile.txt')
x.fileContents()
x.displayDocument()