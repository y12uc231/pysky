import re


def refine(str):
    '''

    :param str: Any tag expression
    :return: Refined string where multiple spaces are removed
    '''
    str = re.sub(' +', ' ', str)
    str = re.sub(' += +', '=', str)
    str = re.sub(' +>', '>', str)
    str = re.sub(' +<', '<', str)
    str = re.sub('< +', '<', str)
    str = re.sub(r'<\\ +', r'<\\', str)
    return str


def pyparser(string, query):
    '''
    :param string: Source code of tags only
    :param query:  Queries in the form of Tag1.Tag2.Tag3~attr
    :return: A list of answer to the queries and -1 for invalid query
    This function works as a hash function for attribute values of valid tags
    '''
    # corner cases
    if len(string) == 0:
        return;
    #
    # Phase1: Storing
    map = dict()
    stack = ''
    pattern1 = re.compile(r'^<\w+')
    pattern2 = re.compile(r'\w+(?==)')
    pattern3 = re.compile(r'"([^"]*)"')
    for i in string:
        s = i
        s = refine(s)
        # print(str)
        re.M  # Multiline
        if s.find('/') == -1:
            result = pattern1.findall(s)
            result1 = pattern2.findall(s)
            result2 = pattern3.findall(s)
            if len(stack) == 0:
                stack = stack + result[0][1:len(result[0])]
            else:
                stack = stack + '.' + result[0][1:len(result[0])]

            # print(stack)
            map[stack] = dict()

            for j in range(len(result1)):
                #if result2[j] ==
                map[stack][result1[j]] = result2[j]
                print(map[stack][result1[j]])

        else:
            if stack.find('.') != -1:
                stack = stack[0:stack.rfind('.')]
            else:
                stack = ''
    # Phase 2
    result = []
    for i in query:
        if i.find('~') == -1:
            result.append(-1)
        else:
            s = i[0:i.find('~')]
            if s in map.keys():
                s2 = i[i.find('~') + 1:len(i)]
                if s2 in map[s].keys():
                    result.append(map[s][s2])
                else:
                    result.append(-1)
            else:
                result.append(-1)
    return result