import hashlib
import requests

def request_api_data(hashed_str):
  url = 'https://api.pwnedpasswords.com/range/'+f'{hashed_str[:5]}'
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching, {res.status_code}. Check the API and try again.')
  return res

def read_response(response):
  print(response.text) #will print all the response that matches the begaining of our hashed passwords.
# The number in front of those hashed strings shows how many times these passwords have been HACKED.

def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h==hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  hashed_str = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  print(f'{password} : {hashed_str}')
  head, tail = hashed_str[:5], hashed_str[5:]
  res = request_api_data(head)
  return get_password_leaks_count(res, tail)

def input_password():
  password = input('Enter the password you want to check : ')
  count = pwned_api_check(password)
  if count:
    print('--------------------- DANGER!! ---------------------')
    print(f'{password} was hacked {count} times.')
    print('----------------------------------------------------')
  else:
    print('Congratulations! Your password is Secure.')

if __name__ == '__main__':
  input_password()
