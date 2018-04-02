def replace_project_name(project_name):
    # Read in the file
    files = ['./app/templates/base.html', './app/templates/auth/login.html', './app/templates/main/index.html']
    for file in files:
        with open(file, 'r') as f:
            filedata = f.read()

        # Replace the target string
        filedata = filedata.replace('%%PROJECT_NAME%%', project_name)

        # Write the file out again
        with open(file, 'w') as f:
            f.write(filedata)

def post_hook():
    project_slug = '{{cookiecutter.project_slug}}'
    project_name = '{{cookiecutter.project_name}}'
    print(project_name, project_slug)
    replace_project_name(project_name)
    print("**************************************************")
    print("\tPost Install Instructions")
    print("\tExecute the following")
    print(f"\tsee {project_slug}/post_instructions.txt")
    print("**************************************************")
    post_instructions = f"""
        cd {project_slug}
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        python main.py

    """

    print(post_instructions)
    with open('./post_instructions.txt', 'w') as f:
        f.write(post_instructions)

if __name__ == '__main__':
    post_hook()