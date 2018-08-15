import sys

class Bracket:
    def __init__(self,aa,bb):
        self.bracket_type = aa
        self.bracket_position = bb

    def Check_match(self,cc):
        if self.bracket_type == "[" and cc == "]":
            return True
        if self.bracket_type == "(" and cc ==")":
            return True
        if self.bracket_type == "{" and cc == "}":
            return True
        return False


if __name__ == "__main__":
    in_put = sys.stdin.read()

    #you cannot fill the list directly, you should fill it one by one.
    #Wrong code: Bracket_list = [Bracket(type, position) for position, type in enumerate(in_put, start = 1) ]
    Bracket_list = []
    for position, type in enumerate(in_put, start=1):
        if type == "[" or type == "(" or type == "{":
            Bracket_list.append(Bracket(type, position))
        if type == "]" or type == ")" or type == "}": #here you can just say else:, since the in_put can also contain some strings
            if not Bracket_list:
                print(position)
            last_bracket = Bracket_list.pop()
            if not last_bracket.Check_match(type):
                print(position)
    if Bracket_list:
        print(Bracket_list.pop().position)
    else:print("Success")

