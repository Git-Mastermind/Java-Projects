sentence = input('Enter a sentence: ')
index = sentence.find('app is called') + len('app is called')
app_name = sentence[index:].split('.')[0].strip()
print(f'You app is called: {app_name}')

# input_bug_report = input('Enter report: ').lower()
# app_name_index = input_bug_report.find('app is called') + len('app is called')
# app_name = input_bug_report[app_name_index:].split('.').strip()[0]
# print(app_name)
# bug_name_index = input_bug_report.find('the bug is') + len('the bug is')
# bug_name = input_bug_report[bug_name_index:].split('.').strip()[0]
# print(bug_name)
