#!/usr/bin/python3
import contextlib, argparse, collections

def get_command_line_args():
  defaults = {'name': None, 'birthdate': None}
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', dest='name', help='name of person')
  parser.add_argument('-b', dest='birthdate', help='date of birth')
  command_line_args = {k:v for k, v in vars(parser.parse_args()).items() if v}
  return collections.ChainMap(command_line_args, defaults)

def main():
  args = get_command_line_args()

  if args['name'] and args['birthdate']:
    print(args['name'] + ', ' + args['birthdate'])
  else:
    print('Display birthdays list')

if __name__ == '__main__':
  with contextlib.suppress(KeyboardInterrupt):
    main()
