# Akamai CLI: Access Revocation

This module enables the use of accessrevocation in the Akamai CLI tool

## API Permissions

Please ensure your API client has access to the "accessrevocation" API (you may need to create a separate API client)

## Install

To install, use [Akamai CLI](https://github.com/akamai/cli):

```
$ akamai install https://github.com/suhasAkamai/cli-accessrevocation.git
```

You may also use this as a stand-alone command by cloning this repository
and compiling it yourself.

## Usage

```
$ akamai accessrevocation [global flags] Commands OR akamai ar [global flags] Commands
```

## Global Flags
- `--edgerc value` — Location of the credentials file (default: user's directory like "/Users/sbharadw") [$AKAMAI_EDGERC]
- `--section value` — Section of the credentials file (default: "default") [$AKAMAI_EDGERC_SECTION]
- `--debug` - `-d` - prints debug information
- `--verbose` - Print verbose information
- `--version`, `-v` — Print the version
- `--help`, `-h` — Show help

## Commands
- `list-tokens` — List identifiers/tokens in the blocklist
- `list-blocklist` — List blocklist in the Account
- `get-token-details` — Get identifier/token details
- `get-configlist` — Get config details associated with blocklist
-  `get-token-count` — Get count of tokens associated with blocklist
-  `revoke-token` — Add the tokens to blocklist
-  `unrevoke-token` — Remove the tokens from the blocklist.


## Examples

#### Help
This displays the usage of accessrevocation Akamai CLI.
```
$ akamai ar --help
usage: akamai accessrevocation [-h] [--verbose] [--debug]
                         [--edgerc credentials_file]
                         [--section credentials_file_section]
                         [--accountSwitchKey Account Switch Key]
                         {list-tokens,list-blocklist,get-token-details,get-configlist,get-token-count,revoke-token,unrevoke-token}
                         ...

Process command line options.

positional arguments:
  {list-tokens,list-blocklist,get-token-details,get-configlist,get-token-count,revoke-token,unrevoke-token}
                        commands
    list-tokens         List identifiers/tokens in the blocklist
    list-blocklist      List blocklist in the Account
    get-token-details   Get identifier/token details
    get-configlist      Get config details associated with blocklist
    get-token-count     Get count of tokens associated with blocklist
    revoke-token        Add the tokens to blocklist
    unrevoke-token      Remove the tokens from the blocklist.



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



#### Usage of list-blocklist Command
This shows how to use list-blocklist .
```
$ akamai ar list-blocklist -h
          [or]
$ akamai ar list-blocklist --help

usage: akamai accessrevocation list-blocklist [-h] [--output-type json/text]

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```

#### List All the blocklist in the account
```
$ akamai accessrevocation list-blocklist

+----------------------+----------------------+----------------------+---------------------------+----------------------+
|         Name         |      ContractId      |          ID          |         createdBy         |     createdTime      |
+======================+======================+======================+===========================+======================+
| deliveryonlyblacklis |      3-195EOUJ       |          44          |     or7qdn4ton36bn3v      | 2019-11-14 12:00:38  |
|          t2          |                      |                      |                           |                      |
+----------------------+----------------------+----------------------+---------------------------+----------------------+

```

#### List All the blocklist in the Account in Json Format
```
$ akamai accessrevocation list-blocklist -t json

[
  {
    "name": "deliveryonlyblocklist2",
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
usage: akamai accessrevocation list-tokens [-h] [--output-type json/text] blocklistId

positional arguments:
  blocklistId           blocklist from which identifiers need to be retrieve

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```


#### List All the list-tokens in the blocklist
This shows how to list all the tokens or identifiers in the blocklist
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

#### List All the list-tokens in the blocklist in Json Format
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
usage: akamai accessrevocation get-token-details [-h] [--output-type json/text] blocklistId tokenID

positional arguments:
  blocklistId           blocklist from which identifiers need to be retrieved
  tokenID               identifiers/token details which need to be retrieved

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```

#### Get token details from  the blocklist
This shows how to get token or identifier details from the blocklist
```
$ akamai accessrevocation get-token-details 44 sqatest5

+-----------------------------------------------+--------------------------------+
|                  Identifier                   |              TTL               |
+===============================================+================================+
|                   sqatest5                    |             84773              |
+-----------------------------------------------+--------------------------------

```


#### Usage of get-configlist Command
This shows how to use get-configlist command to get the list of configurations associated with the blocklist.
```
$ akamai ar get-configlist -h
          [or]
$ akamai ar get-configlist --help
usage: akamai accessrevocation get-configlist [-h] [--output-type json/text] blocklistId

positional arguments:
  blocklistId           blocklist for which associated configs needs to be retrieved

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text


```
#### Get config list where AR is enabled
This shows how to get config list where AR is enabled
```
$ akamai accessrevocation get-configlist 44
+---------------------------+---------------------------+-------------------------------------+
|           arlId           |        propertyId         |            propertyName             |
+===========================+===========================+=====================================+
|          581689           |         161874041         |         trproductiontesting         |
+---------------------------+---------------------------+-------------------------------------+
|         200030526         |         183344635         |             trtemptest2             |
+---------------------------+---------------------------+-------------------------------------+
|          604205           |         176084367         |         amdsqa-goldenconfig         |
+---------------------------+---------------------------+-------------------------------------+
|         200050511         |         183843497         |            trmdp3558test            |
+---------------------------+---------------------------+-------------------------------------+
|          601739           |         174668974         |      cogsperf-amd-allfeatures       |
+---------------------------+---------------------------+-------------------------------------+
|         200030525         |         183344622         |             trtemptest              |
+---------------------------+---------------------------+-------------------------------------+
```


#### Usage of get-token-count Command
This shows how to use get-token-count command to get the details on number of tokens/ identifiers in the blocklist and current limit
```
$ akamai ar get-token-count -h
          [or]
$ akamai ar get-token-count --help
usage: akamai accessrevocation get-token-count [-h] [--output-type json/text] blocklistId

positional arguments:
  blocklistId           blocklist for which count of token needs to be retrieved

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text  Output type {json, text}. Default is text

```

#### Get the count of tokens/identifiers in the blocklist.
Retrieve the details of a stream.
```
$ akamai accessrevocation get-token-count 44

+---------------------------+---------------------------+
|           Count           |           LIMIT           |
+===========================+===========================+
|             2             |           25000           |
+---------------------------+---------------------------+

```

#### Usage of Revoke Token Command
This shows how to use revoke-token command which basically add the token/identifier to blocklist .
```
$ akamai ar revoke-token -h
          [or]
$ akamai ar arevoke-token --help

usage: akamai accessrevocation revoke-token [-h] blocklistId file

positional arguments:
  blocklistId  blocklist for which token needs to be added for Revocation
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


#### Revoking the Token - Adding the token to blocklist
This command provides details on how to add the token to the blocklist
```

$ akamai accessrevocation revoke-token 44 /Users/sbharadw/Documents/cli-AR/identifier.json

[{"id": "sdasd345466dg", "durationSeconds": 18000}, {"id": "utrfhasdf8990", "durationSeconds": 3600}]
{
  "count": 6,
  "limit": 25000
}



```

#### Usage of UnRevoke Token Command
This shows how to use unrevoke-token command which basically remove the token/identifier to blocklist .
```
$ akamai ar unrevoke-token -h
          [or]
$ akamai ar unrevoke-token --help

usage: akamai accessrevocation unrevoke-token [-h] blocklistId file

positional arguments:
  blocklistId  blocklist from which token needs to be removed
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


#### UnRevoking the Token - Removing the token from the blocklist
This command provides details on how to remove the token from the blocklist
```

$ akamai accessrevocation unrevoke-token 44 /Users/sbharadw/Documents/cli-AR/identifier.json

["sdasd345466dg", "utrfhasdf8990"]
{
  "count": 4,
  "limit": 25000
}


```
