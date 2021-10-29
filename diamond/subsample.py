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
    # SRA gives in format of Project/Sample/Sample_1.fastq and Project/Sample/Sample_2.fastq
    # for forward and reverse reads, respectively
    all_fastqs = [(os.path.join(directory, content, f"{content}_1.fastq"),
                    os.path.join(directory, content, f"{content}_2.fastq")) for content in contents]
    return all_fastqs


def merge_reads(filepaths):
    for filepath in filepaths:
        output_filepath = filepath[0].split("_")[0]
        # print(f"Will merge {filepath[0]} with {filepath[1]} and output to {output_filepath}")
        
        pear_path = "~/tools/PEAR/src/pear" 
        command = f"{pear_path} -f {filepath[0]} -r {filepath[1]} -o {output_filepath}"

        subprocess.run(command,
            check=True, text=True, shell=True
        )


def run_seqtk(input_file, output_file, depth):
    command = "seqtk sample {input_file} {depth} >> {output_file}"
    
    subprocess.run(command,
        check=True, text=True, shell=True)


def main():
    directory = get_args()
    all_fastqs = get_paths(directory)
    print(all_fastqs)

if __name__=="__main__":
    main()