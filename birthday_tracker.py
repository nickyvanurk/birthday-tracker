#!/usr/bin/python3
import contextlib, argparse, collections, datetime

def get_command_line_args():
  defaults = {'name': None, 'birthdate': None}
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

def main():
  args = get_command_line_args()
  if args['name'] and args['birthdate']:
    if is_date_valid(args['birthdate']):
      print(args['name'] + ', ' + args['birthdate'])
    else:
      print('Invalid birthday')
  else:
    print('Display birthdays list')

if __name__ == '__main__':
  with contextlib.suppress(KeyboardInterrupt):
    main()
