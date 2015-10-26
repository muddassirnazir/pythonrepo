'''
An assertion is a condition that we’re claiming should be true at this point in the program. Typically, it summarizes the state of the program’s
variables. Assertions can help explain the relationships among variables, review what has happened so far in the program, and show that if statements
and for or while loops have the desired effect. When a program is correct, all of the assertions are true no matter what inputs are provided. When a
program has an error, at least one assertion winds up false for some combination of inputs. Python directly supports assertions through an assert
statement. There are two forms: assert condition assert condition , expression If the condition is False, the program is in error;
this statement raises an AssertionError exception. If the condition is True, the program is correct, this statement does nothing more.
'''
