# import numpy as np
# import pandas as pd

# x = pd.DataFrame({
#     'a': np.arange(10),
#     'b': range(10)
# })

# print(x)
# print("hello")

import markdown

with open("main page markdown.txt", "r", encoding="utf-8") as input_file:
    text = input_file.read()

html = markdown.markdown(text)

# txt = """
# #This is a markdown file
# """
# html = markdown.markdown(txt)
# print(html)

with open("index.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(html)