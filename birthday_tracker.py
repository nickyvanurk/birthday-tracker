#!/usr/bin/python3
import contextlib, argparse, collections, datetime, json, calendar

def get_command_line_args():
  defaults = {'name': '', 'birthdate': ''}
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', dest='name', help='name of person')
  parser.add_argument('-b', dest='birthdate', help='date of birth')
  command_line_args = {k:v for k, v in vars(parser.parse_args()).items() if v}
  return collections.ChainMap(command_line_args, defaults)

def date_is_valid(birthdate):
  try:
    date = datetime.datetime.strptime(birthdate, "%d%m%Y").date()
  except:
    return False
  return date <= datetime.date.today()

def get_json(file):
  with open(file, 'r') as f:
    try:
      return json.load(f)
    except:
      return {}

def dump_json(data, file):
  with open(file, 'w') as f:
    json.dump(data, f)

def add_birthday(name, birthdate, file):
  d = get_json(file)
  d.update({name : birthdate})
  dump_json(d, file)

def get_next_birthday(date, birthdate):
  try:
    next_birthday = birthdate.replace(year=date.year)
    if next_birthday < date:
      next_birthday = birthdate.replace(year=date.year+1)
  except:
    next_birthday = birthdate.replace(day=28, year=date.year)
    if next_birthday < date:
      next_birthday = birthdate.replace(day=28, year=date.year+1)
  return next_birthday

def print_birthday_list(file):
  d = get_json(file)
  d = collections.OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse=True))
  for key, value in d.items():
    birthdate = datetime.datetime.strptime(value, "%d%m%Y").date()
    today = datetime.date.today()
    next_birthday = get_next_birthday(today, birthdate)
    print('{name}\t{countdown}\t{new_age}\t{next_bday}'.format(
      name=key,
      countdown=str((next_birthday - today).days),
      new_age=str(today.year-birthdate.year + next_birthday.year-today.year),
      next_bday=next_birthday.strftime('%d-%m-%Y'))
    )

def main():
  args = get_command_line_args()
  name = args['name'].strip()
  birthdate = args['birthdate'].replace('-','').replace(' ', '')
  file = 'birthdates.json'

  if name and birthdate:
    if date_is_valid(birthdate):
      add_birthday(name, birthdate, file)
    else:
      print('Invalid birthday')
  else:
    print_birthday_list(file)

if __name__ == '__main__':
  with contextlib.suppress(KeyboardInterrupt):
    main()
