from dataclasses import dataclass
from typing import Any


@dataclass
class SearchObject:
    field : str
    operator : str
    value : Any


@dataclass
class SortObject:
    field : str
    order : str


@dataclass
class Indicators:
    ips : list[str]
    hashes : list[str]
    domain_names : list[str]
    urls : list[str]


@dataclass
class CommunityThreat:
    threat : str
    note : str
    indicators : Indicators


@dataclass
class Assignee:
    email : str