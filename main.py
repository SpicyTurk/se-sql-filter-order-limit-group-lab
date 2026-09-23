import pandas as pd 
import sqlite3

conn1 = sqlite3.connect('planets.db')

planets = pd.read_sql("""SELECT * FROM planets; """, conn1)

#print(planets)

df_no_moons = pd.read_sql("""
    SELECT name
    FROM planets
    WHERE num_of_moons = 0
""", conn1)

#print(df_no_moons)

df_name_seven = pd.read_sql("""
SELECT name, mass 
    FROM planets
    WHERE name LIKE "_______";
""", conn1)

#print(df_name_seven)

df_mass = pd.read_sql("""
SELECT name, mass
    FROM planets
    WHERE mass <= 1.00
""", conn1)

#print(df_mass)

df_mass_moon = pd.read_sql("""
SELECT *
    FROM planets
    WHERE num_of_moons >= 1 AND mass < 1
""", conn1)

#print(df_mass_moon)

df_blue = pd.read_sql("""
SELECT name, color
    FROM planets
    WHERE color LIKE "%blue"
""", conn1)

#print(df_blue)

conn2 = sqlite3.connect('dogs.db')

# Select all
dogs = pd.read_sql("SELECT * FROM dogs;", conn2)

#print(dogs)

df_hungry = pd.read_sql("""
SELECT name, age, breed
    FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC
""", conn2)

#print(df_hungry)

df_hungry_ages = pd.read_sql("""
SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1 AND age BETWEEN 2 AND 7
    ORDER BY name ASC
""", conn2)

#print(df_hungry_ages)

df_4_oldest = pd.read_sql("""
SELECT name, age, breed
FROM (
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC
    LIMIT 4
)
ORDER BY breed ASC;
""", conn2)

#print(df_4_oldest)

conn3 = sqlite3.connect('babe_ruth.db')

# Select all
babe_ruth = pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)

#print(babe_ruth)

df_ruth_years = pd.read_sql("""
SELECT (MAX(year) - MIN(year) + 1) AS total_years
FROM babe_ruth_stats;
""", conn3)

#print(df_ruth_years)

df_hr_total = pd.read_sql("""
SELECT SUM(HR) as total_hrs
FROM babe_ruth_stats;
""", conn3)

#print(df_hr_total)

df_teams_years = pd.read_sql("""
SELECT team, COUNT(*) AS number_years
FROM babe_ruth_stats
GROUP BY team;
""", conn3)

#print(df_teams_years)

df_at_bats = pd.read_sql("""
SELECT team, AVG(at_bats) AS average_at_bats
FROM babe_ruth_stats
GROUP BY team
HAVING AVG(at_bats) > 200;
""", conn3)

#print(df_at_bats)

conn1.close()
conn2.close()
conn3.close()