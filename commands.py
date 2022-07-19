from errors import *

variables = {}
args = {}
functions = {}

def run_function(instruction):
    try:
        func = commands[instruction['type']]
    except KeyError:
        raise CommandNotFoundException(
            f"[Error] Cannot find \"{instruction['type']}\" in any libary or function file")

    params = get_params(instruction['params']) if not instruction['type'] in ['while', 'do_while'] else instruction['params']

    return func(*params)


def run_code(instructions, program_functions=None):
    global functions

    functions = program_functions

    for instruction in instructions:
        run_function(instruction)


def get_params(_params):

    params = []

    for param in _params:
        if type(param) is dict:
            params.append(run_function(param))
        else:
            params.append(param)

    return params

def clean_scope():
    for variable in variables:
        if variables[variable]['scope'] == 'local':
            variables.pop(variable)


def add(a, b):
    return a + b


def subtract(a, b):
    return a-b


def divide(a, b):
    return a/b


def multiply(a, b):
    return a*b


def mod(a, b):
    return a % b


def exponent(a, b):
    return a ** b


def _if(cond, do, _else=None):
    if cond:
        run_code(do)
    else:
        if _else is not None:
            run_code(_else)


def evaluate(cond1, op, cond2):
    match op:
        case "==":
            return cond1 == cond2
        case "!=":
            return cond1 != cond2
        case ">=":
            return cond1 >= cond2

        case "<=":
            return cond1 <= cond2

        case ">":
            return cond1 > cond2

        case "<":
            return cond1 < cond2

        case _:
            raise InvalidOperatorException(
                f"{op} is not a valid comparison operator")


def set_var(scope, name, value):
    if name in variables:
        if variables[name]['scope'] == 'const':
            raise ConstantError(f'Variable {name} is constant and cannot be changed')
        variables[name]['value'] = value
    else:
        variables[name] = {'scope': scope, 'value': value}


def get_var(name):
    try:
        return variables[name]['value']
    except KeyError:
        raise DataError(f'Variable {name} does not exist')


def _repeat(_i, do):
    for i in range(_i):
        run_code(do)

    clean_scope()


def _while(cond, do):
    while True:

        if not run_function(cond):
            break

        run_code(do)

    clean_scope()


def do_while(do, cond):
    run_code(do)

    while True:

        if not run_function(cond):
            break

        run_code(do)

    clean_scope()


def _and(cond1, cond2):
    return cond1 and cond2


def _or(cond1, cond2):
    return cond1 or cond2


def _not(cond1):
    return not cond1

def _bool(value):
    if value.lower() in ['true', 'false']:
        if value.lower() == 'true':
            return True
        else:
            return False

    return bool(value)

def call_function(name, params):
    # Generate arguments

    global args

    for i in range(len(params)):
        args[functions[name]['params'][i]] = params[i]

    run_code(functions[name]['instructions'])

    args = {}
    clean_scope()

def get_arg(name):
    return args[name]


commands = {
    "print": print,
    "add": add,
    "subtract": subtract,
    "divide": divide,
    "multiply": multiply,
    "mod": mod,
    "exponent": exponent,
    "if": _if,
    "int": int,
    "str": str,
    "bool": _bool,
    "list": list,
    "evaluate": evaluate,
    "set_var": set_var,
    "get_var": get_var,
    "repeat": _repeat,
    "while": _while,
    "do_while": do_while,
    "input": input,
    "or": _or,
    "and": _and,
    "not": _not,
    "call_function": call_function,
    "get_arg": get_arg,
}