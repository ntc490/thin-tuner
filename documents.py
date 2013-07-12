TABLE_TYPE_FUEL = 0
TABLE_TYPE_INGITION = 1
TABLE_TYPE_LAST = 2

BIN_TYPE_P30 = 0
BIN_TYPE_P72 = 1
BIN_TYPE_LAST = 2

class bin:
    def __init__(self):
        self.tableNum = 0
        self.maxTableNum = 0
        self.table = []
        # Cell max value?  not always 255.

    def incCell(self, x, y, val):
        if not self.table[x][y] < 255:
            return
        self.table[x][y] = self.table[x][y] + val

    def decCell(self, x, y, val):
        if not self.table[x][y] > 0:
            return
        self.table[x][y] = self.table[x][y] - val

    def setCell(self, x, y, val):
        pass

    def getCell(self, x, y):
        pass

    def selectTable(self, num):
        if num < 0 or num > self.maxTableNum:
            # Signal an exception here?
            return
        self.tableNum = num

    def getTableInfo(self):
        "Get a list containing table number, name, and type.  Type may be"
        pass

    def getType(self):
        """Get the type of binfile this is - a string and number.  Override this in
        sub-classes
        """
        pass


class P30Bin(bin):
    def __init__(self):
        bin.__init__(self)
        self.maxTableNum = 3

    def getType(self):
        return ("P30", BIN_TYPE_P30)

    def getTableInfo(self):
        info = (
            ( 0, "Fuel1", TABLE_TYPE_FUEL ),
            ( 1, "Fuel2", TABLE_TYPE_FUEL ),
            ( 2, "Ign1", TABLE_TYPE_IGNITION ),
            ( 3, "Ign2", TABLE_TYPE_IGNITION ) )
        return info

    
class log:
    pass


class views:
    pass


class package:
    """This class defines a FreeMapper document - a collection of many files in zip
    format that can be separated out into individual components.  This allows us to
    keep revision history of the map files, keep logs and all other related tuning
    data in one spot.
    """
    pass


class notes:
    """The class contains notes for different 'events' during the tuning process.
    Notes are kept along with the bin, logs, and other data during tuning.
    """
    pass
