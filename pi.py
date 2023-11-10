import base64
from github import Github

# Replace these with your GitHub credentials and repository information
github_username = "sajanchahal"
github_token = "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"
repository_name = "wphunter"
file_name = "output.txt"

# Create a GitHub instance
g = Github(github_username, github_token)

# Get the repository
repo = g.get_user().get_repo(repository_name)

# Simulate loop values
def generate(arr, i, s, len, values_str_list):
    # base case
    if i == 0:
        values_str_list.append(s)
        return

    # iterate through the array
    for j in range(0, len):
        # Create new string with next character
        appended = s + arr[j]
        generate(arr, i - 1, appended, len, values_str_list)

# function to generate all possible passwords
def crack(arr, len):
    values_str_list = []

    # call for all required lengths
    for i in range(4, 5):
        generate(arr, i, "", len, values_str_list)

    return values_str_list

# Driver Code
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','+','-','.','~','|','<','>','=','-','_','/',':',';','?','[',']','{','}','~']
len_arr = len(arr)

# Generate loop values
values_str_list = crack(arr, len_arr)

# Convert values to a string
values_str = "\n".join(values_str_list)

try:
    # Try to get the file
    contents = repo.get_contents(file_name)
    # Update the file if it exists
    repo.update_file(file_name, "Update loop values", values_str, contents.sha)
    print("Loop values updated and pushed to GitHub.")
except Exception as e:
    # If the file doesn't exist, create it
    repo.create_file(file_name, "Create loop values", values_str)
    print("Loop values file created and pushed to GitHub.")
