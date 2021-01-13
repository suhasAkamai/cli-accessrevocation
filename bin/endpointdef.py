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

from __future__ import print_function
import sys
import os
import logging
import random
import re
import requests
import json
import urllib
import texttable as tt
from future import standard_library
from future.builtins import next
from future.builtins import object
from http_calls import EdgeGridHttpCaller
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from config import EdgeGridConfig
from subprocess import call
standard_library.install_aliases()
if sys.version_info[0] >= 3:
    # python3
    from urllib import parse
else:
    # python2.7
    import urlparse as parse

logger = logging.getLogger(__name__)

session = requests.Session()
debug = False
verbose = False
cache = False
format = "json"
section_name = "default"

# If all parameters are set already, use them.  Otherwise
# use the config
config = EdgeGridConfig({"verbose": False}, section_name)

if hasattr(config, "debug") and config.debug:
    debug = True

if hasattr(config, "verbose") and config.verbose:
    verbose = True

if hasattr(config, "cache") and config.cache:
    cache = True


# Set the config options
session.auth = EdgeGridAuth(
    client_token=config.client_token,
    client_secret=config.client_secret,
    access_token=config.access_token
)

if hasattr(config, 'headers'):
    session.headers.update(config.headers)

session.headers.update({'User-Agent': "AkamaiCLI"})

baseurl_prd = '%s://%s/' % ('https', config.host)
prdHttpCaller = EdgeGridHttpCaller(session, debug, verbose, baseurl_prd)


def listblocklist(accountSwitchKey=None):
    """ List the blocklist in the account """

    listblocklistEndpoint = '/taas/v2/revocation-lists'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        blocklistId = prdHttpCaller.getResult(listblocklistEndpoint, params)
    else:
        blocklistId = prdHttpCaller.getResult(listblocklistEndpoint)
    return(blocklistId)


def listidentifiers(blocklistId, accountSwitchKey=None):
    """ List the identifiers associated with the blocklist """

    listidentifiersEndpoint = '/taas/v2/revocation-lists/'+str(blocklistId)+'/identifiers'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'blocklistId': int(blocklistId)}
        identifierList = prdHttpCaller.getResult(listidentifiersEndpoint, params)
    else:
        identifierList = prdHttpCaller.getResult(listidentifiersEndpoint)
    return(identifierList)


def getidentifier(blocklistId, identifier, accountSwitchKey=None):
    """ Get identifier details """

    getidentifierEndpoint = '/taas/v1/blacklists/'+str(blocklistId)+'/identifiers/'+str(identifier)
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'blocklistId': int(blocklistId),
                  'identifier': str(identifier)
                  }
        identifierList = prdHttpCaller.getResult(getidentifierEndpoint, params)
    else:
        identifierList = prdHttpCaller.getResult(getidentifierEndpoint)
    return(identifierList)


def getblack_list_arls(blocklistId, accountSwitchKey=None):
    """ Get configs associated with blocklist"""
    getarlblocklistEndpoint = '/taas/v2/revocation-lists/'+str(blocklistId)+'/properties'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'blocklistId': int(blocklistId)
                  }
        arlList = prdHttpCaller.getResult(getarlblocklistEndpoint, params)
    else:
        arlList = prdHttpCaller.getResult(getarlblocklistEndpoint)
    return(arlList)


def getblack_list_count(blocklistId, accountSwitchKey=None):
    """ Get configs associated with blocklist"""
    getcountblocklistEndpoint = '/taas/v2/revocation-lists/'+str(blocklistId)+'/meta'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'blocklistId': int(blocklistId)
                  }
        blocklist_count = prdHttpCaller.getResult(getcountblocklistEndpoint, params)
    else:
        blocklist_count = prdHttpCaller.getResult(getcountblocklistEndpoint)
    return(blocklist_count)


def revoke_token(data, blocklistId, accountSwitchKey=None):
    """ revoke Token"""
    revoketokenEndpoint = ' /taas/v2/revocation-lists/'+str(blocklistId)+'/identifiers/add'

    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'blocklistId': int(blocklistId)

                  }
        createResponse = prdHttpCaller.postResult(revoketokenEndpoint, data, params)
    else:
        createResponse = prdHttpCaller.postResult(revoketokenEndpoint, data)
    return(createResponse)


def unrevoke_token(data, blocklistId, accountSwitchKey=None):
    """ un-revoke Token"""
    unrevoketokenEndpoint = '/taas/v2/revocation-lists/'+str(blocklistId)+'/identifiers/remove'

    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'blocklistId': int(blocklistId)

                  }
        createResponse = prdHttpCaller.postResult(unrevoketokenEndpoint, data, params)
    else:
        createResponse = prdHttpCaller.postResult(unrevoketokenEndpoint, data)
    return(createResponse)
