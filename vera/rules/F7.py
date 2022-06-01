import vera
from utils import is_source_file, is_header_file
from utils.functions import get_functions


def check_nested_functions():
    for file in vera.getSourceFileNames():
        if not is_source_file(file) and not is_header_file(file):
            continue

        functions = get_functions(file)
        for id_a, function_a in enumerate(functions):
            if function_a.body is None:
                continue
            for id_b, function_b in enumerate(functions):
                if function_b.prototype is None:
                    continue
                if id_a == id_b:
                    continue
                if function_a.body.line_start <= function_b.prototype.line_start and function_a.body.line_end >= function_b.prototype.line_end:
                    vera.report(file, function_b.prototype.line_start, "MAJOR:F7")


check_nested_functions()
