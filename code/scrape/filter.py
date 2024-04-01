import os
import pandas as pd
from log import get_logger
from langdetect import detect
from tqdm import tqdm

logger = get_logger()

logger.info('filtering english chat')

csv_path = os.path.join(os.getcwd(), 'data', 'merged.csv')
df = pd.read_csv(csv_path)

with tqdm(total=df.shape[0]) as pbar:

    for index, row in df.iterrows():
        try:
            language = detect(row['message'])
        except:
            language = "error"

        if language != 'en':
            df.drop(index, inplace=True)

        pbar.update(1)


df = df.drop_duplicates()
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
filter_csv_path = os.path.join(os.getcwd(), 'data', 'filtered.csv')
logger.info(df.info())
df.to_csv(filter_csv_path, index=False)

logger.info('finished')
