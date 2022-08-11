import pandas as pd
import os

def ret_list(filename):
    df = pd.read_excel(f"./projects/{filename}")
    roll_list = df.iloc[:,0].tolist() 
    return roll_list

def get_project_prefs():
    """
    Returns:
    a) List of projects in the preference form
    eg: [project1, project2, project3, project4, project5, ...]
    and
    b) Project's preference dictionary.
    eg: {project1: [roll1, roll2, roll3, roll4, roll5, ...], project2: [roll1, roll2, roll3, roll4, roll5, ...], ...}
    NOTE : Each value for project keys in the dict is in decreasing order of priority. eg project 1 has priority : roll1> roll2> roll3> ... so on...
    """

    project_prefs = {} # Project's preference dictionary. key: project, value: order of preference.
    projects = [] # Name of the projects that have submitted merit lists. 
    for file in os.listdir("./projects"):
        if not ".xlsx" in file:
            continue
        project_prefs[file[:-5]] = ret_list(file)
        if file[:-5] not in projects:
            projects.append(file[:-5])
    return projects, project_prefs

if __name__=="__main__":
    projects, project_prefs = get_project_prefs()
    print(projects)
    print(project_prefs)
