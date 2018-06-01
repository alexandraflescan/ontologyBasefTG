import rdflib
import re


def getLabelOfUri(uri):
    return uri.toPython()

def to_list(results):
    result_list = []
    for line in results:
        for rdf_node in line:
            if not isinstance(rdf_node, rdflib.term.URIRef):
                continue
            rdf_node = rdf_node.toPython()
            if rdf_node.find('#') >= 0:
                result_list.append(rdf_node.split('#')[1])

    return result_list





