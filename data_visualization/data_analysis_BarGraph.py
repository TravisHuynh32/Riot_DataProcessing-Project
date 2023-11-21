import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Create By: Travis Huynh
# Data Analysis, Bar Graph of Champion Data Mastery


def connect_to_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="TravisPC",
            user="DuhBoss32",
            password="9379544trav",
            database="testing"
        )
        print("MySQL Database Connected!")
    except mysql.connector.Error as err:
        print("Error!: '{err}'")
    return connection

def fetch_champion_data():
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Mastery7Champions")
            data = cursor.fetchall()
            columns = [i[0] for i in cursor.description]
            df = pd.DataFrame(data, columns=columns)
            cursor.close()
            connection.close()
            return df
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
        return None

def analyze_champion_data(df):
    if df is not None:
        champion_mastery = df.groupby('champion_name')['champion_points'].max().sort_values(ascending=False)

        plt.figure(figsize=(12, 8))
        colors = plt.cm.viridis_r((champion_mastery.values - min(champion_mastery)) / (max(champion_mastery) - min(champion_mastery)))
        champion_mastery.plot(kind='bar', color=colors)
        plt.title('Champions by Mastery Points', fontsize=16)
        plt.xlabel('Champion', fontsize=14)
        plt.ylabel('Mastery Points', fontsize=14)
        plt.xticks(rotation=90, fontsize=10)
        plt.yticks(fontsize=10)
        plt.tick_params(axis='x', which='major', labelsize=8) 
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

        print("\nSummary Statistics:")
        print(champion_mastery.describe())
    else:
        print("No data available.")

if __name__ == "__main__":
    champion_data = fetch_champion_data()
    analyze_champion_data(champion_data)