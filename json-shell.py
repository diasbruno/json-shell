import json

class DocDontExist(BaseException):
    pass


EXIT = ['exit', 'quit']

def doc_new(poll, args):
    name = args[0]
    poll[name] = json.loads("{}")

def doc_insert(poll, args):
    name = args[0]
    if name not in poll:
        raise DocDontExist("Don't exist.")

def load(poll, args):
    fname = args[0]
    name = fname.split('.')[0]
    with open(fname, 'r') as f:
        poll[name] = json.loads(f.read())

def print_all(poll, args):
    for k, v in poll.items():
        print(k)
        print(v)
        print("-" * 40)

def print_item(poll, args):
    ls = args[0]
    keys = args[1].split('.')
    cpoll = poll[ls]
    for k in keys:
        cpoll = cpoll[k]
    print(cpoll)

PROGRAMS = {'n': doc_new,
            'l': load,
            'i': doc_insert,
            'a': print_all,
            'p': print_item}

def parse_cmd(poll, cmd_args):
    cmd = cmd_args[0]
    args = cmd_args[1:]
    prog = PROGRAMS[cmd]
    prog(poll, args)

def main():
    running = True
    poll = {}

    while running:
        x = input("> ")
        if x in EXIT:
            running = False
        else:
            parse_cmd(poll, x.split(' '))

if __name__ == "__main__":
    main()
