# League of Legends Data Processing Program

![League of Legends Image](images/gragas.jpg)

## Overview

The League of Legends Data Processing Program is a Python application designed to gather, process, and store player statistics and game-related information from Riot's API into a MySQL database. The program utilizes various libraries such as Cassiopeia, MySQL Connector, Pandas, and interacts with Riot's API to retrieve League of Legends data.

## Details

### Components

1. **cassiopeia**: Utilized for interfacing with Riot's API to retrieve summoner information, champion mastery data, and other game-related details.
2. **MySQL Connector**: Used to establish a connection with a MySQL database to store and manage player statistics.
3. **Pandas**: Employed for data manipulation, especially for transforming fetched data into dataframes.

### File Structure

- `src/apikey.txt`: Contains the Riot API key needed for accessing the Riot API.
- `src/config.json`: JSON file storing MySQL connection details (`host`, `user`, `password`, `database`).
- `base.py`: Python script serving as the main program file.

### Program Functionality

1. **Fetching Riot Data**:
   - Utilizes Cassiopeia to retrieve summoner details and champion masteries from Riot's API.
   - Interacts with the API to gather League of Legends information based on a specific summoner name and region.

2. **Database Interaction**:
   - Establishes a connection to a MySQL database using provided credentials.
   - Creates a table (`Mastery7Champions`) if it doesn't exist to store champion mastery data.
   - Inserts retrieved summoner and champion mastery data into the MySQL database table.

3. **Data Retrieval**:
   - Fetches data from the `Mastery7Champions` table in the MySQL database.
   - Transforms the fetched data into a Pandas DataFrame.

4. **IN PROGRESS** 

## Usage

The main entry point of the program is the `base.py` file.
Execute the program with the necessary summoner name and region parameters to retrieve and store League of Legends data into the MySQL database.
Once executed, the program displays the fetched data in the form of a Pandas DataFrame.

### Example Command:
```bash
python base.py
```

Credits:

Author: Travis Huynh
Creation Date: November 15, 2023
