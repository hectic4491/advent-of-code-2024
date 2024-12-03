# pylint: skip-file
from itertools import filterfalse

"""Problem 2; part 1"""


# Read file contents and write them into our data variable.
data = []
with open("problem_2/input.txt", "r") as f:
  for report in f:
    data.append([int(n) for n in report.split()])


def safe_check(report):
  """Check Function

  We calculate the integer difference between consecutive levels in a
  report and store the unique differences in 'unique_differences'.
  
  We then take the set difference of unqiue_differences to either the
  increase or decrease set, dependent on the sign of the first
  difference. 
  
  If the set difference of either is ever non-empty, we return false.
  Otherwise we return true.
  """
  unique_differences = set()
  increase = set([1, 2, 3])
  decrease = set([-1, -2, -3])

  for i, level in enumerate(report):
    if i > 0: # we want differences, so skip the first level.
      unique_differences.add(difference:= level - report[i-1])

      if difference > 0:
        if unique_differences.difference(increase):
          # if this set difference is ever non empty:
          return False
      else:
        if unique_differences.difference(decrease):
          # if this set difference is ever non empty:
          return False

  return True


# Filter our data with the check, cast it to a list, and count elements.
safe_reports_count = len(list(filter(safe_check, data)))
print(f"Part 1 answer: {safe_reports_count}")


""" Problem 2; part 2"""

# Focus on the bad reports:
failed_data = list(filterfalse(safe_check, data))

def check_bad_reports(bad_report):
  report = bad_report.copy()
  difference = []
  positives = []
  negatives = []
  constants = []

  for i, n in enumerate(report):
    if i > 0: # skip first integer difference
      difference.append(n - report[i-1])

  for diff in difference:
    if diff > 0:
      positives.append(diff)
    elif diff < 0:
      negatives.append(diff)
    else:
      constants.append(diff)

  report_length = len(report)
  largest = max(len(positives), len(negatives), len(constants))

  if report_length - largest > 2:
    return False
  
  for i in range(len(report)):
    report_copy = report.copy()
    report_copy.pop(i)
    if safe_check(report_copy):
      return True
    
  return False
    

saved_reports_count = len(list(filter(check_bad_reports, failed_data)))
print(f"Part 2 answer: {saved_reports_count + safe_reports_count}")
