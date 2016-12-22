import birthday_tracker, datetime
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

def test_date_is_valid():
  assert birthday_tracker.date_is_valid('') == False
  assert birthday_tracker.date_is_valid('000') == False
  assert birthday_tracker.date_is_valid('112016') == True
  assert birthday_tracker.date_is_valid('01012016') == True
  assert birthday_tracker.date_is_valid('32012016') == False
  assert birthday_tracker.date_is_valid('10132016') == False
  assert birthday_tracker.date_is_valid('10012030') == False

def test_add_birthday():
  file = path + '/birthdates.json'
  assert birthday_tracker.get_json(file) == {}
  birthday_tracker.add_birthday('John Doe', '20-12-2016', file)
  assert birthday_tracker.get_json(file) == {'John Doe' : '20-12-2016'}

def test_remove_birthday():
  file = path + '/birthdates.json'
  birthday_tracker.add_birthday('John Doe', '20-12-2016', file)
  assert birthday_tracker.get_json(file) == {'John Doe' : '20-12-2016'}
  birthday_tracker.remove_birthday('John Doe', file)
  assert birthday_tracker.get_json(file) == {}

def test_get_next_birthday():
  # Birthday in a leap year on 29th of february
  birthdate = datetime.datetime(year=1992, month=2, day=29).date()
  # Date (leap year) < Birthday
  date = datetime.datetime(year=2016, month=2, day=20).date()
  expected = datetime.datetime(year=2016, month=2, day=29).date()
  assert birthday_tracker.get_next_birthday(date, birthdate) == expected
  # Date (no leap year) < Birthday
  date = datetime.datetime(year=2017, month=2, day=20).date()
  expected = datetime.datetime(year=2017, month=2, day=28).date()
  assert birthday_tracker.get_next_birthday(date, birthdate) == expected
  # Date == Birthday
  date = datetime.datetime(year=2016, month=2, day=29).date()
  expected = datetime.datetime(year=2016, month=2, day=29).date()
  assert birthday_tracker.get_next_birthday(date, birthdate) == expected
  # Date > Birthday
  date = datetime.datetime(year=2016, month=3, day=1).date()
  expected = datetime.datetime(year=2017, month=2, day=28).date()
  assert birthday_tracker.get_next_birthday(date, birthdate) == expected





