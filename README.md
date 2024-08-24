<!-- TOC --><a name="filesorter"></a>
# FileSorter

A Python script to sort all files in a given Direcorty into folders based on the file extension  
  

### Table Of Contents
<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->
- [FileSorter](#filesorter)
   * [Info](#info)
   * [Constraints](#constraints)
   * [How to use](#how-to-use)
   * [Error handling](#error-handling)
<!-- TOC end -->

<!-- TOC --><a name="info"></a>
## Info
<!--
to have a self-incrementing Version Number you can use GitHub workflows
-->
+ **Version:** `0.9.0`
+ **language:** `Python`
+ **License:** `MIT`

<!-- TOC --><a name="constraints"></a>
## Constraints
+ File only works on the directory in which it is currently in
+ Not good error handling

<!---
after the 1. there are two spaces to tell the markdown interpreter to start a new line as an alternative you could also use the HTML tag "<br>"
also don't forget to change the git repo link to your own and do not forget the required format is: name/repo/branch.git
-->
<!-- TOC --><a name="how-to-use"></a>
## How to use
1. Clone the repository or download the FileSorter.py file  
  run `git clone https://github.com/Yan1921/FileSorter.git`
2. Put the file in the directory you want to sort
3. Run the FileSorter.py
4. FileSorter.py creates a folder with subfolders which are named after the present file extensions and moves the files in their respective subfolders
5. Profit

<!-- TOC --><a name="error-handling"></a>
## Error handling
### As already stated under [Constraints](#constraints) there is no proper error handling implemented yet, once it is it will be documented here
<!--
Maybe error handling is a suboptimal name, it should also be documented how the code behaves in edge cases, etc.
-->
