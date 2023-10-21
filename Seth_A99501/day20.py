import os
#create a file
lecture_note1="note.txt"
with open(lecture_note1,'w') as file:
    file.write("This is new file")
print("Created file: ", lecture_note1)

#create a file
lecture_note3="note3.txt"
with open(lecture_note3,'w') as file:
    file.write("This is new file")
print("Created file: ", lecture_note3)


#delete a file
os.remove(lecture_note1)
print("deleted file: ", lecture_note1)

#rename a file
lecture_note2="updated_notes.txt"
os.rename(lecture_note3,lecture_note2)
print(f"File {lecture_note3} has been renamed to: {lecture_note2}")
