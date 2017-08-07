# Day One Classic converter to Ulysses Markdown

This is a simple Python script that converts Day One Classic files (.doentry files) into Markdown suitable for [Ulysses](https://www.ulyssesapp.com/) (.md files). It extracts the Markdown from the Day One plist file, deals with how each program treats line breaks differently, and it sets the creation time of the resulting Ulysses .md file to matche the creation time of the Day One Classic entry.

It also names the new markdown files based on the date of the original Day One entry.

Once you bring your Day One entires into Ulysses, you can sort them by creation time there, as needed.

# Usage

Put your Day One entries (available via Show Package Contents of your Day One Journal file) into the `entries` folder. Run the script, and your Markdown files will show up in the `md` folder. You can now bring these into Ulysses.
