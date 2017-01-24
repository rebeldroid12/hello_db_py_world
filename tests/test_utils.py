import os
import utils
import unittest
import datetime as dt


# creds -- will be used in tests later on (dont repeat code if you dont have to)
def get_test_creds():
    # configs_yml_to_dict fn
    directory = os.path.dirname(__file__)
    yml = utils.configs_yml_to_dict(os.path.join(directory, 'test_creds.yml'))

    # test
    return yml['database_configs']


class TestUtils(unittest.TestCase):
    # test all utils functions

    print(get_test_creds)

    # test configs_yml_to_dict
    def test_configs_yml_to_dict(self):
        # configs_yml_to_dict fn
        directory = os.path.dirname(__file__)
        yml = utils.configs_yml_to_dict(os.path.join(directory, 'test_creds.yml'))

        # test
        self.assertEqual(yml['database_configs']['db'], 'staging')


    def test_convert_to_bool_yes(self):
        # test convert_to_bool function

        yes = 'yes'
        bool_yes = utils.convert_to_bool(yes)

        self.assertTrue(bool_yes)

    def test_convert_to_bool_no(self):
        # test convert_to_bool function

        no = 'no'
        bool_no = utils.convert_to_bool(no)

        self.assertFalse(bool_no)

    def test_convert_to_date(self):
        date = '20200202'
        date_correct = utils.convert_to_date(date)

        self.assertEqual(date_correct, dt.date(2020,2,2))

    # test connect_to_database success case
    def test_connect_to_database_success(self):
        # creds
        creds = get_test_creds()

        t = utils.connect_to_database(username=creds['user'], db_name=creds['db'], password=creds['pw'], host=creds['host'])
        self.assertNotEqual(t, 'Could not connect')

    # test connect_to_database fail case
    def test_connect_to_database_fail(self):
        # creds
        creds = get_test_creds()

        t = utils.connect_to_database(username=creds['user'], db_name='db2', password=creds['pw'],
                                      host=creds['host'])

        self.assertEqual(t, 'Could not connect')

    # test disconnect_from_database
    def test_disconnect_from_database(self):
        # creds
        creds = get_test_creds()

        connection = utils.connect_to_database(username=creds['user'], db_name=creds['db'], password=creds['pw'],
                                      host=creds['host'])
        self.assertEqual(utils.disconnect_from_database(connection), 'closed')

    # test run_sql_query create
    def test_run_sql_query_create(self):
        # create query
        query = '''CREATE TABLE user_scratch.test_utils_table (
            name TEXT
            ,fecha DATE
            ,count INTEGER
            );
            '''

        # creds
        creds = get_test_creds()

        connection = utils.connect_to_database(username=creds['user'], db_name=creds['db'], password=creds['pw'],
                                               host=creds['host'])
        # test
        result = utils.run_sql_query(connection, query, {})
        self.assertEqual(result, 'no results to fetch')

    # test run_sql_query select
    def test_run_sql_query_select_no_data(self):
        # select query
        create_query = '''CREATE TABLE user_scratch.test_utils_table2 (
            name TEXT
            ,fecha DATE
            ,count INTEGER
            );'''

        query = '''SELECT * FROM user_scratch.test_utils_table2;'''

        # creds
        creds = get_test_creds()

        connection = utils.connect_to_database(username=creds['user'], db_name=creds['db'], password=creds['pw'],
                                               host=creds['host'])
        # test
        utils.run_sql_query(connection, create_query, {})
        result = utils.run_sql_query(connection, query, {})
        self.assertEqual(result, [])

    # test run_sql_query insert
    def test_run_sql_query_insert(self):
        # insert query
        query = '''INSERT INTO user_scratch.test_utils_table
            (name, fecha, count) values (%(name)s, %(fecha)s, %(count)s);
            '''
        params = {'name': 'Loren',
                  'fecha': dt.datetime.today(),
                  'count': 12}

        # creds
        creds = get_test_creds()

        connection = utils.connect_to_database(username=creds['user'], db_name=creds['db'], password=creds['pw'],
                                               host=creds['host'])
        # test
        result = utils.run_sql_query(connection, query, params)
        self.assertEqual(result, 'no results to fetch')

    # test run_sql_query select
    def test_run_sql_query_select(self):
        # select query
        query = '''SELECT * FROM user_scratch.test_utils_table;'''

        # creds
        creds = get_test_creds()

        connection = utils.connect_to_database(username=creds['user'], db_name=creds['db'], password=creds['pw'],
                                               host=creds['host'])
        # test
        result = utils.run_sql_query(connection, query, {})
        self.assertEqual(result[0]['name'], 'Loren')

    # test run_sql_query delete/drop
    def test_run_sql_drop(self):
        # select query
        query = '''drop table user_scratch.test_utils_table;'''

        # creds
        creds = get_test_creds()

        connection = utils.connect_to_database(username=creds['user'], db_name=creds['db'], password=creds['pw'],
                                               host=creds['host'])
        # test
        result = utils.run_sql_query(connection, query, {})
        self.assertEqual(result, 'no results to fetch')

    # test log_operation
    def test_log_operation(self):
        # log_operation fn
        t = utils.log_operation('test')

        # test
        d = dt.datetime.now()
        fmt = '%Y-%m-%d %H:%M:%S'
        t2 = '{} - test'.format(d.strftime(fmt))

        self.assertEqual(t, t2)

if __name__ == '__main__':
    unittest.main()