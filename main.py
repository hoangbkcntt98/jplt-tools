from tkinter import *
from convert import *

database = findWord(None,'')
print(database)
root = Tk()
root.title("Gấu Ngáo")
fram = Frame(root)
Label(fram,text='Mún tìm gì:').pack(side=LEFT)
edit = Entry(fram)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()
butt = Button(fram, text='Find') 
butt.pack(side=RIGHT)
fram.pack(side=TOP)
text = Text(root)
# for data in database:

[text.insert('1.0',data[0]+' ('+data[1]+')'+'\n') for data in database]
text.pack(side=BOTTOM)
def find():
	text.tag_remove('found', '1.0', END)

	s = edit.get()
	print(s)
	res = findWord(None,s)
	text.delete('1.0',END)
	[text.insert('1.0',data[0]+' ('+data[1]+')'+'\n') for data in res]
	# find()
	if s:
		idx = '1.0'
		while 1:
			idx = text.search(s, idx, nocase=1,stopindex=END)
			if not idx: break
			lastidx = '%s+%dc' % (idx, len(s))
			text.tag_add('found', idx, lastidx)
			idx = lastidx
			text.tag_config('found',foreground='red')
	edit.focus_set()
butt.config(command=find)
root.mainloop()