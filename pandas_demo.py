# ==========================================================
# This script shows many pandas + plotly tricks, step by step.
# Every part has a simple comment so even a child can understand it!
# ==========================================================

# First, we bring in the tools (libraries) we need to use.
import pandas as pd        # pandas = helps us work with tables (like Excel)
import numpy as np         # numpy = helps us work with numbers
import plotly.express as px            # plotly.express = easy way to make pictures/graphs
import plotly.graph_objects as go      # plotly.graph_objects = detailed way to make graphs
from plotly.subplots import make_subplots  # this helps put many graphs on one page

# This just makes the printed table look wider and neater on screen.
pd.set_option('display.width', 120)

# ----------------------------------------------------------
# STEP 1: Make our table (called a DataFrame) from scratch
# ----------------------------------------------------------
print("="*60, "1. DATA CREATE KARNA", "="*60)

# A dictionary is like a box with labeled drawers.
# Each drawer (key) holds a list of values (one column of our table).
data = {
    "ID": [1,2,3,4,5],                                                      # a number for each person
    "Name": ["Rohit Sharma","Priya Verma","Aman Gupta","Sneha Singh","Vikas Yadav"],  # names
    "City": ["Delhi","Mumbai","Jaipur","Lucknow","Pune"],                   # which city they live in
    "Age": [28,24,31,26,29],                                                # how old they are
    "Mobile": ["9876543210","9123456780","9988776655","9871234560","9765432180"]  # phone numbers
}
df = pd.DataFrame(data)   # turn our dictionary into a real table (DataFrame)
print(df)                 # show the table on screen

# ----------------------------------------------------------
# STEP 2: Look at (inspect) the table - like peeking inside a box
# ----------------------------------------------------------
print("\n"+"="*60, "2. INSPECT KARNA", "="*60)
print("\n-- head(3) --\n", df.head(3))     # show only the FIRST 3 rows
print("\n-- tail(2) --\n", df.tail(2))     # show only the LAST 2 rows
print("\n-- shape --\n", df.shape)         # tells us (rows, columns) count
print("\n-- info() --")
df.info()                                   # gives a quick summary (types, empty cells, etc.)
print("\n-- describe() --\n", df.describe())  # gives stats like average, min, max for numbers
print("\n-- dtypes --\n", df.dtypes)        # shows what TYPE of data is in each column

# ----------------------------------------------------------
# STEP 3: Pick out specific parts of the table (select)
# ----------------------------------------------------------
print("\n"+"="*60, "3. SELECT KARNA", "="*60)
print("\n-- df['Name'] --\n", df['Name'])              # get only the Name column
print("\n-- df[['Name','City']] --\n", df[['Name','City']])  # get 2 columns together
print("\n-- df.loc[0] --\n", df.loc[0])                 # get row number 0 (by its label)
print("\n-- df.iloc[1:3] --\n", df.iloc[1:3])            # get rows 1 and 2 (by position)
print("\n-- df.at[0,'Name'] --\n", df.at[0,'Name'])      # get ONE single value fast

# ----------------------------------------------------------
# STEP 4: Filtering - only keep rows that match a rule
# ----------------------------------------------------------
print("\n"+"="*60, "4. FILTERING", "="*60)
print("\n-- Age > 26 --\n", df[df['Age']>26])   # keep only people older than 26
print("\n-- City isin Delhi/Pune --\n", df[df['City'].isin(['Delhi','Pune'])])  # only Delhi or Pune people
print("\n-- query --\n", df.query("Age > 25 and City != 'Pune'"))  # write the rule like a sentence

# ----------------------------------------------------------
# STEP 5: Add brand new columns to our table
# ----------------------------------------------------------
print("\n"+"="*60, "5. NAYA COLUMN ADD", "="*60)
df['Age_after_5yr'] = df['Age'] + 5             # new column = Age + 5 (future age)
print(df)
df['City_Upper'] = df['City'].apply(lambda x: x.upper())  # new column = City name in CAPITAL letters
print(df[['Name','City_Upper']])

# ----------------------------------------------------------
# STEP 6: Rename a column (just give it a new name tag)
# ----------------------------------------------------------
print("\n"+"="*60, "6. RENAME", "="*60)
df_renamed = df.rename(columns={'Mobile':'Phone_Number'})  # Mobile column is now called Phone_Number
print(df_renamed.columns.tolist())

# ----------------------------------------------------------
# STEP 7: Drop (remove) columns or rows we don't want
# ----------------------------------------------------------
print("\n"+"="*60, "7. DROP", "="*60)
df_drop_col = df.drop('Age_after_5yr', axis=1)  # axis=1 means "remove a column"
print(df_drop_col.columns.tolist())
df_drop_row = df.drop(0, axis=0)                # axis=0 means "remove a row"
print(df_drop_row)

# ----------------------------------------------------------
# STEP 8: Handle missing data (empty/blank cells)
# ----------------------------------------------------------
print("\n"+"="*60, "8. MISSING DATA (demo ke liye ek NaN daal rahe)", "="*60)
df_missing = df.copy()                 # make a safe copy so we don't break the real table
df_missing.loc[2,'Age'] = np.nan       # make one Age value empty (NaN = "Not a Number" = blank)
print(df_missing)
print("\n-- isnull().sum() --\n", df_missing.isnull().sum())  # count how many blanks in each column
print("\n-- fillna(mean) --\n", df_missing['Age'].fillna(df_missing['Age'].mean()))  # fill blank with the average

# ----------------------------------------------------------
# STEP 9: Sorting - put rows in order (smallest to biggest, etc.)
# ----------------------------------------------------------
print("\n"+"="*60, "9. SORTING", "="*60)
print("\n-- sort by Age --\n", df.sort_values('Age'))                      # youngest to oldest
print("\n-- sort by Age desc --\n", df.sort_values('Age', ascending=False))  # oldest to youngest

# ----------------------------------------------------------
# STEP 10: Group rows together and find averages (like grouping toys by color)
# ----------------------------------------------------------
print("\n"+"="*60, "10. GROUPBY", "="*60)
df_group = df.copy()
df_group['Region'] = ['North','West','North','North','West']   # give each person a "Region" group
print(df_group.groupby('Region')['Age'].mean())     # average age in each region
print("\n-- agg --\n", df_group.groupby('Region').agg({'Age':['mean','max'],'ID':'count'}))  # many stats at once

# ----------------------------------------------------------
# STEP 11: Merge and Concat - join two tables together
# ----------------------------------------------------------
print("\n"+"="*60, "11. MERGE / CONCAT", "="*60)
extra = pd.DataFrame({'ID':[1,2,3,4,5],'Salary':[50000,60000,45000,55000,70000]})  # a second small table
merged = pd.merge(df, extra, on='ID')     # join both tables using the matching "ID" column
print(merged[['ID','Name','Salary']])
df2 = pd.DataFrame({"ID":[6],"Name":["Neha Kapoor"],"City":["Chennai"],"Age":[27],"Mobile":["9000011122"]})
concatenated = pd.concat([df[['ID','Name','City','Age','Mobile']], df2], ignore_index=True)  # stack tables on top of each other
print("\n-- concat --\n", concatenated)

# ----------------------------------------------------------
# STEP 12: String operations - working with text/words
# ----------------------------------------------------------
print("\n"+"="*60, "12. STRING OPERATIONS", "="*60)
print(df['Name'].str.lower())                 # make all names lowercase
print(df['Name'].str.contains('Sharma'))      # check if "Sharma" is inside the name (True/False)
print(df['Name'].str.split(' '))              # split name into first name and last name
print(df['Name'].str.len())                   # count how many letters are in each name

# ----------------------------------------------------------
# STEP 13: Date/Time operations - working with dates
# ----------------------------------------------------------
print("\n"+"="*60, "13. DATE/TIME (demo ke liye join date add)", "="*60)
df_date = df.copy()
df_date['Join_Date'] = pd.to_datetime(['2021-05-10','2020-03-15','2022-07-01','2019-11-20','2023-01-05'])  # add real dates
print(df_date[['Name','Join_Date']])
print(df_date['Join_Date'].dt.year)           # pull out just the YEAR from each date

# ----------------------------------------------------------
# STEP 14: Apply and Map - run our own small rule on each value
# ----------------------------------------------------------
print("\n"+"="*60, "14. APPLY / MAP", "="*60)
print(df['Age'].apply(lambda x: 'Young' if x<28 else 'Senior'))  # label each person Young or Senior
print(df['City'].map({'Delhi':'DL','Mumbai':'MH','Jaipur':'RJ','Lucknow':'UP','Pune':'MH'}))  # change city name to short code

# ----------------------------------------------------------
# STEP 15: Statistics - simple math facts about our numbers
# ----------------------------------------------------------
print("\n"+"="*60, "15. STATISTICS", "="*60)
print("Sum of Age:", df['Age'].sum())              # add up all ages
print("Mean of Age:", df['Age'].mean())             # average age
print("Median:", df['Age'].median())                # middle value when sorted
print("Std:", df['Age'].std())                      # how spread out the ages are
print("Min/Max:", df['Age'].min(), df['Age'].max()) # youngest and oldest age
print("Value counts City:\n", df['City'].value_counts())  # how many times each city appears
print("Unique City:", df['City'].unique())          # list of different cities (no repeats)
print("Nunique City:", df['City'].nunique())        # how many different cities there are

# ----------------------------------------------------------
# STEP 16: Reshaping - flip the table sideways
# ----------------------------------------------------------
print("\n"+"="*60, "16. RESHAPING", "="*60)
print(df.set_index('Name').T)   # .T flips rows and columns, like turning a table on its side

# ----------------------------------------------------------
# STEP 17: Type conversion - change what "type" a column is
# ----------------------------------------------------------
print("\n"+"="*60, "17. TYPE CONVERSION", "="*60)
print(df['Age'].astype(str).dtype)      # change Age numbers into text
print(pd.to_numeric(df['Age']).dtype)   # make sure Age stays as a number

# ----------------------------------------------------------
# STEP 18: Index operations - change which column is the "row label"
# ----------------------------------------------------------
print("\n"+"="*60, "18. INDEX OPERATIONS", "="*60)
df_idx = df.set_index('ID')             # use ID column as the row label instead of 0,1,2...
print(df_idx)
print("\n-- reset_index --\n", df_idx.reset_index())  # put it back to normal numbering

# ----------------------------------------------------------
# STEP 19: Export - save our table into real files
# ----------------------------------------------------------
print("\n"+"="*60, "19. EXPORT (files save honge)", "="*60)
df.to_csv("/mnt/user-data/outputs/pandas_output.csv", index=False)     # save as a CSV file
df.to_excel("/mnt/user-data/outputs/pandas_output.xlsx", index=False)  # save as an Excel file
print("CSV aur Excel save ho gaye")

# ----------------------------------------------------------
# STEP 20: Small extra (misc) tricks
# ----------------------------------------------------------
print("\n"+"="*60, "20. MISC", "="*60)
print("Duplicated rows:\n", df.duplicated())          # check if any row repeats
print("Copy check:", df.copy().equals(df))            # check if a copy is exactly the same
print("nlargest by Age:\n", df.nlargest(2,'Age'))      # top 2 oldest people
print("nsmallest by Age:\n", df.nsmallest(2,'Age'))    # top 2 youngest people
print("Round demo:", pd.Series([1.234,5.678]).round(1).tolist())  # round numbers to 1 decimal

# ==========================================================
# STEP 21: GRAPHS! Now we draw pretty pictures using Plotly
# ==========================================================
print("\n"+"="*60, "21. GRAPHS (PLOTLY)", "="*60)

# --- Chart 1: Bar chart - shows Age as tall bars for each Name ---
fig_bar = px.bar(
    df, x="Name", y="Age", color="City", text="Age",
    title="Age by Name (City-wise Color)"
)
fig_bar.update_traces(textposition="outside")   # put the number label above each bar
fig_bar.update_layout(template="plotly_white")  # use a clean white background

# --- Chart 2: Pie chart - shows Age like slices of a pizza, one slice per City ---
fig_pie = px.pie(
    df, names="City", values="Age",
    title="Age Share by City"
)

# --- Chart 3: Scatter plot - shows dots for each person (ID vs Age) ---
fig_scatter = px.scatter(
    df, x="ID", y="Age", size="Age", color="Name",
    title="ID vs Age (Scatter)", text="Name"
)
fig_scatter.update_traces(textposition="top center")  # put the name above each dot
fig_scatter.update_layout(template="plotly_white")

# --- Chart 4: Line chart - connects dots with a line to show a trend ---
fig_line = px.line(
    df, x="Name", y="Age", markers=True,
    title="Age Trend across Records"
)
fig_line.update_layout(template="plotly_white")

# --- Dashboard: put all 4 charts together on ONE page, like a poster ---
dashboard = make_subplots(
    rows=2, cols=2,   # 2 rows and 2 columns = 4 boxes total
    subplot_titles=("Age by Name", "Age Share by City", "ID vs Age", "Age Trend"),
    specs=[[{"type": "bar"}, {"type": "domain"}],
           [{"type": "scatter"}, {"type": "scatter"}]]
)

# Put each small chart into its own box on the dashboard
dashboard.add_trace(go.Bar(x=df["Name"], y=df["Age"], marker_color="steelblue", name="Age"), row=1, col=1)
dashboard.add_trace(go.Pie(labels=df["City"], values=df["Age"], name="City"), row=1, col=2)
dashboard.add_trace(go.Scatter(x=df["ID"], y=df["Age"], mode="markers+text",
                                text=df["Name"], textposition="top center",
                                marker=dict(size=12, color="orange"), name="ID vs Age"), row=2, col=1)
dashboard.add_trace(go.Scatter(x=df["Name"], y=df["Age"], mode="lines+markers",
                                line=dict(color="green"), name="Age Trend"), row=2, col=2)

dashboard.update_layout(height=800, width=1000, title_text="Pandas + Plotly Dashboard", template="plotly_white", showlegend=False)

# ----------------------------------------------------------
# Save ALL the charts into one HTML file, so we can open it in a browser
# ----------------------------------------------------------
# NOTE: Plotly's normal "cdn" option tries to load its helper code from
# cdn.plot.ly, but that address is blocked on some pages.
# So instead, we point to a SAFE, ALLOWED address (jsdelivr) that works fine.
plotly_js_src = "https://cdn.jsdelivr.net/npm/plotly.js-dist-min@2/plotly.min.js"

with open("/mnt/user-data/outputs/pandas_plotly_charts.html", "w", encoding="utf-8") as f:
    f.write(f"<script src='{plotly_js_src}'></script>")   # load the plotly drawing tool first
    f.write("<h1 style='font-family:Arial'>Pandas Data - Plotly Charts</h1>")  # a big title on the page
    f.write(fig_bar.to_html(full_html=False, include_plotlyjs=False))       # add chart 1
    f.write(fig_pie.to_html(full_html=False, include_plotlyjs=False))       # add chart 2
    f.write(fig_scatter.to_html(full_html=False, include_plotlyjs=False))   # add chart 3
    f.write(fig_line.to_html(full_html=False, include_plotlyjs=False))      # add chart 4
    f.write(dashboard.to_html(full_html=False, include_plotlyjs=False))     # add the combined dashboard

print("Plotly charts HTML file save ho gayi: pandas_plotly_charts.html")
