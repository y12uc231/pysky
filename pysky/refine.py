import re
def refine_string(str):
    str = re.sub(' +', ' ', str)
    str = re.sub(' += +', '=', str)
    str = re.sub(' +>', '>', str)
    str = re.sub(' +<', '<', str)
    str = re.sub('< +', '<', str)
    str = re.sub(r'<\\ +', r'<\\', str)
    return str