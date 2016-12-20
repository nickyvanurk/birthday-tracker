#!/usr/bin/python3
import contextlib, argparse, collections, datetime, json

def get_command_line_args():
  defaults = {'name': '', 'birthdate': ''}
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', dest='name', help='name of person')
  parser.add_argument('-b', dest='birthdate', help='date of birth')
  command_line_args = {k:v for k, v in vars(parser.parse_args()).items() if v}
  return collections.ChainMap(command_line_args, defaults)

def is_date_valid(birthdate):
  try:
    bdate = birthdate.split('-')
    day = int(bdate[0])
    month = int(bdate[1])
    year = int(bdate[2])
    date = datetime.datetime(year,month,day)
  except ValueError:
    return False
  return date <= date.now()

def get_json_data(file):
  with open(file, 'r') as f:
    try:
      data = json.load(f)
    except ValueError:
      data = {}
  return data

def dump_json_data(data, file):
  with open(file, 'w') as f:
    json.dump(data, f)

def main():
  args = get_command_line_args()
  name = args['name'].strip()
  birthdate = args['birthdate'].strip()
  data_file = 'birthdates.json'

  if name and birthdate:
    if is_date_valid(birthdate):
      data = get_json_data(data_file)
      data.update({name : birthdate})
      dump_json_data(data, data_file)
    else:
      print('Invalid birthday')
  else:
    data = get_json_data(data_file)
    for key, value in data.items():
      print(key + ', ' + value)

if __name__ == '__main__':
  with contextlib.suppress(KeyboardInterrupt):
    main()
