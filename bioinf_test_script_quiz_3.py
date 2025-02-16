# Test codes for Quiz 3


def output(x):
    x = ('A', 'B', 'C')
    concatenated_list = ''.join(x)
    repeated_list = concatenated_list * 3
    return repeated_list

#Test the function and print result
if __name__ == "__main__":
    input_list = ['A', 'B', 'C']
    result = output(input_list)
    print(result)
