from pprint import pprint as pp
from src.read_github_namespace.graph.fetch_org_repos import collate, fetch_org_repos
from src.clone.shell_clone import clone_list
from src.arg_parsing.parse_cmd_line import parse_cmd_line
from tabulate import tabulate


def tabulate_nodes(nodes, url_protocol):
    table = []
    for node in nodes:
        row = [node["name"], node[url_protocol]]
        table.append(row)
    print(tabulate(table, headers=["name", "url"], tablefmt="github"))


if __name__ == "__main__":
    args = parse_cmd_line()
    organization = args["org"]
    url_protocol = args["url_proto"]
    to_folder = args["to_folder"]
    results = fetch_org_repos(organization)
    nodes = collate(results)
    # pp(nodes)
    tabulate_nodes(nodes, url_protocol)
    # clone_list(nodes, to_folder, "sshUrl")
