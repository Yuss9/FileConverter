# rename all file extension in a folder documentToConvert  from cpp to txt
import os
from fpdf import FPDF
from PyPDF2 import PdfMerger


# function count number of txt file il a folder
def countFileInFolder(folder):
    count = 0
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            count += 1
    return count


def convertAllCppToTxt(folder):
    for file in os.listdir(folder):
        if file.endswith(".cpp"):
            os.rename(folder + "/" + file, folder + "/" + file[:-4] + ".txt")
        if file.endswith(".hpp"):
            # rename file
            os.rename(folder + "/" + file, folder +
                      "/" + file[:-4] + "_HPP" + ".txt")
        if file.endswith(".h"):
            os.rename(folder + "/" + file, folder +
                      "/" + file[:-2] + "_H" + ".txt")


def convertTxtToPdf(filename, folder, saveFolder):
    # save FPDF() class into
    # a variable pdf
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=11)

    # path of the file
    pathOfFile = folder + "/" + filename

    # open the text file in read mode
    f = open(pathOfFile, "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='L')

    # new file name with folder
    newFilename = saveFolder + "/" + filename[:-4] + ".pdf"
    pdf.output(newFilename)


def convertAllTxtToPdf(folder, saveFolder):
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            convertTxtToPdf(file, folder, saveFolder)


def MergedPdf(folder, saveFolder):

    pdfs = []

    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            pdfs.append(file)

    value = True

    while value:
        print("Pour changer l'ordre des fichiers, entrez les numéros des fichiers que vous voulez changer de place")
        count = 0

        for pdf in pdfs:
            print("#" + str(count) + " : " + pdf)
            count = count + 1

        reponse = input(
            "Quitter l'application  ou Continuer la modification ? (q/c) : ")

        if reponse == "q":
            value = False
        else:
            print("Entrer le numéro du fichier que vous voulez changer : ")
            file1 = int(input("Entrer le numéro du premier fichier : "))
            file2 = int(input("Entrer le numéro du deuxieme fichier : "))

            # change place in pdfs
            filename1 = pdfs[file1]
            filename2 = pdfs[file2]

            tmp = filename1
            pdfs[file1] = filename2
            pdfs[file2] = tmp

        reponse = input(
            "Quitter l'application  ou Continuer la modification ? (q/c) : ")

        if reponse == "q":
            value = False

    newFilenameofOutput = input("Entrer le nom du fichier de sortie : ")
    print("Merging en cours ....")

    merger = PdfMerger()

    newFilenameofOutput = saveFolder + "/" + newFilenameofOutput + ".pdf"

    for pdf in pdfs:
        merger.append(folder + "/" + pdf)

    merger.write(newFilenameofOutput)
    merger.close()


def deleteAllFileInFolder(folder):
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            os.remove(folder + "/" + file)
        if file.endswith(".pdf"):
            os.remove(folder + "/" + file)


def main():
    folder = "documentToConvert"
    saveFolder = "documentPDF"
    finalFolder = "FinalResult"

    print("Le programme de conversion de fichier .cpp en .pdf commence ...")

    # rename all file extension in a folder documentToConvert  from cpp to txt
    convertAllCppToTxt(folder)

    # count number of txt file il a folder
    count = countFileInFolder(folder)

    print("Nombre de fichier dans documentToConvert : " + str(count))

    # convert all txt file to pdf file
    convertAllTxtToPdf(folder, saveFolder)

    # merge all pdf file
    MergedPdf(saveFolder, finalFolder)

    # delete all file in folder
    deleteAllFileInFolder(saveFolder)
    deleteAllFileInFolder(folder)


main()
