from CreateDocument import CreateDocument
from ExecuteProgram import ExecuteProgram
from GetFiles import GetFiles
from ReadFile import ReadFile
import argparse, sys
from pyautogui import screenshot
from datetime import datetime
from time import sleep


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir",help="Fetch files from given directory & execute")
    parser.add_argument("-t", "--template", help="Provide template file for the document")
    parser.add_argument("-s", "--subject", help="provide subject name override in document")
    parser.add_argument("-n", "--name", help="name for the output doc file")
    parser.add_argument("-pn", "--pno", help="Practical No ")
    args = parser.parse_args()

    if not args.dir :
        print("directory should be specified")
        sys.exit(0)

    if not args.template:
        args.template = "template.docx"

    if not args.pno:
        args.pno = 1
    if not args.name :
        args.name = "AnilSoni-" + str(datetime.now().strftime("%d-%m-%y %H-%M-%S")) + ".docx"

    #print(args.dir, args.template, args.name)
    files = GetFiles( args.dir )
    path,list_files = files.get_file()
    path += "\\"
    #print("{}, {}".format(path,list_files))
    #execute all files present in directory
    execute_program = ExecuteProgram()
    doc = CreateDocument(template= args.template, subject= args.subject, practicalno = args.pno)
    read_file_source = ReadFile()
    pic_name=""
    for pythonfile in list_files:
        #print("Executing {} ".format(pythonfile))
        execute_program.execute(path=args.dir,filename=pythonfile)    
        #execute_program.wait()
        sleep(5)
        pic = screenshot()
        pic_name = pythonfile[0:len(pythonfile)-3] + ".png"
        pic.save(pic_name)
        #print("screenshot saved with name {}".format(pic_name))
        execute_program.terminate()
        source = read_file_source.read_file(filename = args.dir+pythonfile)
        #print(args.dir+pythonfile)
        source = "".join(source)
        print(execute_program.get_aim())
        doc.set_aim_source_output(aim=execute_program.get_aim(), source=source, output= pic_name)
        #print("terminating cmd")
        
        sleep(2)
        
        #print("Terminating the process")

    doc.save_doc(args.name)
if __name__ == '__main__':
    main()
