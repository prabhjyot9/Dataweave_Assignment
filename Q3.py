def remove_duplicates(data):
  seen = set()
  result = []
  for item in data:
    name = item["name"]
    if name not in seen:
      seen.add(name)
      result.append(item)
  return result

data = []
while True:
    name = input("Enter a name (or 'done' to finish): ")
    if name == "done":
        break
    age = int(input("Enter the age: "))
    data.append({"name": name, "age": age})

uniqe_data = remove_duplicates(data)
print(uniqe_data)
