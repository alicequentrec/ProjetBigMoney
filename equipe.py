import pandas as pd
import feedparser as fp
import os

list_sport = [
    "https://dwh.lequipe.fr/api/edito/rss?path=/Football/", 
    "https://dwh.lequipe.fr/api/edito/rss?path=/Formule-1/", 
    "https://dwh.lequipe.fr/api/edito/rss?path=/Tennis/",
    "https://dwh.lequipe.fr/api/edito/rss?path=/Basket/Nba/"
]

class FluxRSS:
    def __init__(self, url) -> None:
        self.url = url

    def extract_rss(self):
        test = fp.parse(self.url)
        entries = test.entries
        if entries:
            df_rss = pd.DataFrame([{
                'Title': entry.title,
                'Category': entry.category,
                'Published': entry.published
            } for entry in entries])

            self.df = df_rss
            return self.df
        else:
            print("No entries found in RSS feed.")
            return None

def save_rss_to_file(rss_data, file_path):
    rss_data.to_csv(file_path, index=False)
    print(f"RSS data saved to {file_path}.")

def concatenate_csv(file1, file2, output_file):
    if os.path.exists(file1) and os.path.exists(file2):
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)
        concatenated_df = pd.concat([df1, df2], ignore_index=True)
        concatenated_df.to_csv(output_file, index=False)
        print(f"The combined data has been saved to {output_file}.")
    else:
        print("One of the files does not exist.")

if __name__ == '__main__':
    combined_df = pd.DataFrame() 
    for url in list_sport:
        equipe = FluxRSS(url)
        df = equipe.extract_rss()
        if df is not None:
            combined_df = pd.concat([combined_df, df], ignore_index=True)

    if not combined_df.empty:
        rss_file_path = 'out/rss_data.csv'
        save_rss_to_file(combined_df, rss_file_path)
    else:
        print("No RSS data to save.")

    original_csv = 'out/out.csv'
    rss_csv = 'out/rss_data.csv'
    output_csv = 'out/equipefinal.csv'

    concatenate_csv(original_csv, rss_csv, output_csv)
