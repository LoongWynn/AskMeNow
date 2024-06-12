from github import Github
from github import Auth
from dotenv import dotenv_values
from src.utils import env_config, AppConfig
import os
import requests
import tarfile

config = dotenv_values(".env")


@env_config
def init(config: AppConfig):
    auth = Auth.Token(config.access_token)
    github = Github(auth=auth)
    current_user = github.get_user()
    print(f"Login as {current_user.name} <{current_user.email}> | {current_user.id}")
    repo = github.get_repo(config.target_repo)
    print(rawtar := repo.get_archive_link(archive_format="tarball"))
    # download_repo_archive(rawtar,config.target_repo)
    unzip_archive(config.target_repo)


@env_config
def download_repo_archive(archive_url: str, target_repo: str, config: AppConfig):
    root_path = f"./temp/{target_repo}"
    tar_path = os.path.join(root_path, "code.tar.gz")
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    response = requests.get(
        archive_url,
        stream=False,
        headers={"Authorization": f"token {config.access_token}"},
    )
    print(response.status_code)
    with open(tar_path, "wb") as file:
        file.write(response.content)


def unzip_archive(target_repo: str):
    root_path = f"./temp/{target_repo}"
    tar_path = os.path.join(root_path, "code.tar.gz")
    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=root_path)


def draw_file_tree(target_repo: str):
    root_path = f"./docs/docs/"
    work_app_root_dir = os.getcwd()
    os.chdir(root_path)
    count = 0
    with open("./file_tree.md", "w", encoding="utf8") as w:
        w.write('# Source code file trees\n')
        for root_dir, dirs, file_names in os.walk(target_repo):
            for file_name in file_names:
                if file_name.endswith(".md") or file_name.endswith(".MD"):
                    continue
                w.write("\n---\n")
                w.write(f"## {os.path.join(root_dir,file_name)}\n")
                with open(os.path.join(root_dir, file_name), "r", encoding="utf8") as r:
                    try:
                        w.write("```\n" + r.read() + "```\n")
                    except Exception as err:
                        print(os.path.join(root_dir, file_name))
                        print(err)
                        w.write(f"![binary file]({os.path.join(root_dir, file_name)})")

    print(count)
    os.chdir(work_app_root_dir)
