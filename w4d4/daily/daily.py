import random
import psycopg2
import requests
from DB_connection import DBManager


def get_random_countries(num_countries=10):
    response = requests.get('https://restcountries.com/v3.1/all')
    if response.status_code == 200:
        countries_data = response.json()
        random_countries = random.sample(countries_data, num_countries)
        return random_countries
    else:
        return None


def insert_countries(data):
    with DBManager() as db:
        for country in data:
            name = country['name']['common']
            capital = country['capital'][0] if 'capital' in country else ''
            flag_svg = requests.get(country['flags']['svg'])
            flag_bytes = flag_svg.content
            subregion = country['subregion'] if 'subregion' in country else ''
            population = country['population'] if 'population' in country else 0

            try:
                cursor = db.connection.cursor()
                insert_query = "INSERT INTO countries (name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s);"
                data = (name, capital, flag_bytes, subregion, population)
                cursor.execute(insert_query, data)
                db.connection.commit()
            except (Exception, psycopg2.Error) as err:
                print("Error while inserting to PostgreSQL:", err)
                db.connection.rollback()


if __name__ == "__main__":
    random_countries = get_random_countries()
    if random_countries:
        insert_countries(random_countries)
    else:
        print("Failed to fetch random countries from API.")
