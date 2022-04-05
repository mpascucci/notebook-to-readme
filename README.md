# notebook-to-readme
Easily convert jupyter notebooks into markdown README (and open notebooks previews on mouse click).

## Install

1. clone this repository
2. cd into the cloned folder
3. Install the module from the command line with `pip install .` 


## Command line tools
This module installs two command line tools:

- `nb2md` that converts a jupyter notebook into markdown, with the possibility of hiding cells containing certain tags

- `notebook_preview` which converts the notebook into HTML and opens it with the default browser


## nb2md : convert notebook to README
The following is is the output of `nb2md -h` and explains how to use the tool:

```
usage: nb2md [-h] [-o OUTPUT_PATH] [-i OUTPUT_IMAGE_FOLDER] [-c] [-e] [-k KEYWORD [KEYWORD ...]] [-a] input_path

Convert a notebook into a markdown file. Hide cells containing the autorelaod magic command or the comment #HIDE_IN_MARKDOWN.

positional arguments:
  input_path            The path of the Juptyter notebook to be converted

options:
  -h, --help            show this help message and exit
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        The path of the output markdown files, specified as '[output_path]/filename.md'. Default ./NOTEBOOK.md
  -i OUTPUT_IMAGE_FOLDER, --output_image_folder OUTPUT_IMAGE_FOLDER
                        The path to the folder that will contain the images linked in the markdown. This path will be added to [output_path].
                        Default [output_path]/NOTEBOOK_files/
  -c, --no_code_cells   Remove all code cells.
  -e, --keep_empty_cells
                        Keep empty code cells.
  -k KEYWORD [KEYWORD ...], --keyword KEYWORD [KEYWORD ...]
                        Remove the cells containing the specified keywords (use quotes to specify the keywords)
  -a, --keep_auto_hidden
                        Keep the automatically hidden cells. If this flag is not active, cells containing the autorelaod magic command or #README_HIDE_CELL comment will be hidden
```

## notebook_preview
Use this command line to open a preview of your notebook (eg `notebook_preview Untitled1.pynb`).

This command line tool can be associated with the `.ipynb` extension to open a preview of the notebook when double-clicking its icon in a file browser.

instructions for Linux:
- find the location of notebook_preview by executing `which notebook_preview` in a terminal
- right click a notebook file and choose "open with>Other application"
- paste the location of notebook_preview
- check "Remember application..."
- click 'OK'

