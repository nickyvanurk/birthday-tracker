import birthday_tracker
from testfixtures import TempDirectory

tempdir = TempDirectory()
path = tempdir.makedir('tests/fixtures')
tempdir.write('tests/fixtures/birthdates.json', b'')

def teardown_module(module):
  TempDirectory.cleanup_all();

def test_get_command_line_args():
  args = birthday_tracker.get_command_line_args()
  assert args['name'] == ''
  assert args['birthdate'] == ''

def test_is_date_valid():
  assert birthday_tracker.is_date_valid('') == False
  assert birthday_tracker.is_date_valid('0-0-0') == False
  assert birthday_tracker.is_date_valid('1-1-2016') == True
  assert birthday_tracker.is_date_valid('01-01-2016') == True
  assert birthday_tracker.is_date_valid('32-01-2016') == False
  assert birthday_tracker.is_date_valid('10-13-2016') == False
  assert birthday_tracker.is_date_valid('10-01-2030') == False

def test_json_read_write():
  data = {'John Doe' : '20-12-2016'}
  data_file = path + '/birthdates.json'
  assert birthday_tracker.get_json_data(data_file) == {}
  birthday_tracker.dump_json_data(data, data_file)
  assert birthday_tracker.get_json_data(data_file) == data




