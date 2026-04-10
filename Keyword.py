from docx import Document
doc = Document("book.docx")
keyword=input("Enter a keyword: ")
keyword=keyword.strip().lower()
match=0
for p in doc.paragraphs:
  text=p.text.strip().lower()
  if keyword in text:
    print(p.text)
    match+=1
print("total matches:", match)    
if match == 0:
  print("No matches found")

  
    