import sys
from init import init
from add import add
def main():
    try: 
        cmd = sys.argv[1]

        if cmd == "init":
            init(sys.argv[2])
        if cmd == "add":
            add(sys.argv[2])

    except IndexError:
        print("Invalid of args")
        return
   