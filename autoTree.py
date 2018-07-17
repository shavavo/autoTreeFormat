import os
from functools import reduce
import argparse

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_directory_structure(rootdir, show_sys_files=False, blacklist=[]):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    Modified by: David Cheng
    Orginal by: Andrew Clark (http://code.activestate.com/recipes/577879-create-a-nested-dictionary-from-oswalk/)
    """
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        if not show_sys_files:
            files = [f for f in files if f[0] != '.' and f not in blacklist]
            dirs[:] = [d for d in dirs if d[0] != '.' and d not in blacklist]

        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)

        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir


def create_tree(current_dict, top_dir, prefix="", sort_alpha=True):
    if current_dict == None:
        return ""

    keys = list(current_dict.keys())

    output = ""

    if sort_alpha:
        keys.sort(key=lambda x: x[0].lower())

    for i, item in enumerate(keys):
        last = True if i == len(keys) - 1 and item != top_dir else False
        connector = '' if item == top_dir else '└── ' if last else '├── '
        nextPrefix = prefix + ('' if item == top_dir else '│   ' if not last else '    ')
        new_row = create_tree(current_dict[item], top_dir, prefix=nextPrefix, sort_alpha=sort_alpha)

        output += prefix + connector + item + '\n' + new_row

    return output


def add_comment(output):
    new_output = ""

    output_split = output.split('\n')[:-1]
    padding = max([len(x) for x in output_split]) + 10

    for x in output_split:
        new_output += x + (padding - len(x)) * " " + "#\n"

    return new_output



def main():
    parser = argparse.ArgumentParser(description='Creates easy to read file structure text file.')
    parser.add_argument('-f', dest="file", type=str, default=["."], nargs=1, help='Root directory. Default: .')

    parser.add_argument('-t', dest="text_file_name", type=str, default=["README_FILE_STRUCTURE.txt"], nargs=1,
                        help='Text file save name. Default: README_FILE_STRUCTURE.txt')

    parser.add_argument('-b', dest="blacklist", type=str, default=[[]], nargs="+",
                        help="Names of files/directories to blacklist. Default: []")

    parser.add_argument('-s', dest="include_system_files", type=str2bool, default=[False], nargs=1,
                        help="Include system files (.) Default: False")

    parser.add_argument('-a', dest="sort_alpha", type=str2bool, default=[True], nargs=1,
                        help="Sort files alphabetically. If set to False, will order in natural progression.")

    parser.add_argument('-c', dest="comment_fields", type=str2bool, default=[True], nargs=1,
                        help="Add comment fields for each file")

    args = parser.parse_args()

    file_dict = get_directory_structure(args.file[0], show_sys_files=args.include_system_files[0], blacklist=args.blacklist)
    output = create_tree(file_dict, list(file_dict.keys())[0], sort_alpha=args.sort_alpha[0])

    if args.comment_fields[0]:
        output = add_comment(output)

    path = args.file[0] + '/' + args.text_file_name[0]
    with open(path, "w") as text_file:
        text_file.write(output)

    print("Saved to " + path)




if __name__ == "__main__":
    main()