#!/usr/bin/python3
import contextlib, argparse, collections, datetime, json, calendar

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
    date = datetime.datetime(year,month,day).date()
  except ValueError:
    return False
  return date <= datetime.date.today()

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
    data = collections.OrderedDict(sorted(data.items(), key=lambda t: t[1], reverse=True))
    for key, value in data.items():
      bdate = value.split('-')
      bdate = datetime.datetime(year=int(bdate[2]),
                                month=int(bdate[1]),
                                day=int(bdate[0])).date()
      today = datetime.date.today()

      try: next_bday = bdate.replace(year=today.year)
      except ValueError: next_bday = bdate.replace(day=28, year=today.year)

      if next_bday < today:
        try: next_bday = bdate.replace(year=today.year + 1)
        except ValueError: next_bday = bdate.replace(day=28, year=today.year + 1)

      days_until_bday = (next_bday - today).days
      new_age = today.year-bdate.year + next_bday.year-today.year
      eu_date = next_bday.strftime('%d-%m-%Y')

      print(key + '\t' + str(days_until_bday) + '\t' + str(new_age) + '\t' + eu_date)

if __name__ == '__main__':
  with contextlib.suppress(KeyboardInterrupt):
    main()
