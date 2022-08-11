import pandas as pd
import os

def extract_project_maxcap(filename, project_maxcap):
    df = pd.read_excel(f"./maxcap/{filename}")
    n_responses = df.shape[0]
    for i in range(n_responses):
        proj_name = df.iloc[i, 0].replace('\n','').strip()
        max_cap = df.iloc[i, 1]
        project_maxcap[proj_name] = max_cap

def get_project_maxcap():
    """
    Returns:
    a) Dictionary of projects and their max capacities as key-value pairs.
    eg: {project1: max_cap1, project2: max_cap2, project3: max_cap3, project4: max_cap4, project5: max_cap5, ...}
    """
    project_maxcap = {} # Dictionary to hold the max capacity to accomodate students for each project.
    for file in os.listdir("./maxcap"):
        if not ".xlsx" in file:
            continue
        extract_project_maxcap(file, project_maxcap)
    return project_maxcap

if __name__=="__main__":
    project_maxcap =get_project_maxcap()
    print(project_maxcap)

