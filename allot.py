from extract_student_preferences import get_student_prefs
from extract_proj_prefs import get_project_prefs
from extract_proj_max_cap import get_project_maxcap
import pandas as pd
from config import n_candidate_preferences
import copy

def allot():
    # students: List of students who filled the project preference format
    # student_prefs : Dict of student rollno and list of their project preference order as key-value pairs.
    students, student_prefs = get_student_prefs()

    # projects: List of projects who filled the project preference format
    # project_prefs : Dict of project name and list of their eligible students preference order as key-value pairs.
    projects, project_prefs = get_project_prefs()

    count_projs = get_project_maxcap()



    for p in projects: # Ensuring the maxcap for each project is minimum of the permissible maxcap, and the eligible students.
        count_projs[p] = min(
            count_projs.get(p, 0), # Max Capacity submitted by the project.
            len(project_prefs[p])  # len(project_prefs[p]) is the number of eligible students for the concerned project.
            )     

    max_cap_vals = copy.deepcopy(count_projs) # To keep the original maxcap values for stats.

    allocations = dict()    # * Stores (Student, Project) pairs | Final return entity!
    fraud = [] 
    # To store the roll numbers of the students who have been found in the project preferences, but they haven't filled that project / or the preference form!

    changed = True # To keep track of whether the allocation has been changed or not. If not, then we can stop the algorithm.

    # * Gale-Shapley Algorithm
    while changed:
        changed = False # If no changes, then stable allotment reached
        for p in projects: # Iterating through each project | p : project
            for s in project_prefs[p]: # Iterating through each student in the project's eligible list | s : student
                if (s not in students ) or p not in student_prefs[s]: # If student is not found in student prefs OR student didn't fill this project as his/her preference.
                    if [s, p] not in fraud:
                        fraud.append([s, p])
                    continue
                elif count_projs.get(p, 0) > 0:  # Project has some space for more students
                    if allocations.get(s, None) is not None: # If student has been allocated a project already.
                        if student_prefs[s].index(allocations[s]) > student_prefs[s].index(p): # * Project `p` has higher preference from student `s` than the project currently allotted to him
                            count_projs[allocations[s]] += 1 # As we are removing the student from previously allocated project.
                            allocations[s] = p # Update allocation of student `s` to project `p`
                            count_projs[p] -= 1 # Update new allocated project's remaining capacity.
                            changed = True
                    else:   # * Student currently has no project allotted to him
                        allocations[s] = p # Allocate student `s` to project `p`
                        count_projs[p] -= 1 # Update new allocated project's remaining capacity.
                        changed = True
                else:
                    break

    prefs = [0] * n_candidate_preferences # Maintain statistics of the number of times each preference is filled. 

    project_freq = {} # Maintain statistics of the number of times each project is filled.

    allocs= [] # Allocations in the form of (Student, Project) pairs.

    for i, j in allocations.items():
        prefs[student_prefs[int(i)].index(j)] += 1 # Updating the count of preference that is filled. 
        project_freq[j] = project_freq.get(j, 0) + 1 # Updating the count of project that is filled.
        allocs.append([i, j])
    allocs.sort()
    print('\n\n\33[32mPreferences filled: ', prefs, '\n\nTotal allocated projects = ',sum(prefs), end='\n\n')

    # Make a df with three columns project, freq, and maxcap
    # To show statistics in the following format : Project, Number of students actually allocated, Max capacity.
    df = pd.DataFrame(columns=['project', 'freq', 'maxcap'])
    for p in projects:
        df.loc[len(df)] = [p, project_freq.get(p,0), max_cap_vals.get(p,0)]
    df.to_excel('statistics.xlsx', index=False)
    print('Statistics saved to statistics.xlsx', end='\n\n')

    # Make a df with student_id, project_alloted
    df = pd.DataFrame(allocs, columns=['student_id', 'project_alloted'])
    for i in range(len(allocs)):
        # Append entries in the list allocs to df
        df.iloc[i,0] = (allocs[i][0])
        df.iloc[i,1] = allocs[i][1]
    df.to_excel('allotment.xlsx', index=False)
    print('Allotment stored at allotment.xlsx\33[0m', end='\n\n')

    if(len(fraud)>0):
        # Make a df with fraud_student_id, fraud_project_attempt
        df = pd.DataFrame(fraud, columns=['fraud_student_id', 'fraud_project_attempt'])
        for i in range(len(fraud)):
            # Append entries in the list allocs to df
            df.iloc[i,0] = (fraud[i][0])
            df.iloc[i,1] = fraud[i][1]
        df.to_excel('fraud.xlsx', index=False)
        print('\033[91m!!! Suspected fraud cases stored at fraud.xlsx !!!\033[0m')
def intro_print():
    # Print the file batman.txt
    with open('batman.txt', 'r') as f:
        print(f.read())
        
def credits():

    tanwargit = '\33[34mhttps://github.com/cliche-niche\33[0m';
    premgit = '\33[34mhttps://github.com/PremBharwani\33[0m';
    print(f'\nCredits: \nAditya Tanwar {tanwargit}\nPrem Bharwani {premgit}\n')

if __name__=='__main__':
    intro_print()
    allot()
    credits()
