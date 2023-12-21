def count_code_occurrences():
  data = []
  while True:
    entry = input("Enter a code-count pair (e.g., 1:200) or 'done' to finish: ")
    if entry.lower() == "done":
      break
    try:
      code, count = map(int, entry.split(":"))
      data.append({code: count})
    except ValueError:
      print("Invalid input format. Please enter code-count pairs like 1:200.")

  code_counts = {}
  for entry in data:
    for code in entry.values():
        if code in code_counts:
            code_counts[code] += 1
        else:
            code_counts[code] = 1
  print(f"Code occurrences: {code_counts}")
  return code_counts

count_code_occurrences()