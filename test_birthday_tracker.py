import birthday_tracker

def test_get_command_line_args():
  args = birthday_tracker.get_command_line_args()
  assert args['name'] == None
  assert args['birthdate'] == None
