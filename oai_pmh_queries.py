import lxml
from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader
from oaipmh import error
from urllib import error as urlerror

registry = MetadataRegistry()
registry.registerReader('oai_dc', oai_dc_reader)

def get_software_set(oai_url):

    error_urls = []
    
    try:
        print(oai_url)
        client = Client(oai_url, registry)
        for i in client.listSets():
            print(i)
    except error.NoRecordsMatchError:
        print(oai_url+" No records")
        pass
    except error.BadVerbError:
        error_urls.append(oai_url)
        pass
    except urlerror.HTTPError:
        error_urls.append(oai_url)
        print(oai_url+" urllib.error.HTTPError: 404")
        pass
    except urlerror.URLError:
        print(oai_url + " URLError")
        error_urls.append(oai_url)
        pass
    except TimeoutError:
        print(oai_url + "TimeoutError")
        error_urls.append(oai_url)
        pass
    except error.BadArgumentError:
        print(oai_url + "BadArg")
        error_urls.append(oai_url)
        pass
    except lxml.etree.XMLSyntaxError:
        print(oai_url + "XMLSyntaxError")
        error_urls.append(oai_url)
        pass
    except error.XMLSyntaxError:
        print(oai_url + " XMLSyntaxError")
        pass

def get_software_records(oai_url):

    num_software_records = 0
    client = Client(oai_url, registry)

    try:
        error_urls = []
        for record in client.listRecords(metadataPrefix='oai_dc', set='74797065733D736F667477617265'):
            num_software_records += 1
            print(record[1].getMap(), "records ", num_software_records)
    except error.NoRecordsMatchError:
        print(oai_url+" No records")
        pass
    except error.BadVerbError:
        error_urls.append(oai_url)
        pass
    except urlerror.HTTPError:
        error_urls.append(oai_url)
        print(oai_url+" urllib.error.HTTPError: 404")
        pass
    except urlerror.URLError:
        print(oai_url + " URLError")
        error_urls.append(oai_url)
        pass
    except TimeoutError:
        print(oai_url + "TimeoutError")
        error_urls.append(oai_url)
        pass
    except error.BadArgumentError:
        print(oai_url + "BadArg")
        error_urls.append(oai_url)
        pass
    except lxml.etree.XMLSyntaxError:
        print(oai_url + "XMLSyntaxError")
        error_urls.append(oai_url)
        pass
    except error.XMLSyntaxError:
        print(oai_url + " XMLSyntaxError")
        pass

