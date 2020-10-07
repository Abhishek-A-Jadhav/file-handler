# file-handler

---
This is version 1.0 of File Handler. And contains lot of bugs. Just an intermidiate programmer. This was intended for personal use but decided to expand over a few ideas and make it publically available. Future plans on upgrading to next version will include lot of bugs solving.

**Known bugs:** No progress bars yet. Working on udating certain variables in real time.
            Few variables does not get initiated in certain places. May lead to crashing.

Please report any other bugs on abhishekajadhavb4@gmail.com I will surely try and fix them in next version.

_**P.S. First time making of a UI based application.**_

---
#### Usage:

##### Just run `main.py` through the terminal. Make sure you have `kivy` installed on your device. Works on Windows, Mac & Linux. Could be used on mobile devices if the user has basic understanding of file-management in mobile devices.

- ##### Copy:
    - **Path:** Enter the path to the directory where the files are located.

    - **Filter:** Filters files in the directry using the given keyword. (Keep blank if none required)

    - **Extension:** Filters the files with given extension. (Keep blank if none required)

    - **List:** Applies the fileters (if given) and lists the files in the first column.

    - **Add files manually:** Enter the name of file that needs to be particularly added after applying filters. (Manually added files will be shown in second column)

    - **Remove files manually:** Enter the name of file that needs to be particularly removed after applying filters.

    - **Compute:** This will combine the files from column 1 and 2 and display a final list of files on which the operation will carry out.

    - **Destination:** Enter the path to destination directory.

    - **Start Copy:** Will start copying files. Sometimes will look like the screen is stuck if files have large sizes. Have not figured out the code for progress bar yet. A message of completion will appear when operation is finished. Be sure to check file list before proceeding.

    - **Reset:** Resets all the inputs and clears all the columns.

- ##### Move:
    **Basically similar steps to Copy.**

- ##### Rename:
    - **Path:** Enter the path to the directory where the files are located.

    - **Filter:** Filters files in the directry using the given keyword. (Keep blank if none required)

    - **Extension:** Filters the files with given extension. (Keep blank if none required)

    - **List:** Applies the fileters (if given) and lists the files in the first column.

    - **Pattern:** Enter the pattern that needs to be followed while renaming. (eg- imgPattern_) This will rename all files startting with 'imgPattern_' and add numbers in front of them -> imgPattern_001. Pressing 'Ok' button will show the glimpse of file naming pattern applied to it.

    - **Prefix:** Enter the prefix that needs to be applied to files. Pressing 'Ok' button will show the glimpse of file added with prefix applied to it.

    - **Suffix:** Enter the suffix that needs to be applied to files. Pressing 'Ok' button will show the glimpse of file added with suffix applied to it.

    _**Pattern, Prefix and Suffix can be used together. (eg- pre_pattern001_suff.ext)**_

    - **Preview:** This will preview the naming of all files in column 2 for confirmation.

    - **Destination:** Enter the path to destination directory.

    - **Start Rename:** Will start renaming files. A message of completion will appear when operation is finished. Be sure to check file list before proceeding.

    - **Reset:** Resets all the inputs and clears all the columns.

- ##### Delete:
    **Basically similar steps to Copy.**

- ##### Auto Scroll:
    This will automatically sort all the files in given directory to the folders of their respecive types. The folders will be created automatically. \

    Folders include:
    - Documents
    - Pictures
    - Videos
    - Setups
    - Compressed
    - Misc

 Let me know if any other category needs to be added.

---
