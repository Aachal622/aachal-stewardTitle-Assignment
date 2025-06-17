# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:56:11 2025

@author: aachalkala
"""

import pandas as pd

def load_excel_data(file_path):
    xl = pd.ExcelFile(file_path)
    content = ""
    for sheet in xl.sheet_names:
        df = xl.parse(sheet)
        content += df.astype(str).to_string(index=False)
        content += "\n"
    return content


