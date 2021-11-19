import urllib.parse
import urllib.request
import pandas as pd
import argparse 

def get_args():
    parser = argparse.ArgumentParser(
        description="Getting input/output for mapping uniprot names")

    # add my arguments
    parser.add_argument("-i", "--input_file",
                        type=str, action="store",
                        help="The filepath to your input file")

    parser.add_argument("-o", "--output_file",
                        type=str, action="store",
                        help="The filepath to your output file")

    my_args = parser.parse_args()

    input_file = my_args.input_file
    output_file = my_args.output_file

    return input_file, output_file


def read_diamond_df(filepath):
    diamond_columns = ["Query accession",
                        "Target accession",
                        "Sequence identity",
                        "Length",
                        "Mismatches",
                        "Gap openings",
                        "Query start",
                        "Query end",
                        "Target start",
                        "Target end",
                        "E-value",
                        "Bit score"]

    diamond_df = pd.read_csv(filepath, sep="\t", header=None)
    diamond_df.columns = diamond_columns
    return diamond_df

def gene_acc_from_diamond_df(diamond_df):
    target_acc = diamond_df["Target accession"]
    target_acc = target_acc.apply(lambda x: x.split("|")[1])
    return target_acc.tolist()

def get_gene_name(query_list):
    url = 'https://www.uniprot.org/uploadlists/'

    params = {
    'from': 'ACC+ID',
    'to': 'GENENAME',
    'format': 'tab',
    'query': " ".join(query_list)
    }

    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as f:
        response = f.read()
    return response.decode('utf-8')


def add_to_diamond(responses, diamond_df, export_filepath=None, sep="\t"):
    # using [1:] here drops the "from \t to" in the reponse 
    responses_list = responses.split("\n")[1:]
    responses_df = pd.DataFrame([x.split("\t") for x in responses_list], 
                                columns=["Acc id", "name"])

    diamond_df.loc[:,"Gene name"] = responses_df["name"]

    if export_filepath is not None:
        diamond_df.to_csv(export_filepath, sep=sep)

    return diamond_df


def main():
    input_file, output_file = get_args()
    diamond_df = read_diamond_df(input_file)
    query_list = gene_acc_from_diamond_df(diamond_df)
    responses = get_gene_name(query_list)
    
    df = add_to_diamond(responses, diamond_df, 
                        export_filepath=output_file)
    
    # print(df)
if __name__=="__main__":
    main()