from pysniper import snoop, CodeEvent
from termcolor import colored

def callback(code_event: CodeEvent, locals: dict, *args, **kwargs):
    match code_event:
        case CodeEvent.NewSourcePath:
            print(colored(f"{code_event}, {kwargs['source_path']}", 'blue'))
        case CodeEvent.NewVar:
            print(colored(f"{code_event}, {kwargs['var_name']} = {kwargs['var_value']}", 'yellow'))
        case CodeEvent.ModVar:
            print(colored(f"{code_event}, {kwargs['var_name']} = {kwargs['var_value']}", 'green'))
        case CodeEvent.NextSourceLine:
            print(colored(f"{code_event}, {kwargs['source_line']}", 'cyan'))
        
@snoop('test.log', callback=callback)
def test_func(count):
    x = []
    while count < 10:
        count += 1
        x.append(count)
    y = x.pop()
    return y
if __name__ == "__main__":
    result = test_func(0)
