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
- `list-tokens` — List identifiers/tokens in the revocation list
- `get-revocation-lists` — List revocation List in the Account
- `get-token-details` — Get identifier/token details
- `get-configlist` — Get config details associated with revocation list
-  `get-token-count` —  Get count of tokens associated with revocation list
-  `revoke-token` — Add the tokens to revocation list
-  `unrevoke-token` — Remove the tokens from the revocation list


## Examples

#### Help
This displays the usage of accessrevocation Akamai CLI.
```
$ akamai ar --help
usage: akamai-accessrevocation [-h] [--verbose] [--debug]
                               [--edgerc credentials_file]
                               [--section credentials_file_section]
                               [--accountSwitchKey Account Switch Key]
                               {list-tokens,get-revocation-lists,get-token-details,get-configlist,get-token-count,revoke-token,unrevoke-token}
                               ...

Process command line options.

positional arguments:
  {list-tokens,get-revocation-lists,get-token-details,get-configlist,get-token-count,revoke-token,unrevoke-token}
                        commands
    list-tokens         List identifiers/tokens in the revocation list
    get-revocation-lists List revocation List in the Account
    get-token-details   Get identifier/token details
    get-configlist      Get config details associated with revocation list
    get-token-count     Get count of tokens associated with revocation list
    revoke-token        Add the tokens to revocation list
    unrevoke-token      Remove the tokens from the revocation list

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



#### Usage of get-revocation-lists Command
This shows how to use get-revocation-lists .
```
$ akamai ar get-revocation-lists -h
          [or]
$ akamai ar get-revocation-lists --help

usage: akamai accessrevocation get-revocation-lists [-h] [--output-type json/text]

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```

#### List All the revocation lists in the account
```
$ akamai accessrevocation get-revocation-lists

+----------------------+----------------------+----------------------+---------------------------+----------------------+
|         Name         |      ContractId      |          ID          |         createdBy         |     createdTime      |
+======================+======================+======================+===========================+======================+
|      trsqa2acc       |      M-2549SDK       |         445          |     s7r4wvcn3bg5z7bc      | 2020-09-17 12:23:47  |
+----------------------+----------------------+----------------------+---------------------------+----------------------+

```

#### List All the revocation lists in the account in JSON Format
```
$ akamai accessrevocation get-revocation-lists -t json

[
  {
    "name": "trsqa2acc",
    "contractId": "M-2549SDK",
    "id": 445,
    "createdBy": "s7r4wvcn3bg5z7bc",
    "createdTime": 1600325627
  }
]

```


#### Usage of list-tokens  Command
This shows how to use list-tokens .
```
$ akamai ar list-tokens -h
          [or]
$ akamai ar list-tokens --help
usage: akamai-accessrevocation list-tokens [-h] [--output-type json/text] revocation_listId

positional arguments:
  revocation_listId     revocation list from which identifiers need to be
                        retrieve

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```


#### List All the list-tokens in the revocation list
This shows how to list all the tokens or identifiers in the revocation list
```
$ akamai accessrevocation list-tokens 445

+---------------------------+--------------------------------+
|        Identifier         |              TTL               |
+===========================+================================+
|       sdasd345466dg       |             17840              |
+---------------------------+--------------------------------+
|     sqwoieksjbsdf3455     |              3273              |
+---------------------------+--------------------------------+
|       utrfhasdf8990       |              3440              |
+---------------------------+--------------------------------+

```

#### List All the list-tokens in the revocation list in JSON Format
This shows how to list all the tokens or identifiers in the revocation list in JSON Format.
```
$ akamai accessrevocation list-tokens 445 -t json

[
  {
    "id": "sdasd345466dg",
    "ttl": 17083
  },
  {
    "id": "sqwoieksjbsdf3455",
    "ttl": 2516
  },
  {
    "id": "utrfhasdf8990",
    "ttl": 2683
  }
]

```
#### Usage of get-token-details Command
This shows how to use get-token-details command.
```
$ akamai ar get-token-details -h
          [or]
$ akamai ar get-token-details --help
usage: akamai-accessrevocation get-token-details [-h]
                                                 [--output-type json/text]
                                                 revocation_listId tokenID

positional arguments:
  revocation_listId     revocation list from which identifiers need to be
                        retrieved
  tokenID               identifiers/token details which need to be retrieved

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```

#### Get token details from  the revocation list
This shows how to get token or identifier details from the revocation list
```
$ akamai accessrevocation accessrevocation get-token-details 445 sdasd345466dg

+-----------------------------------------------+--------------------------------+
|                  Identifier                   |              TTL               |
+===============================================+================================+
|                 sdasd345466dg                 |             17890              |
+-----------------------------------------------+--------------------------------+

```


#### Usage of get-configlist Command
This shows how to use get-configlist command to get the list of configurations associated with the revocation list.
```
$ akamai ar get-configlist -h
          [or]
$ akamai ar get-configlist --help
usage: akamai-accessrevocation get-configlist [-h] [--output-type json/text]
                                              revocation_listId

positional arguments:
  revocation_listId     revocation list for which associated configs needs to
                        be retrieved

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```
#### Get config list where AR is enabled
This shows how to get config list where Access Revocation behavior is enabled and tied to revocation list
```
$ akamai accessrevocation get-configlist 445
+---------------------------+---------------------------+-------------------------------------+
|           arlId           |        propertyId         |            propertyName             |
+===========================+===========================+=====================================+
|          581689           |         161874041         |         trproductiontesting         |
+---------------------------+---------------------------+-------------------------------------+

```


#### Usage of get-token-count Command
This shows how to use get-token-count command to get the details on number of tokens/ identifiers in the revocation list and current limit
```
$ akamai ar get-token-count -h
          [or]
$ akamai ar get-token-count --help
usage: akamai-accessrevocation get-token-count [-h] [--output-type json/text]
                                               revocation_listId

positional arguments:
  revocation_listId     revocation list for which count of token needs to be
                        retrieved

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text

```

#### Get the count of tokens/identifiers in the revocation lsit.
Retrieve the details of a stream.
```
$ akamai accessrevocation get-token-count 445

+---------------------------+---------------------------+
|           Count           |           LIMIT           |
+===========================+===========================+
|             3             |           25000           |
+---------------------------+---------------------------+

```

#### Usage of Revoke Token Command
This shows how to use revoke-token command which basically add the token/identifier to revocation list .
```
$ akamai ar revoke-token -h
          [or]
$ akamai ar arevoke-token --help

usage: akamai-accessrevocation revoke-token [-h] revocation_listId file

positional arguments:
  revocation_listId  revocation list for which token needs to be added for
                     Revocation
  file               Json File consiting of token Details

optional arguments:
  -h, --help         show this help message and exit

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


#### Revoking the Token - Adding the token to revocation list
This command provides details on how to add the token to the revocation list
```

$ akamai accessrevocation revoke-token 445 identifier.json

[{"id": "sdasd345466dg", "durationSeconds": 18000}, {"id": "utrfhasdf8990", "durationSeconds": 3600}]
{
  "count": 6,
  "limit": 25000
}



```

#### Usage of UnRevoke Token Command
This shows how to use unrevoke-token command which basically remove the token/identifier from the revocation list .
```
$ akamai ar unrevoke-token -h
          [or]
$ akamai ar unrevoke-token --help

usage: akamai-accessrevocation unrevoke-token [-h] revocation_listId file

positional arguments:
  revocation_listId  revocation list from which token needs to removed
  file               Json File consiting of token Details

optional arguments:
  -h, --help         show this help message and exit

Sample JSON Input to remove 3 tokens

[
    "sqwoieksjbsdf3455",
    "9082349u534589824",
    "68sd899ff09sdf8787"
]


```


#### UnRevoking the Token - Removing the token from the revocation list
This command provides details on how to remove the token from the revocation list
```

$ akamai accessrevocation unrevoke-token 445 identifier.json

["sdasd345466dg", "utrfhasdf8990"]
{
  "count": 4,
  "limit": 25000
}


```
