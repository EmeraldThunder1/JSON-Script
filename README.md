# JSON-Script

JSON-Script is an experimental programming language that allows you to write code in the JSON object description language. Currently it is limited in features although this will expand in the future.

## Installation

Navigate to releases, download the correct version for your OS and then run it.

## Basic usage

In a blank json object create a list called instructions which will store each 'line' of code.

```json
{
    "instructions": [

    ]
}
```

Each line of code is an object in this list. JSON-Lang represents everything including loops and maths as a function. Each function object needs two properties, a name and a list of parameters.

For example:

```json
{
    "instructions": [
        {
            "type": "print",
            "params": [
                "Hello World!"
            ]
        }
    ]
}
```

A full list of functions can be found below.

## Creating variables

JSON-Script is a weakly typed language and as such variables can assume any data type. The set_variable function is used to create or update a variable and the get_variable function is used to get the value of a variable.

```json
{
    "instructions": [
        {
            "type": "set_variable",
            "params": [
                "myVariable",
                "Hello World!"
            ]
        }
    ]
}
```

The first parameter is the name of the variable. The second is the value you would like to set it to.

In JSON-Script placing a function call within the parameters list of another function will allow for that function to insert it's returned value into the place of the parameter.

For example, if we want to print the value of our variable:

```json
{
    "instructions": [
        {
            "type": "print",
            "params": [
                {
                    "type": "get_variable",
                    "params": [
                        "myVariable"
                    ]
                }
            ]
        }
    ]
}
```

## Loops and conditionals

Currently there are three loops, a repeat loop, a while loop and a do while loop.

The repeat loop accepts a number and runs a code-block that amount of times. A code-block is a list of functions

```json
{
    "instructions": [
        {
            "type": "repeat",
            "params": [
                10,
                [
                    {
                        "type": "print",
                        "params": [
                            "Hello World!"
                        ]
                    }
                ]
            ]
        }
    ]
}
```

The while loop accepts a boolean and a code-block to run while that boolean is met. For more information on value comparison, see below.

```json
{
    "instructions": [
        {
            "type": "while",
            "params": [
                true,
                [
                    {
                        "type": "print",
                        "params": [
                            "Hello World!"
                        ]
                    }
                ]
            ]
        }
    ]
}
```

The do while loop accepts a code-block and a boolean. It will execute the code-block once no-matter what and will then run it until the condition is met.

```json
{
    "instructions": [
        {
            "type": "do_while",
            "params": [
                [
                    {
                        "type": "print",
                        "params": [
                            "Hello World!"
                        ]
                    }
                ],
                true
            ]
        }
    ]
}
```

It is also possible to run code if a boolean value is true using the if statement. This takes in a boolean and a minimum of one code-block. A second block can be provided to be executed if the condition is not met.

```json
{
    "instructions": [
        {
            "type": "if",
            "params": [
                true,
                [
                    {
                        "type": "print",
                        "params": [
                            "The condition was true"
                        ]
                    }
                ],
                [
                    {
                        "type": "print",
                        "params": [
                            "The condition was false"
                        ]
                    }
                ],
            ]
        }
    ]
}
```

## Comparing values.

The evaluate function can be used to compare values usign one of several operators.
It takes in one value, an operator and then another value.

### Operators:
* == : Will return true if the values are the same
* != : Will return true if the values are not the same
* \>= : Will return true if value one is the same as or greater than value two
* <= : Will return true if value one is the same as or less than value two
* \> : Will return true if value one is greater than value two
* < : Will return true if value one is less than value two

For example

```json
{
    "instructions": [
        {
            "type": "if",
            "params": [
                {
                    "type": "evaluate",
                    "params": [
                        true,
                        "==",
                        false
                    ]
                },
                [
                    {
                        "type": "print",
                        "params": [
                            "The condition was true"
                        ]
                    }
                ]
            ]
        }
    ]
}
```

The functions not, and, and or can be used to combine or invert values (boolean logic)

## List of functions

This is a complete list of all the functions in JSON-Script at the moment. This list will change in the future.

* print: Prints text to the console [1 perameter: text]
* add: Adds two values together [2 perameters: value1, value2]
* subtracts: Subtracts two values [2 perameters: value1, value2]
* multiply: Multiplies two values together [2 perameters: value1, value2]
* divide: Divides two values [2 perameters: value1, value2]
* mod : Finds the modulo of two numbers (divides them together and find the remainer) [2 perameters: value1, value2]
* exponent: Raises one value to the power of another [2 perameters: value1, value2]
* if: Runs a block if a boolean is met and runs another if not [3 parameters: boolean, do, else*]
* int: Converts a value to an integer [1 parameter: value]
* str: Converts a value to a string [1 parameter: value]
* bool: Converts a value to a boolean [1 parameter: value]
* list: Condenses values into a list [Unlimited parameters: items]
* evaluate: Evaluates a boolean condition [3 parameters: value1, operator, values2]
* set_var: Sets a variable to a value [2 parameters: name, value]
* get_var: Gets the value of a variable [1 parameter: name]
* repeat: Repeats a code-block {x} times [2 parameters: times, code]
* while: Runs a block while a condition is met [2 parameters: condtion, code]
* do_while: Runs a block one and then while a condition is met [2 parameters: code, condition]
* input: Gets input from a user
* or: Returns true is either condition is true [2 parameters: cond1, cond2]
* and: Returns true if both conditions are true [2 parameters: cond1, cond2]
* not: Inverts a boolean [1 parameter: cond1]

\* Optional parameter