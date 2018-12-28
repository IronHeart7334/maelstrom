import subprocess

class Op:
    """
    The static Op object is used to format output
    in a more useful way than just printing strait
    to the screen.
    """
    msgs = []
    indentation_level = 0
    border_pattern = "~*"

    @staticmethod
    def indent(lv=4):
        """
        Increases the indentation level,
        defaults to 4
        """
        Op.indentation_level += lv

    @staticmethod
    def set_indentation(lv):
        Op.indentation_level = lv

    @staticmethod
    def add(msgs):
        if type(msgs) == type("I'm a string!"):
            #is it a string?
            Op.msgs.append(" " * Op.indentation_level + msgs)
        else:
            try:
                #is it iterable?
                for msg in iter(msgs):
                    #recursive
                    Op.add(str(msg))
            except:
                #nope, not iterable, so recursive
                Op.msgs.add(str(msgs))

    @staticmethod
    def reset():
        Op.msgs = []
        Op.indentation_level = 0

    @staticmethod
    def display():
        try:
            pass
            #works = subprocess.call("cls", shell=True)
        except:
            print("cls no work in output.py display method!")
        print(Op.border_pattern * 10)
        for msg in Op.msgs:
            print(msg)
        print(Op.border_pattern * 10)
        Op.reset()