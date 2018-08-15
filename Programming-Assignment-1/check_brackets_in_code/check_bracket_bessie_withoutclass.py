import sys

def match(aa, bb):
    if aa == "(" and bb ==")":
        return True
    if aa == "[" and bb =="]":
        return True
    if aa == "{" and bb =="}":
        return True
    return False

def check_without_class(in_put):
    bracket_stack = []
    for position, type in enumerate(in_put, start=1):
        if type == "(" or type == "[" or type == "{":
            bracket_stack.append([position, type])
        if type == ")" or type == "]" or type == "}":
            if not bracket_stack:
                return position
            last_element = bracket_stack.pop()
            if not match(last_element[1], type):
                return position
    if bracket_stack:
        return bracket_stack.pop()[0]
    return "Success"

if __name__ == "__main__":
    text = sys.stdin.read()
    print(check_without_class(text))