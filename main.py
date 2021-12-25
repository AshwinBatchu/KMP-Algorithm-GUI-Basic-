from tkinter import *
root = Tk()
root.title("KMP ALGORITHM")
root.geometry("500x500")
label1=Label(root,text="Enter Text Here")
label1.pack()
Text2=Entry(root,width=45,borderwidth=3)
Text2.pack()
label2=Label(root,text="Enter Pattern Here")
label2.pack()
Text1=Entry(root,width=45,borderwidth=3)
Text1.pack()

def KMPSearch(pat, txt):
	M = len(pat)
	N = len(txt)


	lps = [0]*M
	j = 0


	computeLPSArray(pat, M, lps)

	i = 0
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			a = "Found pattern at index " + str(i - j)
			label41=Label(root , text = a)
			label41.pack()
			j = lps[j-1]


		elif i < N and pat[j] != txt[i]:

			if j != 0:
				j = lps[j-1]
			else:
				i += 1

def computeLPSArray(pat, M, lps):
	len = 0
	lps[0]
	i = 1


	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			if len != 0:
				len = lps[len-1]

			else:
				lps[i] = 0
				i += 1



def function():
	KMPSearch(str(Text1.get()),str(Text2.get()))

button = Button(root, text="Start Algorithm",command = function, padx=20, pady=20)
button.pack()

root.mainloop()

