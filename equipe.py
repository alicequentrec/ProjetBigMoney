import pandas as pd
import numpy as nm
import feedparser as fp

list_sport = ["https://dwh.lequipe.fr/api/edito/rss?path=/Football/", 
    "https://dwh.lequipe.fr/api/edito/rss?path=/Formule-1/" , 
    "https://dwh.lequipe.fr/api/edito/rss?path=/Tennis/",
    "https://dwh.lequipe.fr/api/edito/rss?path=/Basket/Nba/"]

class FluxRSS :
    def __init__(self, url) -> None:
        self.url = url

    def extract_rss (self):
        test = fp.parse(self.url)
        entries = test.entries
        if entries:
            df_rss = pd.DataFrame([{
                'Title': entry.title,
                'Description': entry.description,
                'Category': entry.category,
                'Published': entry.published
            } for entry in entries])

            self.df = df_rss
            return self.df
        else:
            print("No entries found in RSS feed.")
            return None

if __name__ == '__main__':
    combined_df = pd.DataFrame()  # Initialize an empty DataFrame to combine all RSS entries
    for url in list_sport:
        equipe = FluxRSS(url)
        df = equipe.extract_rss()
        if df is not None:
            combined_df = pd.concat([combined_df, df], ignore_index=True)

    if not combined_df.empty:
        combined_df.to_csv('out_equipe.csv', index=False)  # Save the combined DataFrame to a CSV file
        print("RSS feed data saved to 'out.csv'.")
    else:
        print("No data to save.")
    