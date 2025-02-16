"""
This is the code for problem 5, quiz 3 for bioinf6200, in which we must use the **kwargs method and define the function command_line, takes 1 known parameter, 'name', and an unknown number of kwargs. Includes invocation example.
"""

def command_line(name, **kwargs):
    """
    def function to be run in command line which takes 1 positional parameter, 'name', and undetermined number of keyword arguments.
    """
    print(f'I read a book called {name} today and this is what I learned:')
    # print intro statement using 'name' parameter. Format string to contain specified positional parameter
    details = ['protagonist', 'antagonist', 'timeframe', 'location', 'theme', 'outcome', 'moral']
    #create list of keys to introduce keyword arguments. These are the keys and the input parameters are the values for the list,
    for detail in details:
        # use for loop to iterate over each key in list
        value = kwargs.get(detail, 'Not specified')
        # pair each key with corresponding value. If key value doesn't exist, default to ('not specified')

        print(f'{detail} = {value}')
        # print each detail (key) and corresponding value (kwargs) in format key = value


# Invocation example
command_line("Beauty & the Beast", protagonist='Belle', antagonist='Gaston', timeframe='18th century, during Rococo period', location='the Aquitaine region of France', theme='the transformative power of love and acceptance', outcome='The spell is broken when Belle falls in love with the Beast before the last petal from the enchanted rose has fallen', moral='value inward characteristics like kindness over superficial ones like appearance')