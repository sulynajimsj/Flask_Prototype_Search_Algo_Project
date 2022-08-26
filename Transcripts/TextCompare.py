import string

class TextSplit:
    def __init__(self, txtfile):
        self.txtfile = txtfile
    def getWords (self):
        words = []
        with open (self.txtfile) as f:
            fileString = f.read().translate(str.maketrans('', '', string.punctuation))
            words = fileString.lower().split()
            print(words)
        return words

# split = TextSplit(r"C:\Users\james\Documents\app\textCompare\demotext.txt")
# print(split.split())

class textCompare:
    def __init__(self, txt1, txt2):
        txt1 = TextSplit(txt1)
        txt2 = TextSplit(txt2)
        self.split1 = txt1
        self.split2 = txt2
    def compare (self):
        lst1 = self.split1.getWords()
        lst2 = self.split2.getWords()
        list1 = lst1 
        list2 = lst2 
        
        for i in range (len(list2)-1-len(list1)):
            if (list1[1] == list2[i]):
            

                if (list1[0] != list2[i-1] and list1[2] != list2[i+1]):
                    continue
                else:
                    similar = 0
                    for j in range (len(list1)-1):
                        if (list1[j] == list2[i-1+j]):
                            similar += 1
                    if (similar/len(list1)>= 0.6):
                        return (True)
        return(False)

