#creating complete list of all possible mastermind combinations with 6 colors
def CompleteList():
    compList = []
    for i in range(6):
        for ii in range(6):
            for iii in range(6):
                for iv in range(6):
                    compList.append((i,ii,iii,iv))
    return compList

class JoeSolve:
    def __init__(self, window, master):
        self.knownColors = []
        self.solved = False
        self.gotColors = False
        self.master = master
        self.window = window
        #grabbing a copy of the complete list so we don't have to recalculate it
        self.remaining = list(window.completeCopy)
        self.remainingQueue = []
        self.joeGuess = []
    def solve(self):
        for i in range(6):
            self.joeGuess = [i, i, i, i]
            self.window.guess = list(self.joeGuess)
            self.window.Cluenumbers = self.window.CompareInput(self.joeGuess, list(self.master)) # <-- THIS needs to be adjusted
            self.lastClue = self.window.Cluenumbers
            self.window.AddRow()
            for j in range(self.window.Cluenumbers[0]+self.window.Cluenumbers[1]):
                self.knownColors.append(i)
            if len(self.knownColors) == 4:
                self.gotColors = True
                break
            continue

        self.window.guess = list(self.knownColors)
        self.window.Cluenumbers = self.window.CompareInput(list(self.window.guess), list(self.master))
        self.lastClue = tuple(self.window.Cluenumbers)
        self.window.AddRow()
        self.lastGuess = list(self.knownColors)
        
        for i in range(len(self.remaining)):
            if tuple(self.lastClue) == tuple(self.window.CompareInput(list(self.lastGuess), list(self.remaining[i]))):
                self.remainingQueue.append(self.remaining[i])
        self.remaining = list(self.remainingQueue)

        while self.window.solved == False:
            self.remainingQueue = []
            self.window.guess = list(self.remaining[0])
            self.lastGuess = list(self.remaining[0])
            self.window.Cluenumbers = self.window.CompareInput(list(self.window.guess), list(self.master))
            self.lastClue = tuple(self.window.Cluenumbers)
            self.window.AddRow()
            for i in range(len(self.remaining)):
                if tuple(self.lastClue) == tuple(self.window.CompareInput(list(self.lastGuess), list(self.remaining[i]))):
                    self.remainingQueue.append(self.remaining[i])
            self.remaining = list(self.remainingQueue)


class LeylaSolve:
    def __init__(self, window, master):
        self.knownColors = []
        self.solved = False
        self.master = master
        self.window = window
        self.remaining = list(window.completeCopy)
        self.remainingQueue = []
        self.leylaGuess = []
    def solve(self):
        
        self.window.guess = list(self.remaining[0])
        self.window.Cluenumbers = self.window.CompareInput(list(self.window.guess), list(self.master))
        self.lastClue = tuple(self.window.Cluenumbers)
        self.window.AddRow()
        self.lastGuess = list(self.remaining[0])

        for i in range(len(self.remaining)):
            if tuple(self.lastClue) == tuple(self.window.CompareInput(list(self.lastGuess), list(self.remaining[i]))):
                self.remainingQueue.append(self.remaining[i])
        self.remaining = list(self.remainingQueue)
        while self.window.solved == False:
            self.remainingQueue = []
            self.window.guess = list(self.remaining[0])
            self.lastGuess = list(self.remaining[0])
            self.window.Cluenumbers = self.window.CompareInput(list(self.window.guess), list(self.master))
            self.lastClue = tuple(self.window.Cluenumbers)
            self.window.AddRow()
            for i in range(len(self.remaining)):
                if tuple(self.lastClue) == tuple(self.window.CompareInput(list(self.lastGuess), list(self.remaining[i]))):
                    self.remainingQueue.append(self.remaining[i])
            self.remaining = list(self.remainingQueue)

class DarylSolve:
    def __init__(self, window, master):
        self.knownColors = []
        self.solved = False
        self.master = master
        self.window = window
        self.remaining = list(window.completeCopy)
        self.remainingQueue = []
    def solve(self):
        
        self.window.guess = [0,1,2,3]
        self.window.Cluenumbers = self.window.CompareInput(list(self.window.guess), list(self.master))
        self.lastClue = tuple(self.window.Cluenumbers)
        self.window.AddRow()
        self.lastGuess = [0,1,2,3]

        for i in range(len(self.remaining)):
            if tuple(self.lastClue) == tuple(self.window.CompareInput(list(self.lastGuess), list(self.remaining[i]))):
                self.remainingQueue.append(self.remaining[i])
        self.remaining = list(self.remainingQueue)
        while self.window.solved == False:
            self.remainingQueue = []
            self.window.guess = list(self.remaining[0])
            self.lastGuess = list(self.remaining[0])
            self.window.Cluenumbers = self.window.CompareInput(list(self.window.guess), list(self.master))
            self.lastClue = tuple(self.window.Cluenumbers)
            self.window.AddRow()
            for i in range(len(self.remaining)):
                if tuple(self.lastClue) == tuple(self.window.CompareInput(list(self.lastGuess), list(self.remaining[i]))):
                    self.remainingQueue.append(self.remaining[i])
            self.remaining = list(self.remainingQueue)