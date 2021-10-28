import os
import subprocess
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-directory", 
                        help="the input directory filepath")

    args = vars(parser.parse_args())
    return args["input_directory"]


def get_paths(directory):
    contents = os.listdir(directory)
    directories = [os.path.join(directory, content) for content in contents]
    return directories



def main():
    directory = get_args()
    filepaths = get_paths(directory)
    print(filepaths)

if __name__=="__main__":
    main()