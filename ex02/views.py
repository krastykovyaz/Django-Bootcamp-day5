from django.shortcuts import render
import psycopg2


def populate_data(request):
    conn = 0
    resume = list()
    try:
        conn = psycopg2.connect(
            database='djangotraining',
            host='localhost',
            user='djangouser',
            password='secret',
        )
    except:
        resume = "I am unable to connect to the database."
        print(resume)

    curr = conn.cursor()
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
            VALUES
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19')""")
        conn.commit()
        resume.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        resume.append('The Phantom Menace:')
        resume.append(e)
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
            VALUES 
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum',  '2002-05-16')""")
        conn.commit()
        resume.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        resume.append('Attack of the Clones:')
        resume.append(e)
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
            VALUES
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19')""")
        conn.commit()
        resume.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        resume.append('Revenge of the Sith:')
        resume.append(e)
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
            VALUES
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum',  '1977-05-25')""")
        conn.commit()
        resume.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        resume.append('A New Hope:')
        resume.append(e)
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
            VALUES
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kutz, Rick McCallum', '1980-05-17')""")
        conn.commit()
        resume.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        resume.append('The Empire Strikes Back:')
        resume.append(e)
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
                VALUES
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25')""")
        conn.commit()
        resume.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        resume.append('Return of the Jedi:')
        resume.append(e)
    try:
        curr.execute("""INSERT INTO ex02_movies(episode_nb ,title, director, producer, release_date)
                VALUES
        (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11');""")
        conn.commit()
        conn.close()
        resume.append('Ok')
    except psycopg2.DatabaseError as e:
        print(e)
        resume.append('The Force Awakens:')
        resume.append(e)
    return render(request, 'ex02/populate.html', {'resume': resume})


def create_db(request):
    conn = 0
    try:
        conn = psycopg2.connect(
            database='djangotraining',
            host='localhost',
            user='djangouser',
            password='secret',
        )
    except:
        resume = "Fail connetion to database"
        print(resume)
    curr = conn.cursor()
    try:
        curr.execute("""CREATE TABLE IF NOT EXISTS ex02_movies (
        episode_nb serial PRIMARY KEY,
        title VARCHAR(64) UNIQUE NOT NULL,
        opening_crawl TEXT ,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL
        );
        """)
        conn.commit()
        conn.close()
        resume = 'Ok'
    except psycopg2.DatabaseError as e:
        print(e)
        resume = e

    return render(request, 'ex02/index.html', {'resume': resume})


def display_data(request):
    conn = 0
    try:
        conn = psycopg2.connect(
            database='djangotraining',
            host='localhost',
            user='djangouser',
            password='secret',
        )
    except:
        resume = "I am unable to connect to the database."
        print(resume)
    curr = conn.cursor()
    try:
        curr.execute("""SELECT * FROM ex02_movies""")
        movies = curr.fetchall()
        conn.close()
    except psycopg2.DatabaseError as e:
        movies = 0
        print(e)
    return render(request, 'ex02/display.html', {'table': movies})
