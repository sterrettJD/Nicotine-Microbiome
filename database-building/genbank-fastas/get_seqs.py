import subprocess
import pandas as pd
import numpy as np

files = ["metacyc-nic-deg-1.txt", "metacyc-nic-deg-2.txt", "metacyc-nic-deg-3.txt"]

def get_accessions(files):
    no_accession = []
    accession_names = []
    accession_ids = []
    for file in files:
        # read in metacyc file
        metacyc = pd.read_csv(file, sep="\t", header=1)
        
        metacyc["accession_present"] = metacyc["Gene Accession"].notna()
        
        # If there's an accession make note of that name and ID
        # otherwise add the name to no accession ID list
        for i in metacyc.index:
            if metacyc.loc[i,"accession_present"]==True:
                id = metacyc.loc[i,"Gene Accession"]
                accession_ids.append(id)

                name = metacyc.loc[i,"Gene name"]
                accession_names.append(name)

            else:
                name = metacyc.loc[i,"Gene name"]
                no_accession.append((name,file))

    return no_accession, accession_names, accession_ids


def check_for_accession_from_other_files(no_accession, accession_names):
    for i, (name, f) in enumerate(no_accession):
        if name in accession_names:
            print(f"No accession ID for {name} in {f}, but it does exist in another file")
            no_accession.pop(i)

    return no_accession 


def get_gene_fasta(id, output_file):
    command = f"esearch -db protein -query '{id}' | efetch -format fasta >> {output_file}"

    subprocess.run(command,
        check=True, text=True, shell=True)

if __name__=="__main__":
    
    no_accession, accession_names, accession_ids = get_accessions(files)
    no_accession = check_for_accession_from_other_files(no_accession, accession_names)

    print(f"\nAccession IDs exist for:")
    for i, name in enumerate(accession_names):
        print(name)
        
    for id in accession_ids:
        get_gene_fasta(id,"sequences.fasta")

    print(f"\nNO accession IDs exist for:")
    for i, (name,f) in enumerate(no_accession):
        print(name)
