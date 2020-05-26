import ROOT

import optparse

parser = optparse.OptionParser()
parser.add_option('-i', type = 'string', dest = 'input', help='input root file name')

(opt, arg) = parser.parse_args()

inFile = ROOT.TFile(opt.input, "READ")

f=open("directories.txt", "w+")

dirlist = inFile.GetListOfKeys()
itera = dirlist.MakeIterator()
key = itera.Next()
dirs=[]

while key:
    dirs.append(key.ReadObj().GetName())
    key = itera.Next()

for i in range(0, len(dirs), 1):
    f.write(dirs[i]+"\n")
    files=[]
    hist_type=[]

    inFile.cd(dirs[i])
    
    fileList = inFile.CurrentDirectory().GetListOfKeys()
    iterFile = fileList.MakeIterator()
    keyFile = iterFile.Next()

    while keyFile:
        files.append(keyFile.GetName())
        hist_type.append(keyFile.GetClassName())

        keyFile = iterFile.Next()

    for j in range(0, len(files), 1):
        f.write("   ['"+files[j]+"','"+hist_type[j]+"']\n")

    inFile.cd('..')

f.close()
