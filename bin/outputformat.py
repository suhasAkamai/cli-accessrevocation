# Python edgegrid module
""" Copyright 2015 Akamai Technologies, Inc. All Rights Reserved.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.

 You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import sys
import os
import requests
import logging
import json
import texttable as tt
import datetime


from akamai.edgegrid import EdgeGridAuth, EdgeRc
from config import EdgeGridConfig
if sys.version_info[0] >= 3:
    # python3
    from urllib import parse
else:
    # python2.7
    import urlparse as parse

logger = logging.getLogger(__name__)


def formatOutputIdentifiersList(identifierList, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(identifierList, indent=2))
    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([25, 30])
        ParentTable.set_cols_align(['c', 'c'])
        ParentTable.set_cols_valign(['m', 'm'])
        Parentheader = ['Identifier', 'TTL']
        ParentTable.header(Parentheader)
        for my_item in identifierList:
            Parentrow = [my_item["id"], my_item["ttl"]]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputblocklist(blocklistList, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(blocklistList, indent=2))
    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([20, 20, 20, 25, 20])
        ParentTable.set_cols_align(['c', 'c', 'c', 'c', 'c'])
        ParentTable.set_cols_valign(['m', 'm', 'm', 'm', 'm'])
        Parentheader = ['Name', 'ContractId', 'ID', 'createdBy', 'createdTime']
        ParentTable.header(Parentheader)
        for my_item in blocklistList:
            Parentrow = [my_item["name"], my_item["contractId"],
                         my_item["id"], my_item["createdBy"], datetime.datetime.fromtimestamp(my_item["createdTime"]).strftime('%Y-%m-%d %H:%M:%S')]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputIdentifierList(identifierList, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(identifierList, indent=2))
    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([45, 30])
        ParentTable.set_cols_align(['c', 'c'])
        ParentTable.set_cols_valign(['m', 'm'])
        Parentheader = ['Identifier', 'TTL']
        ParentTable.header(Parentheader)
        Parentrow = [identifierList["id"], identifierList["ttl"]]
        ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputblocklistCount(blocklist_count, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(blocklist_count, indent=2))
    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([25, 25])
        ParentTable.set_cols_align(['c', 'c'])
        ParentTable.set_cols_valign(['m', 'm'])
        Parentheader = ['Count', 'LIMIT']
        ParentTable.header(Parentheader)
        Parentrow = [blocklist_count["count"], blocklist_count["limit"]]
        ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputConnectorList(arlblocklist, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(arlblocklist, indent=2))
    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([25, 25, 35])
        ParentTable.set_cols_align(['c', 'c', 'c'])
        ParentTable.set_cols_valign(['m', 'm', 'm'])
        Parentheader = ['arlId', 'propertyId', 'propertyName']
        ParentTable.header(Parentheader)
        for my_item in arlblocklist:
            Parentrow = [my_item["arlFileId"], my_item["propertyId"],
                         my_item["propertyName"]]
            ParentTable.set_cols_dtype(["t", "t", "t"])
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputRevocationResp(updateResponse):
    print(json.dumps(updateResponse, indent=2))


def formatOutputUnrevocationResp(updateResponse):
    print(json.dumps(updateResponse, indent=2))
