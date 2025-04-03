import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
file_path = "imdb_top_1000.csv"
df = pd.read_csv(file_path)

#display first few rows
print(df.head())

print(df.columns)

#Basic Data Cleaning
df.dropna(inplace = True)                   #remove rows or columns containing missing values (NaN, None) from a DataFrame
df["Year"] = df["release_year"].astype(int)            #Extract year


#Data Overview
print("Dataset Info : ")
df.info()
print("\n Basic Statistics")
print(df.describe())

#Top rated movies per decade
df["Decade"] = (df["Year"]//10) * 10
top_movies_per_decade = df.loc[df.groupby("Decade")["rating"].idxmax()]

#most popular genre
df["Genre"] = df["genre"].str.split(',')
genre_exploded = df.explode("genre")
genre_count = genre_exploded['genre'].value_counts().head(10)

#visualisations
plt.figure(figsize=(10,5))
sns.barplot(data = top_movies_per_decade, x = "Decade", y = "rating", hue = "Decade", palette = "viridis", legend = False)
plt.title("Top Rated Movies Per Decade")
plt.xlabel("Decade")
plt.ylabel("IMDB Rating")
plt.show()

plt.figure(figsize = (10,5))
sns.barplot(x = genre_count.index, y = genre_count.values, hue = genre_count.index, palette = "coolwarm", legend = False)
plt.title("Top 10 Most Popular Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation = 45)
plt.show()

plt.figure(figsize = (8,5))
sns.histplot(df["rating"], bins = 20, kde = True, color = "purple")
plt.title("Distribution of IMDB Ratings")
plt.xlabel("IMDB Rating")
plt.ylabel("Count")
plt.show()

print("Analysis Complete!")