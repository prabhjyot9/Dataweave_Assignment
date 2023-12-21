string_input = input("Enter strings separated by commas: ")
string_list = string_input.split(", ")

unique_values = set()

for string_value in string_list:
    sentence_case_value = string_value.capitalize()
    unique_values.add(sentence_case_value)

output_list = list(unique_values)
print(output_list)