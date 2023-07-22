from termcolor import colored
def print_green(txt, end='\n'):
    print(colored(txt,'green',attrs=['reverse']), end=end)
def print_yellow(txt, end='\n'):
    print(colored(txt,'yellow', attrs=['reverse']),end=end)
def print_red(txt, end='\n'):
    print(colored(txt,'red',attrs=['reverse']), end=end)
