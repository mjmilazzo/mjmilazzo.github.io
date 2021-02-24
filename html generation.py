import os
import markdown

"""
All text files in working directory are
markdown files. This script converts them
to html files for the GitHub personal page.

Use this template to generate markdown text:
https://dillinger.io/
"""

wd = os.getcwd()

mdfiles = [f for f in os.listdir(wd) if os.path.isfile(os.path.join(wd, f))]
mdfiles = [f for f in mdfiles if f.endswith('.txt')]

"""
All text files within working directory are markdown files,
with the naming convention "....._md.txt", where prefix
is the name of the desired html file output.
"""

for f in mdfiles:
    fname = f.split("_md.txt")[0]
    
    with open(f, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(text)

    with open("{}.html".format(fname), "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(html)