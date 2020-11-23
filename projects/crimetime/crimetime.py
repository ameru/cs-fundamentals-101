month = ["January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"]

day_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
        "Saturday"]

hour = ["12AM", "1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", "9AM",
        "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM",
        "7PM", "8PM", "9PM", "10PM", "11PM"]

class Crime:
    """Crime
    Attributes:
    crime_id (int): as read from crimes.tsv
    category (string): as read from crimes.tsv
    month (string): modified from times.tsv to be a full word
    day_of_week (string): as read from times.tsv
    hour (int): modified from times.tsv to be in AM/PM format
    """

    def __init__(self, crime_id, category):
        """ Initializes crime object with crime_id
        Arguments:
            crime_id (int): ID of crime
            category (string): type of crime
        Returns:
            crime: crime object with crime_id and category output
        """
        self.month = "Month"
        self.day_of_week = "Day"
        self.hour = "Hour"
        self.crime_id = crime_id
        self.category = category

    def __eq__(self, other) -> bool:
        """ Checks that all crime_ids are consistent
        Arguments:
            other (crime): comparison object for crime_id
        Returns:
            boolean: True if equal, False if not equal
        """
        return self.crime_id == other.crime_id

    def __repr__(self):
        """ Adjust syntax of crime object
        Arguments:
            N/A
        Returns:
            crime: returns correctly formatted crime object
        """
        return "(%s)\t(%s)\t(%s)\t(%s)\t(%s)\n" % (self.crime_id, \
            self.category, self.month, self.day_of_week, self.hour)

def create_crimes(lines) -> list:
    """ Creates one crime object for each unique ID
    Arguments:
        lines (list): list of strings read from crimes.tsv
    Returns:
        list: list of crime obejcts, one for each unique robbery found
    """
    crimes = []
    counter = 0
    
    for line in lines:
        found = 0
        string = line.split("\t")
        try:
            if string[1] == "ROBBERY":
                for counter in range(len(crimes)):
                    if crimes[counter].crime_id == string[0]:
                        found = 1
                if found != 1:
                    crimes.append(lines(string[0].string[1]))
                    # might have to replace 'lines' with Crime
        except:
            pass
    return crimes

def sort_crimes(crimes) -> list:
    """ Import copy module and use the copy() function to shallow copy list of
    crimes into a new, sorted list.
    Arguments:
        crimes (list): list of crime objects
    Returns:
        list: list of crime objects sorted by ID number (use selection or
        insertion sort)
    """
    length = len(crimes)
    for crime in range(length):
        minimum = crime
        for ids in range(crime + 1, length):
            if int(crimes[minimum].crime_id) > int(crimes[ids].crime_id):
                minimum = ids
        temp = crimes[crime].crime_id
        crimes[crime].crime_id = crime[minimum].crime_id
        crimes[minimum].crime_id = temp
    return crimes

def set_crimetime(crime, day_of_week, month, hour):
    """ Update crime attributes using lists, range, or enumerate
    Arguments:
        day_of_week (string): day_of_week of crime
        month (int): month of crime
        hour (int): hour of crime
    Returns:
        list: return updated crime object with month and hour integer arguments
        into their string representations
    """
    crime.month = month[month - 1]
    crime.day_of_week = day_of_week
    crime.hour = hour[hour - 1]

def update_crimes(crimes, lines):
    """ Calls find_crime to locate crime objects and set_crimetime to update 
    attributes of crime object
    Arguments:
        crimes (list): list of crimes
        lines (list): list of strings
    Returns:
        list: updated crimes
    """
    length = len(lines)
    for line in range(length):
        string = lines[line].split("\t")
        location = find_crime(crimes, string[1])
        try:
            location.month = int(string[1][:2])
            location.day_of_week = int(string[2])
            location.hour = int(string[3][:2])
            location.set_time(location.day_of_week, location.month, \
                location.hour)
        except:
            pass
    return crimes

def find_crime(crimes, crime_id):
    """ Uses binary search to find and return crime object
    Arguments:
        crime (list): amount of fuel left on the LM
        crime_id (int): single crime ID integer
    Returns:
        crime: return crime object with crime ID
    """
# Binary Search Example from class
    # lo, hi = 0, len(list) - 1
    # while lo <= hi:
    #     mid = (lo + hi) // 2 # the mid point
    #     if list[mid] == num: # num is found
    #         return mid # return the index
    #     elif num < list[mid] # num is smaller
    #         hi = mid - 1 # go left
    #     else:
    #         lo = mid + 1 # go right
    # return -1 # not found

    counter = 0
    finished = len(crimes) - 1
    while counter != finished:
        mid = (counter + finished) // 2
        if int(crimes[mid].crime_id) == int(crime_id):
            return crimes[mid]
        elif int(crime_id) < int(crimes[mid].crime_id):
            finished = mid
        elif int(crime_id) > int(crimes[mid].crime_id):
            counter = mid + 1
    if int(crimes[finished].crime_id) == int(crime_id):
        return crimes[finished]
    return None

# first implement the simpler but slower linear search to get the program
# working, and later return to replace it with binary search

### HELPER FUNCTIONS
def print_update(crime_list, files):
    """Prints updated class "Crime" to files    
    Args: 
        crime_list (list): list of crime objects
        files (string): files user writes in
    Returns:
        None
    """
    length = len(crime_list)
    for counter in range(length):
        files.write(crime_list[counter].crime_id + "\t" + \
            crime_list[counter].category + "\t" + \
            crime_list[counter].day_of_week + "\t" + \
            crime_list[counter].month + "\t" + \
            crime_list[counter].hour + "\n")
    return

def num_of_times(list):
    """Find most frequent crime in list    
    Args: 
        list (list): list of values      
    Returns:         
        (string): Variable that most commonly occurs in list
    """
    most_frequent = 0
    index = 0
    for counter in range(len(list)):
        count = list.count(list[counter])
        if count > most_frequent:
            most_frequent = count
            index = counter
    return list[index]

def max_month(crime_list):
    """Finds most frequent month of year for crimes
    Args: 
        updated (list): list of "Crime" objects
    Returns:         
        month (string): Most commonly occuring month in "updated"
    """
    list_2 = list()
    length = len(crime_list)
    for counter in range(length):
        list_2.append(crime_list[counter].month)
    return num_of_times(list_2)

def max_day(crime_list):
    """Find most frequent day of week for crimes 
    Args: 
        crime_list (list): list of "Crime" objects
    Returns:         
        day_of_week (string): Most commonly occuring day in "updated"
    """
    list_1 = list()
    length = len(crime_list)
    for counter in range(length):
        list_1.append(crime_list[counter].day_of_week)
    return num_of_times(list_1)

def max_hour(crime_list):
    """Finds most commonly occuring hour    
    Args:
        updated (list): list of "Crime" objects
    Returns:         
        hour (string): Most commonly occuring hour in "updated"
    """
    list_3 = list()
    length = len(crime_list)
    for counter in range(length):
        list_3.append(crime_list[counter].hour)
    return num_of_times(list_3)

def read_crime(files):
    """Opens file for reading     
    Args:
        files (string): file to be read by user
    Returns:
        file (string): returns file variable
    """
    file = open(files, 'r')
    file.readline()
    return file

def write_crime(files):
    """Opens file for writing  
    Args:
        files (string): file to be written in by user
    Returns:
        File (string): returns file variable
    """
    file = open(files, 'w')
    file.write("ID\tCategory\tDayOfWeek\tMonth\tHour\n")
    return file

def record_crime(files):
    """Append file to a list     
    Args:
        files (string): file to be recorded by user
    Returns:
        file_list (list): list of files
    """
    file_list = list()
    file_list = files.readlines()
    return file_list

def main():
    """Run main program     
    Args: 
        N/A
    Returns:         
        N/A
    """
    crime = read_crime("crimes.tsv")
    time = read_crime("times.tsv")
    robberies = write_crime("robberies.tsv")
    lines = record_crime(crime)
    crimes = create_crimes(lines)
    crimes = sort_crimes(crimes)
    lines = record_crime(time)
    crime_list = update_crimes(crimes, lines)
    print_update(crime_list, robberies)

### Output:
# system should write out a robberies.tsv file
# program will print following crime stats:
# NUMBER OF PROCESSED ROBBERIES:
# DAY WITH MOST ROBBERIES:
# MONTH WITH MOST ROBBERIES:
# HOUR WITH MOST ROBBERIES:

    print("NUMBER OF PROCESSED ROBBERIES: %d" % (len(crime_list)-1))
    print("DAY WITH MOST ROBBERIES: %s" % max_day(crime_list))
    print("MONTH WITH MOST ROBBERIES: %s" % max_month(crime_list))
    print("HOUR WITH MOST ROBBERIES: %s" % max_hour(crime_list))

if __name__ == "__main__":
    main()
    
