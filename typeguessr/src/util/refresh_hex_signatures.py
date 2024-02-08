import pandas as pd

def main():
    target_hex_columns = {
        'Hex signature',
        'ISO 8859-1',
        'Offset',
        'Extension',
        'Description',
    }

    hex_df = pd.read_html('https://en.wikipedia.org/wiki/List_of_file_signatures')[1]

    assert set(hex_df.columns).intersection(target_hex_columns) == target_hex_columns, f"Columns mismatch: {target_hex_columns - set(hex_df.columns)}"

    hex_df = hex_df.loc[:, ~hex_df.columns.str.contains('^Unnamed')]

    target_mime_columns = {
        'MIME',
        'File types',
        'AKA',
    }

    mime_df = pd.read_html('https://mimetype.io/all-types')[0]

    assert set(mime_df.columns).intersection(target_mime_columns) == target_mime_columns, f"Columns mismatch: {target_mime_columns - set(mime_df.columns)}"

    mime_df = mime_df.loc[:, ~mime_df.columns.str.contains('^Unnamed')]

if __name__ == "__main__":
    main()
