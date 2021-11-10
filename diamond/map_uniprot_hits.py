import urllib.parse
import urllib.request

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

def main():
    response = get_gene_name(["A0A009SNI0", "A0A084FU31"])
    print(response)

if __name__=="__main__":
    main()