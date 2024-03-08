import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

def fetch_top_20_champion_data():
    try:
        connection = None
        with open("private/config.json", "r") as file:
            config = json.load(file)
            mysql_config = config['mysql']
            connection = mysql.connector.connect(
                host=mysql_config['host'],
                user=mysql_config['user'],
                password=mysql_config['password'],
                database=mysql_config['database']
            )
            print("MySQL Database Connected!")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Mastery7Champions ORDER BY champion_points DESC LIMIT 20")
        data = cursor.fetchall()
        columns = [i[0] for i in cursor.description]
        df = pd.DataFrame(data, columns=columns)

        cursor.close()
        connection.close()

        return df

    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
        return None

def plot_percentage_mastery_points_top_20(df):
    if df is not None:
        total_points = df['champion_points'].sum()
        df['percentage'] = (df['champion_points'] / total_points) * 100

        plt.figure(figsize=(8, 8))
        plt.pie(df['percentage'], labels=df['champion_name'], autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Percentage of Mastery Points for Top 20 Champions')
        plt.show()

    else:
        print("No data available.")

if __name__ == "__main__":
    top_20_champion_data = fetch_top_20_champion_data()
    plot_percentage_mastery_points_top_20(top_20_champion_data)
