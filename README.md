# autoTreeFormat
Command line interface that converts file structure to easy to read text files. Perfect for README's. 

# Quick Start
python autoTree.py -f [directory name]
```
python autoTree.py -f Example
```
 
Output:
```
Example                                #
├── build                              #
│   ├── resources                      #
│   │   └── dog.jpg                    #
│   └── src                            #
│       ├── addition.py                #
│       └── helloworld.py              #
├── docs                               #
├── License.txt                        #
├── src                                #
├── tools                              #
├── test                               #
│   ├── benchmarks                     #
│   ├── integration                    #
│   └── unit                           #
└── zz                                 #
```

# Parameters
| Parameter    | Description                            | Default                     |
| :---------:  |:-------------                          | :-----                      |
| -f           | Name of directory                      | Current working directory   |
| -t           | Text file name                         | README_FILE_STRUCTURE.txt   |
| -b           | Directory/File names to blacklist      | None                        |
| -s           | Include system files                   | True                        |
| -a           | Sort alphabetically                    | False                       |
| -c           | Include Comment fields                 | True                        |

## Examples
Blacklist:
```
python autoTree.py -f Example -b tools zz helloworld.py
```

Output:
```
Example                                #
├── build                              #
│   ├── resources                      #
│   │   └── dog.jpg                    #
│   └── src                            #
│       └── addition.py                #
├── docs                               #
├── License.txt                        #
├── src                                #
└── test                               #
    ├── benchmarks                     #
    ├── integration                    #
    └── unit                           #
```

***
No comment fields:
```
python autoTree.py -f Example -c false
```

Output:
```
Example
├── build
│   ├── resources
│   │   └── dog.jpg
│   └── src
│       ├── addition.py
│       └── helloworld.py
├── docs
├── License.txt
├── src
├── tools
├── test
│   ├── benchmarks
│   ├── integration
│   └── unit
└── zz
```

***
Include hidden files:
```
python autoTree.py -f Example -s true
```

Output:
```
Example                                #
├── .DS_Store                          #
├── build                              #
│   ├── .DS_Store                      #
│   ├── resources                      #
│   │   └── dog.jpg                    #
│   └── src                            #
│       ├── addition.py                #
│       └── helloworld.py              #
├── docs                               #
│   ├── .DS_Store                      #
│   └── .keep                          #
├── License.txt                        #
├── src                                #
│   └── .keep                          #
├── tools                              #
│   └── .keep                          #
├── test                               #
│   ├── .DS_Store                      #
│   ├── benchmarks                     #
│   │   └── .keep                      #
│   ├── integration                    #
│   │   └── .keep                      #
│   └── unit                           #
│       └── .keep                      #
└── zz                                 #
    └── .keep                          #

```
