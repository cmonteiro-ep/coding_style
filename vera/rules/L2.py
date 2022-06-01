import vera

from utils import is_header_file, is_source_file, is_line_correctly_indented, get_lines


def check_line_indentation():
    for file in vera.getSourceFileNames():
        if not is_source_file(file) and not is_header_file(file):
            continue
        for line_number, line in enumerate(get_lines(file), start=1):
            if not is_line_correctly_indented(line):
                vera.report(file, line_number, 'MINOR:L2')


check_line_indentation()
