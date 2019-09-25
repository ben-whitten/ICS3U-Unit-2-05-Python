#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: September 2019
# This is a program shows how local and global variables work.

# This is the global variable
variable_X = 20


def local_variable():

    # This is a local variable.
    variable_X = 10
    variable_Y = 12
    variable_Z = variable_X - variable_Y
    print("local variable X, variable Y, variable Z: {0} {1} {2}"
          .format(variable_X, variable_Y, variable_Z))


def global_variable():

    # This is a global variable.
    global variable_X
    variable_X = variable_X - 2
    variable_Y = 12
    variable_Z = variable_X - variable_Y
    print("local variable X, variable Y, variable Z: {0} {1} {2}"
          .format(variable_X, variable_Y, variable_Z))


def main():
    # This is what shows how they work.

    local_variable()
    global_variable()


if __name__ == "__main__":
    main()
