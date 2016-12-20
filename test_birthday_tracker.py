import birthday_tracker

def test_get_command_line_args():
  args = birthday_tracker.get_command_line_args()
  assert args['name'] == None
  assert args['birthdate'] == None

def test_is_date_valid():
  assert birthday_tracker.is_date_valid('') == False
  assert birthday_tracker.is_date_valid('0-0-0') == False
  assert birthday_tracker.is_date_valid('1-1-2016') == True
  assert birthday_tracker.is_date_valid('01-01-2016') == True
  assert birthday_tracker.is_date_valid('32-01-2016') == False
  assert birthday_tracker.is_date_valid('10-13-2016') == False
  assert birthday_tracker.is_date_valid('10-01-2030') == False
