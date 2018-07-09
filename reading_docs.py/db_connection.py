import psycopg2

# This is a maybe... Most likely going to set up a Django project
class dbConnection:
    # Connect to PGSQL DB
    def connect():
        con = psycopg2.connect("host=localhost dbname=resumeData user=pguser password=Datad0g1")

    def create_table():
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE UserData(Id INTEGER PRIMARY KEY, \
            firstName VARCHAR(30), \
            lastName VARCHAR(50), \
            email VARCHAR(255), \
            address VARCHAR(255), \
            contactNum VARCHAR(10), \
            graduated boolean, \
            experience boolean, \
            hard_skills boolean, \
            soft_skills boolean, \
            )")
        cur.execute(
            "CREATE TABLE Skills(Id INTEGER PRIMARY KEY, \
            firstName VARCHAR(30), \
            lastName VARCHAR(50), \
            email VARCHAR(255), \
            address VARCHAR(255), \
            contactNum VARCHAR(10), \
            schoolName VARCHAR(25), \
            schoolCity VARCHAR(50), \
            schoolState VARCHAR(2), \
            graduationDate DATE, \
            exp_company_1 VARCHAR(50), \
            exp_title_1 VARCHAR(50), \
            exp_city_1 VARCHAR(50), \
            exp_state_1 VARCHAR(2), \
            exp_start_date_1 DATE, \
            exp_end_date_1 DATE, \
            exp_desc_1 VARCHAR(255), \
            hard_skills_1 VARCHAR(255), \
            soft_skills_1 VARCHAR(255), \
            tools_1 VARCHAR(50), \
            )")
        cur.execute(
            "CREATE TABLE Education(Id INTEGER PRIMARY KEY, \
            firstName VARCHAR(30), \
            lastName VARCHAR(50), \
            email VARCHAR(255), \
            address VARCHAR(255), \
            contactNum VARCHAR(10), \
            schoolName VARCHAR(25), \
            schoolCity VARCHAR(50), \
            schoolState VARCHAR(2), \
            graduationDate DATE, \
            exp_company_1 VARCHAR(50), \
            exp_title_1 VARCHAR(50), \
            exp_city_1 VARCHAR(50), \
            exp_state_1 VARCHAR(2), \
            exp_start_date_1 DATE, \
            exp_end_date_1 DATE, \
            exp_desc_1 VARCHAR(255), \
            hard_skills_1 VARCHAR(255), \
            soft_skills_1 VARCHAR(255), \
            tools_1 VARCHAR(50), \
            )")
        cur.execute(
            "CREATE TABLE Experience(Id INTEGER PRIMARY KEY, \
            firstName VARCHAR(30), \
            lastName VARCHAR(50), \
            email VARCHAR(255), \
            address VARCHAR(255), \
            contactNum VARCHAR(10), \
            schoolName VARCHAR(25), \
            schoolCity VARCHAR(50), \
            schoolState VARCHAR(2), \
            graduationDate DATE, \
            exp_company_1 VARCHAR(50), \
            exp_title_1 VARCHAR(50), \
            exp_city_1 VARCHAR(50), \
            exp_state_1 VARCHAR(2), \
            exp_start_date_1 DATE, \
            exp_end_date_1 DATE, \
            exp_desc_1 VARCHAR(255), \
            hard_skills_1 VARCHAR(255), \
            soft_skills_1 VARCHAR(255), \
            tools_1 VARCHAR(50), \
            )")
        cur.execute(
            "CREATE TABLE (Id INTEGER PRIMARY KEY, \
            firstName VARCHAR(30), \
            lastName VARCHAR(50), \
            email VARCHAR(255), \
            address VARCHAR(255), \
            contactNum VARCHAR(10), \
            schoolName VARCHAR(25), \
            schoolCity VARCHAR(50), \
            schoolState VARCHAR(2), \
            graduationDate DATE, \
            exp_company_1 VARCHAR(50), \
            exp_title_1 VARCHAR(50), \
            exp_city_1 VARCHAR(50), \
            exp_state_1 VARCHAR(2), \
            exp_start_date_1 DATE, \
            exp_end_date_1 DATE, \
            exp_desc_1 VARCHAR(255), \
            hard_skills_1 VARCHAR(255), \
            soft_skills_1 VARCHAR(255), \
            tools_1 VARCHAR(50), \
            )")
        con.commit()
