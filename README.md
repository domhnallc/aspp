
This code was used to generate the dataset for our paper, under review at PeerJ Computer Science, titled "Where is all the research software? An
analysis of software in UK academic repositories."

**Important Files**

**core_api_queries.core_query.pi:**

Contains functions to retrieve data from CORE API v3. Authorised using the ./apikey from core.ac.uk.
Based on examples provided by CORE at https://github.com/oacore/apiv3-webinar/

**submission dataset_release_v1.csv:**

The dataset built in this research.  The base dataset can be created using create_base_data_set.py, which retrieves metadata from Core.ac.uk on all repositories from the UK within their platform.  This was further manually edited to remove non-academic institutes.

Cite as:

Domhnall Carlin. (2023). A census of research software in 171 academic institutional repositories. (Version 1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7603444



**Dataset Fields:**
| Item                  | Description                                                                                                                                                     |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \-----------          | \-------------                                                                                                                                                  |
| URL                   | The OAI url                                                                                                                                                     |
| id                    | CORE Identifier                                                                                                                                                 |
| openDoarId            | Open DOAR identifier                                                                                                                                            |
| name                  | Name of repository                                                                                                                                              |
| Russell_member        | If the university is a member of the Russell Group of research intensive universities                                                                           |
| RSE_group             | If an RSE group is present (based on Soc of RSE data)                                                                                                           |
| email                 | Redacted                                                                                                                                                        |
| uri                   | Not used                                                                                                                                                        |
| uni_sld               | Second level domain (the part of the url between . And .ac.uk                                                                                                   |
| homepageUrl           | University website                                                                                                                                              |
| source                | Not used                                                                                                                                                        |
| ris_software          | the Research Information System software used                                                                                                                   |
| ris_software_enum     | Resolve ris_software into similar types (e.g. Eprints 3, EPrints3.3.16 both equal eprints)                                                                      |
| metadataFormat        | the protocol used for metadata                                                                                                                                  |
| createdDate           | Repository creation date                                                                                                                                        |
| location              | location of university                                                                                                                                          |
| logo                  | University logo (resolves in error)                                                                                                                             |
| type                  | Only = Repository for this dataset. Can be = journal etc.                                                                                                       |
| stats                 | Not used                                                                                                                                                        |
| contains_software_set | Whether the OAI-PMH software set is present in the repository.                                                                                                  |
| Num_sw_records        | The response of the OAI-PMH query for software (erroneous as discussed in paper)                                                                                |
| Error                 | The category of error returned by the experiment’s OAI-PMH queries (see paper)                                                                                  |
| Manual_Num_sw_records | The true amount of software contained in the repository as found by a manual exhaustive search of each university website                                       |
| Category              | Whether the repository (a) contains software; (b) can contain software, but doesn’t yet; (c) has no separate type of research output called software or similar |
