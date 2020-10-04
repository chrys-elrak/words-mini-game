# -*- coding:utf-8 -*-

USAGE = "USAGE: python type input_file filename \nUse 'json' to get json file, 'yaml' to get yaml file"
TXT_JSON = "json"
TXT_YAML = "yaml"


def txt2yaml(f_input, output):
    try:
        from yaml import CLoader as Loader, CDumper as Dumper, dump as ydump
    except ImportError:
        from yaml import Loader, Dumper, dump as ydump
    else:
        print("Please install all requirements")
        exit(1)
    file_name = output if output.endswith('.yaml') or output.endswith('.yml') else output + '.yaml'
    with open(file_name, mode='w') as yml_file:
        yml_file.write(ydump(load_txt(f_input), Dumper=Dumper))


def txt2json(f_input, output):
    import json
    file_name = output if output.endswith('.json') else output + '.json'
    with open(file_name, mode='w') as json_file:
        json_file.write(json.dumps(load_txt(f_input), sort_keys=True, indent=4, ensure_ascii=False))


def load_txt(f_input):
    with open(f_input, encoding='utf-8') as file:
        words_list = file.read().split()
        words_list.sort()
    words = []

    for word in words_list:
        word = (word.strip('\ufeff.():;,“"-«»…!0123456789:*=<>')).lower()
        if word not in words and len(word) > 1:
            words.append(word)
    words.sort()
    return words


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 4:
        p = sys.argv[1]
        input_file = sys.argv[2]
        filename = sys.argv[3]
        if not input_file.endswith('txt'):
            print('Type of input file not recognized')
            exit(1)
        if p == TXT_JSON:
            txt2json(input_file, filename)
        elif p == TXT_YAML:
            txt2yaml(input_file, filename)
    else:
        print(USAGE)
        exit(1)
