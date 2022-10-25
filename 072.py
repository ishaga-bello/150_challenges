# Create a list of six school subjects. Ask the user which of these subjects they don’t like. Delete the subject they have chosen from the
# list before you display the list again.

subject_list = ['physics', 'biology', 'geo', 'maths', 'history', 'logic']
print(subject_list)
dislike = (input('Enter subject don’t like: '))
subject_list.remove(dislike)
print(sorted(subject_list))