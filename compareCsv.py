import pytest
import pandas as pd
from tabulate import tabulate

def test_compare_csv_files():
    original_csv_path = 'SuperHero.csv'
    updated_csv_path = 'SuperHero_updated.csv'

    df1 = pd.read_csv(original_csv_path)
    df2 = pd.read_csv(updated_csv_path)

    assert df1.equals(df2), "CSV файлы различаются"

    diff = pd.concat([df1, df2]).drop_duplicates(keep=False)
    if not diff.empty:
        print("\nРазличия между CSV файлами:")
        table = tabulate(diff, headers='keys', tablefmt='grid', showindex=False)
        print(table)

if __name__ == '__main__':
    pytest.main()