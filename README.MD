## Running
**Before running please read through the [instructions](INSTRUCTIONS.md)!**
```bash
python allot.py
```
* `allot.py` is the only file you need to run. All the other files are utilities. <br>
It produces two important files, one which contains *(Roll Number, Project Alloted)* pairs, and one which contains fraudulent pairs, which may arise from a student being allotted a project which was not in his preferences or if a student had not filled the preference form altogether. The other files are common statistics regarding the allocation.
* `config.py` has some parameters-
    * Number of preferences a student is allowed to fill
    * The path to `master_responses`
* Dependencies: `pandas`

## Common debugging:
* `Duplicate Roll Number found...`: There is a duplicate entry (of a roll number) in `master_responses`. Some suggestions-
    * Keep the form editable to ensure that the same person does not fill the form twice
    * It might be the case that someone made a typo while filling the form. Take suitable actions
* Check the project names, most probably there is an inconsistency
* A student/project not getting an allotment is completely possible and is not erroneous. No bugs here, only functionalities

## 🦇 Credits 🦇

* [Aditya Tanwar](https://github.com/cliche-niche) 
* [Prem Bharwani](https://github.com/PremBharwani)
