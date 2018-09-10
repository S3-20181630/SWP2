import pickle


dbfilename= 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB:", dbfilename)
        return []

    scdb=[]
    try:
        scdb=pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            except:
                pass
        elif parse[0] == 'del':
            for p in scdb:
                try:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
                        break
                except:
                    pass
        elif parse[0] == 'show':
            try:
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except:
                pass
        elif parse[0] == 'quit':
            break
        elif parse[0] =='find':
            for i in scdb:
                try:
                    if i['Name']==parse[1]:
                        print("Age="+str(i['Age'])+"Name="+str(i['Name'])+"Score="+str(i['Score']))
                except:
                    pass
        elif parse[0] =='inc':
            for m in scdb:
                try:
                    if m['Name'] == parse[1]:
                        m['Score']=str(int(m['Score'])+int(parse[2]))
                except:
                    pass
        else:
            print("Invalid command: " + parse[0])

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr+" = "+p[attr], end=' ')
        print()

scoredb=readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

