## Instructions for Excel files

* All the files should have the extension `.xlsx`

* Names of projects: These should be consistent across all occurrences of the project in each file, and should not contain any special characters. Use only the `62` alphanumeric characters, `_`, spaces, and `-`. This is to ensure that no exceptions arise while inferring the project names from directory, preference lists or otherwise.

* `master_responses`: This file contains the project preferences of each student. 
    * Each row corresponds to one student.
    * The first column in each row should be the roll number of the student.
    * The next `n` columns should be the project names in the preference of the student. There should be NO repetitions in this list, violating which might lead to unexpected behavior. *(n=Number of preferences)*

* `./projects`: This directory should contain a filename corresponding to each project. The file corresponding to a project should contain the merit list (in the form of **roll numbers**) for the same project, i.e., the "preferred students" of the project. 
    * The filename should be exactly the name of the project; consistent with all its other occurrences. The project name will be inferred from the filename
    * The first row is reserved for the column heading, the actual roll numbers should start from the second row onwards
    * The student who is most preferred by the project should be in the beginning and least preferred should be towards the end
    * If a student does not qualify for the project, he should NOT be included in the list AT ALL

* `./maxcap`: This directory shall be used to scrape the maximum students a project is willing to take. 
    * The first row is reserved for the column headers. The first column shall contain the project name, and the second column shall contain the maximum capacity (numeric) the project is willing to tolerate
    * The project name will be inferred from the entries, so it needs to again be consistent