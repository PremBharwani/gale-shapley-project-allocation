import pandas as pd
from config import n_candidate_preferences, student_preferences_path

def get_student_prefs():
    """
    Returns: 
    a) List of students in the preference form  
    eg: [roll1, roll2, roll3, roll4, roll5, ...]
    and 
    b) Student's preference dictionary. 
    eg : {roll1: [project1, project2, project3, project4, project5, ...], roll2: [project1, project2, project3, project4, project5, ...], ...}
    """

    df = pd.read_excel(student_preferences_path) # Read the student preferences.
    n_responses = df.shape[0] # Number of responses.
    
    student_prefs = {} # Student's preference dictionary. key: rollnumber, value: order of preference.
    
    students = [] # To keep a track of the students who filled the preference form. 

    for i in range(n_responses):
        try:
            rollno = int(df.iloc[i, 0]) # Get the rollno. from column 0. 
            prefs = df.iloc[i, 1:n_candidate_preferences + 1] # Get the preferences from column 1 to candidate_preferences+1.
            student_prefs[rollno] = prefs.tolist()
            if rollno not in students:
                students.append(rollno)
            else: # Duplicate rollno found
                raise Exception(f"Duplicate Roll Number found {rollno}. Please refer to README on how to resolve this.")

        except:
            continue
    
    return students, student_prefs

if __name__ == "__main__":
    students, student_prefs = get_student_prefs()
    print(students)
    print(student_prefs)