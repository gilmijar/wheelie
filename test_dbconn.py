from unittest import TestCase
import dbconn


class TestDBConnection(TestCase):
    def setUp(self):
        self.db = dbconn.connection('wheelie_test')
        self.cursor = self.db.cursor()

    def tearDown(self):
        self.cursor.close()
        self.db.close()

    def test_connection_connects_to_db(self):
        self.cursor.execute("SELECT 1;")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 1)

    def test_insert_places_rows_in_db(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50));")
        self.cursor.execute("INSERT INTO test_table (name) VALUES ('test_name');")
        self.db.commit()
        self.cursor.execute("SELECT name FROM test_table WHERE name='test_name';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 'test_name')
        self.cursor.execute("DROP TABLE test_table;")
        self.db.commit()