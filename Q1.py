def intersection1(list1, list2):
  return set(list1) & set(list2)

def intersection2(list1, list2):
  intersection = []
  for i in list1:
    if i in list2 and i not in intersection:
      intersection.append(i)

  return intersection


list1 = list(map(int, input("Enter elements of list1 separated by spaces: ").split()))
list2 = list(map(int, input("Enter elements of list2 separated by spaces: ").split()))

intersection1 = intersection1(list1, list2)
intersection_list = list(intersection1)

intersection2 = intersection2(list1, list2)


print(f"Unique intersection elements using Intersection1: {intersection_list}")
print(f"Unique intersection elements using Intersection2: {intersection2}")