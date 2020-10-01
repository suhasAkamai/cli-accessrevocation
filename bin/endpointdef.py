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


def listblacklist(accountSwitchKey=None):
    """ List the blacklist in the account """

    listBlacklistEndpoint = '/taas/v1/blacklists'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        blackListId = prdHttpCaller.getResult(listBlacklistEndpoint, params)
    else:
        blacklistId = prdHttpCaller.getResult(listBlacklistEndpoint)
    return(blacklistId)


def listidentifiers(blacklistId, accountSwitchKey=None):
    """ List the identifiers associated with the blacklist """

    listidentifiersEndpoint = '/taas/v1/blacklists/'+str(blacklistId)+'/identifiers'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'blacklistId': int(blacklistId)}
        identifierList = prdHttpCaller.getResult(listidentifiersEndpoint, params)
    else:
        identifierList = prdHttpCaller.getResult(listidentifiersEndpoint)
    return(identifierList)


def getidentifier(blacklistId, identifier, accountSwitchKey=None):
    """ Get identifier details """

    getidentifierEndpoint = '/taas/v1/blacklists/'+str(blacklistId)+'/identifiers/'+str(identifier)
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'blacklistId': int(blacklistId),
                  'identifier': str(identifier)
                  }
        identifierList = prdHttpCaller.getResult(getidentifierEndpoint, params)
    else:
        identifierList = prdHttpCaller.getResult(getidentifierEndpoint)
    return(identifierList)


def getblack_list_arls(blacklistId, accountSwitchKey=None):
    """ Get configs associated with blacklist"""
    getarlblacklistEndpoint = '/taas/v1/blacklists/'+str(blacklistId)+'/properties'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'blacklistId': int(blacklistId)
                  }
        arlList = prdHttpCaller.getResult(getarlblacklistEndpoint, params)
    else:
        arlList = prdHttpCaller.getResult(getarlblacklistEndpoint)
    return(arlList)


def getblack_list_count(blacklistId, accountSwitchKey=None):
    """ Get configs associated with blacklist"""
    getcountblacklistEndpoint = '/taas/v1/blacklists/'+str(blacklistId)+'/meta'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'blacklistId': int(blacklistId)
                  }
        blackList_count = prdHttpCaller.getResult(getcountblacklistEndpoint, params)
    else:
        blackList_count = prdHttpCaller.getResult(getcountblacklistEndpoint)
    return(blackList_count)


def revoke_token(data, blacklistId, accountSwitchKey=None):
    """ revoke Token"""
    revoketokenEndpoint = '/taas/v1/blacklists/'+str(blacklistId)+'/identifiers/add'

    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'blacklistId': int(blacklistId)

                  }
        createResponse = prdHttpCaller.postResult(revoketokenEndpoint, data, params)
    else:
        createResponse = prdHttpCaller.postResult(revoketokenEndpoint, data)
    return(createResponse)


def unrevoke_token(data, blacklistId, accountSwitchKey=None):
    """ un-revoke Token"""
    unrevoketokenEndpoint = '/taas/v1/blacklists/'+str(blacklistId)+'/identifiers/remove'

    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'blacklistId': int(blacklistId)

                  }
        createResponse = prdHttpCaller.postResult(unrevoketokenEndpoint, data, params)
    else:
        createResponse = prdHttpCaller.postResult(unrevoketokenEndpoint, data)
    return(createResponse)