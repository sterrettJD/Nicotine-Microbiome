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


def add_to_diamond(responses, diamond_df):
    # using [1:] here drops the "from \t to" in the reponse 
    responses_list = responses.split("\n")[1:]
    responses_df = pd.DataFrame([x.split("\t") for x in responses_list], 
                                columns=["Acc id", "name"])

    print("responses length" + str(responses_df.shape))
    diamond_df.loc[:,"Gene name"] = responses_df["name"]

    return diamond_df

def main():
    diamond_df = read_diamond_df("organisms/Paenarthrobacter_diamond_results.txt")
    query_list = gene_acc_from_diamond_df(diamond_df)
    print("query length" + str(len(query_list)))
    responses = get_gene_name(query_list)
    
    df = add_to_diamond(responses, diamond_df)
    
    print(df)
if __name__=="__main__":
    main()