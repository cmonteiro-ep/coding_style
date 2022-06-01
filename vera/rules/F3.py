import vera

from utils import is_header_file, is_source_file, is_makefile
from utils import get_lines

TAB_MAX_LENGTH = 4
LINE_MAX_LENGTH = 80


def check_line_length():
    for file in vera.getSourceFileNames():
        if not is_source_file(file) and not is_header_file(file) and not is_makefile(file):
            continue

        for line_number, line in enumerate(get_lines(file), start=1):
            count = 0
            for character in line:
                if character == '\t':
                    count = (count + TAB_MAX_LENGTH) - (count % TAB_MAX_LENGTH)
                else:
                    count += 1
            if count > LINE_MAX_LENGTH:
                vera.report(file, line_number, "MAJOR:F3")


check_line_length()
