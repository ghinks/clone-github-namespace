import os
from pathlib import Path
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

token = os.getenv("GITHUB_TOKEN")
reqHeaders = {
    'Authorization': 'Bearer ' + token
}
# TODO create a unit test , look into [mock](https://pypi.org/project/pytest-asyncio/)

def fetch_org_repos(organization):
    # Select your transport with a defined url endpoint
    transport = AIOHTTPTransport(url="https://api.github.com/graphql", headers=reqHeaders)

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    query_text = ""
    query_file = Path(__file__).with_name('org-repos.graphql')
    with query_file.open('r') as f:
        query_text = f.read()
    query = gql(query_text)

    params = {
        "login": organization
    }

    result = client.execute(query, variable_values=params)
    return result

def collate(data):
    try:
        pass
        nodes = data["organization"]["repositories"]["nodes"]
        return nodes
    except Exception as err:
        print(f"Unexpected {err}")
        raise err
