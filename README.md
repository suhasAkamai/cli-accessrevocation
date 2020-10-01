# Akamai CLI: Access Revocation

This module enables the use of accessrevocation in the Akamai CLI tool

## API Permissions

Please ensure your API client has access to the "accessrevocation" API (you may need to create a separate API client)

## Install

To install, use [Akamai CLI](https://github.com/akamai/cli):

```
$akamai install https://github.com/suhasAkamai/cli-accessrevocation.git
```

You may also use this as a stand-alone command by cloning this repository
and compiling it yourself.

## Usage

```
$akamai accessrevocation [global flags] Commands
```

## Global Flags
- `--edgerc value` — Location of the credentials file (default: user's directory like "/Users/sbharadw") [$AKAMAI_EDGERC]
- `--section value` — Section of the credentials file (default: "default") [$AKAMAI_EDGERC_SECTION]
- `--debug` - `-d` - prints debug information
- `--verbose` - Print verbose information
- `--version`, `-v` — Print the version
- `--help`, `-h` — Show help

## Commands
- `list-tokens` — List identifiers/tokens in the blacklist
- `list-blacklist` — List blacklist in the Account
- `get-token-details` — Get identifier/token details
- `get-configlist` — Get config details associated with blacklist
-  `get-token-count` — Get count of tokens associated with blacklist
-  `revoke-token` — Add the tokens to blacklist
-  `unrevoke-token` — Remove the tokens from the blacklist.


## Examples

#### Help
This displays the usage of accessrevocation Akamai CLI.
```
$akamai ar --help
usage: akamai accessrevocation [-h] [--verbose] [--debug]
                         [--edgerc credentials_file]
                         [--section credentials_file_section]
                         [--accountSwitchKey Account Switch Key]
                         {list-tokens,list-blacklist,get-token-details,get-configlist,get-token-count,revoke-token,unrevoke-token}
                         ...

Process command line options.

positional arguments:
  {list-tokens,list-blacklist,get-token-details,get-configlist,get-token-count,revoke-token,unrevoke-token}
                        commands
    list-tokens         List identifiers/tokens in the blacklist
    list-blacklist      List blacklist in the Account
    get-token-details   Get identifier/token details
    get-configlist      Get config details associated with blacklist
    get-token-count     Get count of tokens associated with blacklist
    revoke-token        Add the tokens to blacklist
    unrevoke-token      Remove the tokens from the blacklist.



optional arguments:
  -h, --help            show this help message and exit
  --verbose, -v         Verbose mode
  --debug, -d           Debug mode (prints HTTP headers)
  --edgerc credentials_file, -e credentials_file
                        Location of the credentials file (default is
                        ~/.edgerc)
  --section credentials_file_section, -c credentials_file_section
                        Credentials file Section's name to use
  --accountSwitchKey Account Switch Key, -a Account Switch Key
                        Switch key to different account
```



#### Usage of list-blacklist Command
This shows how to use list-blacklist .
```
$ akamai ar list-blacklist -h
          [or]
$ akamai ar list-blacklist --help

usage: akamai accessrevocation list-blacklist [-h] [--output-type json/text]

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```

#### List All the blacklist in the account
```
akamai accessrevocation list-blacklist

+----------------------+----------------------+----------------------+---------------------------+----------------------+
|         Name         |      ContractId      |          ID          |         createdBy         |     createdTime      |
+======================+======================+======================+===========================+======================+
| deliveryonlyblacklis |      3-195EOUJ       |          44          |     or7qdn4ton36bn3v      | 2019-11-14 12:00:38  |
|          t2          |                      |                      |                           |                      |
+----------------------+----------------------+----------------------+---------------------------+----------------------+

```

#### List All the blacklist in the Account in Json Format
```
akamai accessrevocation list-blacklist -t json

[
  {
    "name": "deliveryonlyblacklist2",
    "contractId": "3-195EOUJ",
    "id": 44,
    "createdBy": "or7qdn4ton36bn3v",
    "createdTime": 1573713038
  }
]

```


#### Usage of list-tokens  Command
This shows how to use list-tokens .
```
$ akamai ar list-tokens -h
          [or]
$ akamai ar list-tokens --help
usage: akamai accessrevocation list-tokens [-h] [--output-type json/text] blacklistId

positional arguments:
  blacklistId           blacklist from which identifiers need to be retrieve

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```


#### List All the list-tokens in the blacklist
This shows how to list all the tokens or identifiers in the blacklist
```
$ akamai accessrevocation list-tokens 44

+---------------------------+--------------------------------+
|        Identifier         |              TTL               |
+===========================+================================+
|         sqatest5          |             85077              |
+---------------------------+--------------------------------+
|         sqatest6          |             85077              |
+---------------------------+--------------------------------+

```

#### List All the list-tokens in the blacklist in Json Format
This shows how to list all the tokens or identifiers in the blacklis in Json Format.
```
$ akamai accessrevocation list-tokens 44 -t json



[
  {
    "id": "sqatest5",
    "ttl": 85028
  },
  {
    "id": "sqatest6",
    "ttl": 85028
  }
]
```
#### Usage of get-token-details Command
This shows how to use get-token-details command.
```
$ akamai ar get-token-details -h
          [or]
$ akamai ar get-token-details --help
usage: akamai accessrevocation get-token-details [-h] [--output-type json/text] blacklistId tokenID

positional arguments:
  blacklistId           blacklist from which identifiers need to be retrieved
  tokenID               identifiers/token details which need to be retrieved

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```

#### Get token details from  the blacklist
This shows how to get token or identifier details from the blacklist
```
akamai akamai accessrevocation get-token-details 44 sqatest5

+-----------------------------------------------+--------------------------------+
|                  Identifier                   |              TTL               |
+===============================================+================================+
|                   sqatest5                    |             84773              |
+-----------------------------------------------+--------------------------------

```


#### Usage of get-configlist Command
This shows how to use get-configlist command to get the list of configurations associated with the blacklist.
```
$ akamai ar get-configlist -h
          [or]
$ akamai ar get-configlist --help
usage: akamai accessrevocation get-configlist [-h] [--output-type json/text] blacklistId

positional arguments:
  blacklistId           blacklist for which associated configs needs to be retrieved

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text


```
#### Get config list where AR is enabled
This shows how to get config list where AR is enabled
```
akamai akamai accessrevocation get-configlist 44
+---------------------------+---------------------------+-------------------------------------+
|           arlId           |        propertyId         |            propertyName             |
+===========================+===========================+=====================================+
|          581689           |         1.619e+08         |         trproductiontesting         |
+---------------------------+---------------------------+-------------------------------------+
|         2.000e+08         |         1.833e+08         |             trtemptest2             |
+---------------------------+---------------------------+-------------------------------------+
|          601739           |         1.747e+08         |      cogsperf-amd-allfeatures       |
+---------------------------+---------------------------+-------------------------------------+
|         2.000e+08         |         1.833e+08         |             trtemptest              |
+---------------------------+---------------------------+-------------------------------------+
|          611925           |         1.801e+08         |       tr-Irdeto.akamaized.net       |
+---------------------------+---------------------------+-------------------------------------+
|          604205           |         1.761e+08         |         amdsqa-goldenconfig         |
+---------------------------+---------------------------+-------------------------------------+
```


#### Usage of get-token-count Command
This shows how to use get-token-count command to get the details on number of tokens/ identifiers in the blacklist and current limit
```
$ akamai ar get-token-count -h
          [or]
$ akamai ar get-token-count --help
usage: akamai accessrevocation get-token-count [-h] [--output-type json/text] blacklistId

positional arguments:
  blacklistId           blacklist for which count of token needs to be retrieved

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text  Output type {json, text}. Default is text

```

#### Get the count of tokens/identifiers in the blacklist.
Retrieve the details of a stream.
```
$ akamai akamai accessrevocation get-token-count 44

+---------------------------+---------------------------+
|           Count           |           LIMIT           |
+===========================+===========================+
|             2             |           25000           |
+---------------------------+---------------------------+

```

#### Usage of Revoke Token Command
This shows how to use revoke-token command which basically add the token/identifier to blacklist .
```
$ akamai ar revoke-token -h
          [or]
$ akamai ar arevoke-token --help

usage: akamai accessrevocation revoke-token [-h] blacklistId file

positional arguments:
  blacklistId  blacklist for which token needs to be added for Revocation
  file         Json File consiting of token Details

optional arguments:
  -h, --help   show this help message and exit

Sample JSON Input to add 2 tokens

[
    {
        "id": "sdasd345466dg",
        "durationSeconds": 18000
    },
    {
        "id": "utrfhasdf8990",
        "durationSeconds": 3600
    }
]


```


#### Revoking the Token - Adding the token to blacklist
This command provides details on how to add the token to the blacklist
```

 akamai accessrevocation revoke-token 44 /Users/sbharadw/Documents/cli-AR/identifier.json

[{"id": "sdasd345466dg", "durationSeconds": 18000}, {"id": "utrfhasdf8990", "durationSeconds": 3600}]
{
  "count": 6,
  "limit": 25000
}



```

#### Usage of UnRevoke Token Command
This shows how to use unrevoke-token command which basically remove the token/identifier to blacklist .
```
$ akamai ar unrevoke-token -h
          [or]
$ akamai ar unrevoke-token --help

usage: akamai accessrevocation unrevoke-token [-h] blacklistId file

positional arguments:
  blacklistId  blacklist from which token needs to be removed
  file         Json File consiting of token Details

optional arguments:
  -h, --help   show this help message and exit

Sample JSON Input to remove 3 tokens

[
    "sqwoieksjbsdf3455",
    "9082349u534589824",
    "68sd899ff09sdf8787"
]


```


#### UnRevoking the Token - Removing the token from the blacklist
This command provides details on how to remove the token from the blacklist
```

 akamai accessrevocation unrevoke-token 44 /Users/sbharadw/Documents/cli-AR/identifier.json

["sdasd345466dg", "utrfhasdf8990"]
{
  "count": 4,
  "limit": 25000
}


```
