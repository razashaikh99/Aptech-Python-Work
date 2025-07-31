import os.path
import pandas
import pydriller
from pydriller import Repository

repoInput = input("Enter Repo URL : ")

url = repoInput

# url = [
#     "https://github.com/tensorflow/tensorflow",
#     "https://github.com/pytorch/pytorch"
# ]

committername, email, CommitMsg, DateCommit, RepoName = [], [], [], [], []
print(f"Fetching Information from {url}")

for a in Repository(url).traverse_commits():
    committername.append(a.author.name)
    email.append(a.author.email)
    CommitMsg.append(a.msg)
    DateCommit.append(a.author_date)
    RepoName.append(a.project_name)

print("Scrapping Complete")

GithubRepo = {
    "Repo Name": RepoName,
    "Name": committername,
    "Email": email,
    "Message": CommitMsg,
    "Date": DateCommit
}

github_df = pandas.DataFrame(GithubRepo)

filename = input("Enter Filename to Save: ")

if os.path.exists(f"{filename}.csv"):
    print("File Already Exists")
else:
    github_df.to_csv(f"{filename}.csv", index=False)