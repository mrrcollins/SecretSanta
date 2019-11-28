# My Secret Santa Name Picker

I wrote this last year, and then lost it, so I ended up writing it again. christmasdrawing.py will take a .csv file of the people in the drawing, and then randomly pick their secret santa. Using the groups field, people in the same family will not get anyone in their family.

# Setting it up

I shared a Google Sheets document with the family with edit access. The headers of the sheet are:

`firstname,lastname,email,group,list`

Family members can then modify their line. The group field is used to group people that shouldn't get each other in the drawing. I use numbers, but anything should work. 

The list field is for what the person wants for Christmas. I usually link to my Amazon Christmas list.

To email the secret santas, I used mutt. Mutt is easy to set up, and can email from the command line.

# Running Secret Santa

Put the .csv file in the same directory of the script, set up mutt, and modify the line for the file in the script to point to your .csv file. Then, let her rip!

If you want to test, you can comment out the `os.system` line that runs mutt and watch how it goes.
