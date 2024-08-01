# Problem Statement
Imagine a file in the following fixed format:\
`<url><white_space><long value>`\
e.g.\
http://api.tech.com/item/121345 9\
http://api.tech.com/item/122345 350\
http://api.tech.com/item/123345 25\
http://api.tech.com/item/124345 231\
http://api.tech.com/item/125345 111

Write a program that reads from 'stdin' the absolute path of a file expected to be in this format and outputs a list of the urls associated with the 10 largest values in the right-most column. For example, given the input data above if the question were to output the 2 largest values the output would be:
http://api.tech.com/item/122345\
http://api.tech.com/item/124345\

**_NOTE:_** Your solution should take into account extremely large files.
# Comments:
- Read the assignment carefully
- Use the programming language of your choice
- The program may use any recent stable version of the language, but
should compile / run using official binaries / runtime (such as Oracle
JDK or OpenJDK for Java)
- For any chosen language, only the standard included libraries may be
used.
- Describe how to build and run your code, optionally including some
build or make file.
- If you make some assumptions or decisions about used algorithms, please
explain them briefly.
- Think about how to verify / test this application and include a
description or code.

# Considerations
- Extremely large file usually means one that do not fit into the RAM

# Approach
The approach would be reading a file chunk by chunk, reducing each chunk to top N lines using heap DS, and then reducing reduced tops down to one.

# Usage
`make && make test && make clean`\
`python generate_data.py 10000`\
`python -m topn -p data/data10000.txt`