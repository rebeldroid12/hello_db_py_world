import os
import datetime as dt
import yaml

# postgres db
import psycopg2
from psycopg2.extras import RealDictCursor


def get_today_date():
    """
    returns today's date
    :return: today's date
    """
    return dt.date.today()


def convert_to_bool(bool_input):
    """
    Grabs bool_input and gives back 0 or 1
    :param bool_input: yes or no
    :return: True or False
    """

    bool_dict = {
        'yes': True,
        'no': False
    }
    bool_output = bool_dict[bool_input]

    return bool_output


def convert_to_date(date_input):
    """
    Grabs date that is in yyyymmdd format (no slashes/dashes) and converts it to a python date
    :param date_input: string in yyyymmdd format
    :return: python date
    """
    yyyy = int(date_input[0:4])
    mm = int(date_input[4:6])
    dd = int(date_input[6:8])
    date_output = dt.date(yyyy,mm,dd)

    return date_output


def log_operation(operation):
    """
    Give operation/message and get the timestamp of operation/message
    :param operation: message you want to log
    :return: timestamp of the operation
    """
    return '{} - {}'.format(dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d %H:%M:%S"), operation)


def configs_yml_to_dict(filename):
    """
    Give filename (configs.yml) and it will return a config yaml file in a dictionary format
    :param filename: configs.yml
    :return: Returns dictionary format of config.yml
    """

    # open yaml file and grab contents
    with open(filename, 'r') as f:
        configs = yaml.load(f)

    return configs


def connect_to_database(username=None, host=None, db_name=None, password=None):
    """
    With given credentials (username, host, db, password) connect to db -- RealDictCursor
    :param username:
    :param host:
    :param db_name:
    :param password:
    :return: returns connection that allows for dictionary data retrieval
    """
    try:
        return psycopg2.connect(database=db_name, user=username, password=password, host=host, cursor_factory=RealDictCursor)

    except Exception as e:
        # print(e)
        return 'Could not connect'


def disconnect_from_database(connection):
    """
    Give connection and function will close database connection
    :param connection: connection closed
    """
    conn = connection
    conn.close()
    return 'closed'


def run_sql_query(connection, query, dict_param):
    """
    Give connection and query to run, returns results (list of dictionaries) from the query
    :param connection: connection to db
    :param query: sql query
    :param dict_param: parameters but in dict form
    :return: results from query
    """

    # establish cursor
    cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    try:
        # try running query
        cur.execute(query, dict_param)
        results = cur.fetchall()

    except Exception as e:
        # print(e)
        results = str(e)

    # commit sql execution
    connection.commit()

    # close the cursor and close the connection
    cur.close()

    return results


def clear_log_file(logfile):
    # make sure log directory exists
    try:
        os.makedirs(os.path.dirname(logfile))
    except OSError:
        pass
    with open(logfile, 'w'):
        pass
