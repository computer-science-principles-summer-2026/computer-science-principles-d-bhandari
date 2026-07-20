import csv

with open("module_05/dict.csv","r") as file:
    reader=csv.reader(file)

    first_line=next(reader)
    secondline=next(reader)     
print(first_line)
print(secondline)
 
pirate_dict = {
    "hello": "avast",
    "exuse": "arr",
    "sir": "matey",
    "your": "yer"
}

print(pirate_dict)

with open("module_05/in.txt","r") as file:
           text = file.read()
print(text)


translated_text = " ".join(
    map(lambda word: pirate_dict.get(word, word), text.split())
)

# Write output file
with open("module_05/out.txt", "w") as file:
    file.write(translated_text)

print("Translation complete!")


