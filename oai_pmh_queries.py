import lxml
import json
from oaipmh.client import Client
from oaipmh.validation import validate
from oaipmh.metadata import MetadataRegistry, oai_dc_reader
from oaipmh import error
from urllib import error as urlerror

registry = MetadataRegistry()
registry.registerReader('oai_dc', oai_dc_reader)
SOFTWARE_SET = '74797065733D736F667477617265'


def get_software_set(oai_url):
    error_urls = []

    try:
        print(f"[] Getting sets from {oai_url}")
        client = Client(oai_url, registry)
        output = {"URL": oai_url,
                  "Sets": None,
                  "Error": "No error"
                  }
        tuple_holder = []
        for i in client.listSets():
            #print(i)
            tuple_holder.append(i)
        output['Sets'] = tuple_holder
        #print(tuple_holder)

    except error.NoRecordsMatchError:
    # print(f"{oai_url} No records")
        pass
    except error.BadVerbError:
    # error_urls.append(oai_url)
        output["Error"] = "BadVerbError"
        pass
    except error.NoSetHierarchyError:
        # error_urls.append(oai_url)
        output["Error"] = "NoSetHierarchyError"
        # print(f"{oai_url} urllib.error.HTTPError: 404")
        pass
    except urlerror.HTTPError:
        # error_urls.append(oai_url)
        output["Error"] = "404 error"
        # print(f"{oai_url} urllib.error.HTTPError: 404")
        pass
    except urlerror.URLError:
        output["Error"] = "URL error"
        # print(f"{oai_url} URLError")
        # error_urls.append(oai_url)
        pass
    except TimeoutError:
        output["Error"] = "Timeout error"
        print(f"{oai_url} TimeoutError")
        # error_urls.append(oai_url)
        pass
    except error.BadArgumentError:
        output["Error"] = "Bad Argument Error"
        # print(f"{oai_url} BadArg")
        # error_urls.append(oai_url)
        pass
    except lxml.etree.XMLSyntaxError:
        output["Error"] = "lxml XML syntax error"
        # print(f"{oai_url} XMLSyntaxError")
        # error_urls.append(oai_url)
        pass
    except error.XMLSyntaxError:
        output["Error"] = "OAI XML Syntax error"
        # print(f"{oai_url} XMLSyntaxError")
        pass
    except AttributeError:
        output["Error"] = "AttributeError getMap"
        pass
    except ValueError:
        output["Error"] = "ValueError unknown url type"
        pass
    return output


def get_software_records(oai_url):
    num_software_records = 0
    client = Client(oai_url, registry)
    error_urls = []
    output = {"URL": oai_url,
              "Num_sw_records": num_software_records,
              "Error": "No error"
              }
    try:

        for record in client.listRecords(metadataPrefix='oai_dc', set=SOFTWARE_SET):
            num_software_records += 1
            # print(record[1].getMap(), "records ", num_software_records)
            output["URL"] = oai_url
            output["Num_sw_records"] = num_software_records

    except error.NoRecordsMatchError:
        # print(f"{oai_url} No records")
        pass
    except error.BadVerbError:
        # error_urls.append(oai_url)
        output["Error"] = "BadVerbError"
        pass
    except error.NoSetHierarchyError:
        # error_urls.append(oai_url)
        output["Error"] = "NoSetHierarchyError"
        # print(f"{oai_url} urllib.error.HTTPError: 404")
        pass
    except urlerror.HTTPError:
        # error_urls.append(oai_url)
        output["Error"] = "404 error"
        # print(f"{oai_url} urllib.error.HTTPError: 404")
        pass
    except urlerror.URLError:
        output["Error"] = "URL error"
        # print(f"{oai_url} URLError")
        # error_urls.append(oai_url)
        pass
    except TimeoutError:
        output["Error"] = "Timeout error"
        print(f"{oai_url} TimeoutError")
        # error_urls.append(oai_url)
        pass
    except error.BadArgumentError:
        output["Error"] = "Bad Argument Error"
        # print(f"{oai_url} BadArg")
        # error_urls.append(oai_url)
        pass
    except lxml.etree.XMLSyntaxError:
        output["Error"] = "lxml XML syntax error"
        # print(f"{oai_url} XMLSyntaxError")
        # error_urls.append(oai_url)
        pass
    except error.XMLSyntaxError:
        output["Error"] = "OAI XML Syntax error"
        # print(f"{oai_url} XMLSyntaxError")
        pass
    except AttributeError:
        output["Error"] = "AttributeError getMap"
        pass
    except ValueError:
        output["Error"] = "ValueError unknown url type"
        pass
    return output


def write_to_file(all_output: dict, json_file_out: str):
    with open(json_file_out, 'w') as fp:
        json.dump(all_output, fp, indent=4)
