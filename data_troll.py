import utils
import logging
import os

from queries.data_trolls_sql_queries import CREATE_DATA_TROLLS_TABLE, INSERT_INTO_DATA_TROLLS_TABLE

# get directory
directory = os.path.dirname(__file__)

# commandline program --- first collect all the data
print('Hello db py world!!!')

print("""I see you are the new data troll around these parts of town.
Well, before you become the official data troll I to get some data from you.""")
print

# list for all data troll information -- for db insert later on
data_troll_info = []

# data troll name
your_name = raw_input("Enter your name, data troll: ")
print

# push name info
data_troll_info.append(your_name)

# data troll fave color
your_favourite_color = raw_input("Enter your favorite color: ")
print

# push color info
data_troll_info.append(your_favourite_color)

# flag for correct start date format
start_date_flg = False

# data troll employee start date
# precaution to get correct date format -- ask them this question until they get it right!
while not start_date_flg:

    # employee start date -- need date format as yyyymmdd
    employee_date = raw_input("Enter your employee start date in the YYYYMMDD format (no need for dashes or slashes): ")

    if len(employee_date) == 8:             # check input is 8 chars long... it should be without dashes

        # convert to python date
        employee_start_date = utils.convert_to_date(employee_date)
        print

        # push start date info
        data_troll_info.append(employee_start_date)

        # start date is a go, roger that
        start_date_flg = True

    else:
        # just keep going until it's a real date
        print
        print("***** There is a mistake in there... You entered {} *****".format(employee_date))
        print

# data troll title
your_title = raw_input("Enter your role/title: ")
print

# push title info
data_troll_info.append(your_title)


# flag for yes or no response
yes_no_flg = False

# data troll survey
# checks for yes or no response
while not yes_no_flg:

    # data troll mini survey
    mini_survey = raw_input("Yes or No. Did you enjoy this? ")
    print

    # check if answer is yes or no
    if mini_survey.lower() == 'yes' or mini_survey.lower() == 'no':

        # convert to bool response
        enjoyed = utils.convert_to_bool(mini_survey.lower())

        # push bool response
        data_troll_info.append(enjoyed)

        # response is yes/no, roger that
        yes_no_flg = True

    else:
        print
        print("***** There is a mistake in there... You entered {} *****".format(mini_survey))
        print

print('***'*50)
print
print('Thank you for your answers. Time to populate the table user_scratch.data_trolls in the monthly snapshot ...')

# .....data troll information has been collected at this point.....

# get db creds from secret yaml file
configs = utils.configs_yml_to_dict(os.path.join(directory, 'creds.yml'))
# configs = utils.configs_yml_to_dict('creds.yml')

# define creds for easy reading
user = configs['database_configs']['user']
pw = configs['database_configs']['pw']
host = configs['database_configs']['host']
db = configs['database_configs']['db']

# create db connection from yaml creds
connect_to_db = utils.connect_to_database(username=user, host=host, db_name=db, password=pw)

# run create table sql
utils.run_sql_query(connect_to_db, CREATE_DATA_TROLLS_TABLE, {})

# push data -- run insert sql
utils.run_sql_query(connect_to_db, INSERT_INTO_DATA_TROLLS_TABLE,
                    {'name': data_troll_info[0],
                     'favourite_color': data_troll_info[1],
                     'employee_start_at': data_troll_info[2],
                     'title': data_troll_info[3],
                     'enjoyed_lunch_n_learn': data_troll_info[4],
                     'data_troll_start_at': utils.get_today_date()
                     })

# close the connection
utils.disconnect_from_database(connect_to_db)

print
print('bibbidi-bobbidi-boo..... done!')
print
print("data_trolls has been updated with your credentials! What? You don't believe me? Go check, I dare you...")
print

# logs.....

# clear previous log file
utils.clear_log_file('logs/data_trolls.log')

print("""Logs are great right?
They show you what's going on and they keep a record of things too!
Woo data about data, love it <3""")
print
print("Generating logs...")

# set up log file
log_location = os.path.join(directory, 'logs', 'data_trolls.log')
logging.basicConfig(filename=log_location, level=logging.INFO)

print
print("Logs complete.")
print

# log info
logging.info(utils.log_operation('Data regarding data troll {} has been updated in user_scratch.data_trolls'.format(data_troll_info[0])))

print("Check out the logs in the /logs folder to see what it has logged")
