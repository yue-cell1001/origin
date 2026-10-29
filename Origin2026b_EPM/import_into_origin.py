"""Run using Origin 2026b's embedded Python (not a standalone Linux interpreter).
Imports editable worksheets only; it does not reconstruct graph pages.
Set FIGURES to a subset to inspect one reference figure at a time.
"""
from pathlib import Path
import json
import pandas as pd
import originpro as op
ROOT = Path(__file__).resolve().parent
FIGURES = list(range(2, 12))
for number in FIGURES:
    folder = ROOT / f'Fig{number:02d}'
    book = op.new_book('w', lname=f'Fig{number:02d} reproduction data')
    for i, path in enumerate(sorted(folder.glob('*.csv'))):
        sheet = book[0] if i == 0 else book.add_sheet()
        sheet.name = f'Data{i+1:03d}'
        sheet.from_df(pd.read_csv(path, encoding='utf-8-sig'))
        sheet.set_label(0, path.name, 'C')
    print(f'Imported Fig{number:02d}: {len(list(folder.glob("*.csv")))} worksheets')
print('Data import finished. Graph pages still need to be constructed and checked against reference PNGs. Save the project with File > Save Project As.')
