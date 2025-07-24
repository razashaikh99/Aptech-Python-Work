import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://oladoc.com/pakistan/lahore/dermatologist"
response = requests.get(url)

data = BeautifulSoup(response.text, "html.parser")

# All h2 tags (just like your code)
h2_data = data.find_all("h2")

# Lists to hold titles and links
a_title, a_href = [], []

# Loop over all h2 tags
for a in h2_data:
    # Find all <a> tags with class "doctor-name" inside h2
    a_tags = a.find_all("a", class_="doctor-name")
    for b in a_tags:
        a_title.append(b.text.strip())
        a_href.append(b.get("href"))

# Save results
anchor_data_dic = {"Title": a_title, "Href": a_href}

df = pd.DataFrame(anchor_data_dic)
df.to_csv("razashaikh.csv", index=False)
print(df)
