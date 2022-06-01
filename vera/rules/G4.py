import vera

from utils import is_source_file, is_header_file


def acceptPairs(file, tokens, index=0, level=0, state="other"):
    end = len(tokens)
    while index != end:
        token = tokens[index]

        if token.type == "leftbrace":
            index += 1
            level += 1
            acceptPairs(file, tokens, index, level, state)
            if index == end:
                return

            index += 1
        elif token.type == "assign":
            index += 1
            if level == 0 and state != "const":
                state = "assign"
            elif level == 0:
                state = "constassign"

        elif token.type == "rightbrace":
            level -= 1
            if level == 0:
                state = "other"
            return
        elif token.type == "semicolon":
            index += 1
            if level == 0 and state == "assign":
                vera.report(file, token.line, "MINOR:G4")
            state = "other"
        elif token.type == "const":
            index += 1
            if level == 0 and state == "other":
                state = "const"

def check_global_variable_constness():
    for file in vera.getSourceFileNames():
        if not (is_source_file(file) or is_header_file(file)):
            continue
        tokens = vera.getTokens(
            file, 1, 0, -1, -1, ["const", "semicolon", "assign", "leftbrace", "rightbrace"])
        acceptPairs(file, tokens)

check_global_variable_constness()
