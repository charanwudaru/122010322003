import requests
import json

def get_numbers(urls):
  """Gets numbers from the specified URLs."""
  numbers = []
  for url in urls:
    response = requests.get(url, timeout=500)
    if response.status_code == 200:
      data = json.loads(response.content)
      numbers.extend(data["numbers"])
  numbers = sorted(list(set(numbers)))
  return numbers

def main():
  """The main function."""
  urls = [
      "http://20.244.56.144/numbers/primes",
      "http://20.244.56.144/numbers/fibo",
      "http://20.244.56.144/numbers/odd",
  ]
  numbers = get_numbers(urls)
  print(json.dumps({"numbers": numbers}))

if __name__ == "__main__":
  main()
