"""Build a real .xlsx file using only Python stdlib (zipfile + xml).

Outputs 04-storyboard.xlsx in the same directory.
"""
import csv
import os
import zipfile
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "03-storyboard.csv")
XLSX_PATH = os.path.join(HERE, "04-storyboard.xlsx")

# Read rows from generated CSV (utf-8-sig)
rows = []
with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.reader(f)
    for r in reader:
        rows.append(r)

n_rows = len(rows)
n_cols = len(rows[0]) if rows else 0

# ---- Build shared strings table (all cells as inlined strings is simpler) ----
# We'll use inline strings (t="inlineStr") to avoid building a sharedStrings.xml.
# Numeric column "时长(秒)" can also be inline; xlsx accepts numeric via t="n".

def col_letter(idx_zero):
    """0-based -> 'A','B',...,'Z','AA',..."""
    s = ""
    n = idx_zero
    while True:
        s = chr(ord("A") + (n % 26)) + s
        n = n // 26 - 1
        if n < 0:
            break
    return s

def cell_xml(col_letter_str, row_num, value, is_number=False):
    if is_number:
        return f'<c r="{col_letter_str}{row_num}" t="n"><v>{value}</v></c>'
    safe = escape(str(value))
    return (
        f'<c r="{col_letter_str}{row_num}" t="inlineStr">'
        f'<is><t xml:space="preserve">{safe}</t></is></c>'
    )

# Build sheet1.xml
sheet_rows_xml = []
for r_idx, row in enumerate(rows):
    excel_row = r_idx + 1
    cells = []
    for c_idx, val in enumerate(row):
        letter = col_letter(c_idx)
        is_num = False
        # Header is row 1 -> all strings. Data rows: col 0 (#) and col 2 (时长) numeric
        if r_idx > 0 and c_idx in (0, 2):
            try:
                fv = float(val)
                if fv.is_integer():
                    val = int(fv)
                else:
                    val = fv
                is_num = True
            except Exception:
                is_num = False
        cells.append(cell_xml(letter, excel_row, val, is_num))
    sheet_rows_xml.append(f'<row r="{excel_row}">' + "".join(cells) + "</row>")

last_col_letter = col_letter(n_cols - 1)
sheet_xml = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
    f'<dimension ref="A1:{last_col_letter}{n_rows}"/>'
    '<sheetViews><sheetView workbookViewId="0"><pane state="frozen" ySplit="1" topLeftCell="A2" activePane="bottomLeft"/></sheetView></sheetViews>'
    '<cols>'
    '<col min="1" max="1" width="6" customWidth="1"/>'
    '<col min="2" max="2" width="9" customWidth="1"/>'
    '<col min="3" max="3" width="9" customWidth="1"/>'
    '<col min="4" max="4" width="60" customWidth="1"/>'
    '<col min="5" max="5" width="50" customWidth="1"/>'
    '<col min="6" max="6" width="80" customWidth="1"/>'
    '<col min="7" max="7" width="10" customWidth="1"/>'
    '</cols>'
    '<sheetData>' + "".join(sheet_rows_xml) + '</sheetData>'
    '</worksheet>'
)

# Other required parts of the xlsx package
content_types = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
    '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
    '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
    '</Types>'
)

root_rels = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
    '</Relationships>'
)

workbook_xml = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
    '<sheets><sheet name="Storyboard" sheetId="1" r:id="rId1"/></sheets>'
    '</workbook>'
)

workbook_rels = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
    '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
    '</Relationships>'
)

styles_xml = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
    '<fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts>'
    '<fills count="1"><fill><patternFill patternType="none"/></fill></fills>'
    '<borders count="1"><border/></borders>'
    '<cellStyleXfs count="1"><xf/></cellStyleXfs>'
    '<cellXfs count="1"><xf fontId="0" fillId="0" borderId="0" xfId="0"/></cellXfs>'
    '</styleSheet>'
)

# Write the zip
with zipfile.ZipFile(XLSX_PATH, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", content_types)
    z.writestr("_rels/.rels", root_rels)
    z.writestr("xl/workbook.xml", workbook_xml)
    z.writestr("xl/_rels/workbook.xml.rels", workbook_rels)
    z.writestr("xl/styles.xml", styles_xml)
    z.writestr("xl/worksheets/sheet1.xml", sheet_xml)

print(f"Wrote {n_rows} rows ({n_cols} cols) to {XLSX_PATH}")
print(f"File size: {os.path.getsize(XLSX_PATH)} bytes")
