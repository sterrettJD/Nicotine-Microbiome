import urllib.parse
import urllib.request
import pandas as pd


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


def add_to_diamond(responses):
    # using [1:] here drops the "from \t to" in the reponse 
    responses_list = responses.split("\n")[1:]
    response_df = pd.DataFrame([x.split("\t") for x in responses_list], 
                                columns=["query", "name"])

    return response_df

def main():
    responses = get_gene_name(["A0A009SNI0", "A0A084FU31"])
    diamond = read_diamond_df("organisms/Paenarthrobacter_diamond_results.txt")

    #df = add_to_diamond(responses, filepath="organisms/Paenarthrobacter_diamond_results.txt")
    print(diamond)
if __name__=="__main__":
    main()