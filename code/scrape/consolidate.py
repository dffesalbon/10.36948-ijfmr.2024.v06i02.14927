import os
import pandas as pd
from log import get_logger

logger = get_logger()

folder_path = os.path.join(os.getcwd(), 'data')
all_files = os.listdir(folder_path)
csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))
file_list = [os.path.join(folder_path, f) for f in csv_files]

csv_list = []
for file in sorted(file_list):
    csv_list.append(pd.read_csv(file, header=0))

concat = pd.concat(csv_list, ignore_index=True)
unique = concat.drop_duplicates()
unique = unique.loc[:, ~unique.columns.str.contains('^Unnamed')]
logger.info(unique.info())
texts = unique[~unique['message'].astype(str).str.isnumeric()]
texts.to_csv(os.path.join(os.getcwd(), 'data', 'merged.csv'), index=False)

logger.info(f'csv files consolidated')
