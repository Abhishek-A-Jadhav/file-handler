from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.core.window import Window
import os
import shutil


Window.size = (1920, 1080)
Window.clearcolor = (0.1, 0.1, 0.1, 1)

#-------------------------------------------------
# Start Window
class Window1(Screen):
    pass


#-------------------------------------------------
# Home Window
class Window2(Screen):
    pass


#-------------------------------------------------
# Copy Window
class Window3(Screen):

    def autoSelection(self):

        global srcPath, fileList, dummy1, dummy2, addManList, removeManList, finalSelectionList, num1
        dummy1 = []
        dummy2 = []
        addManList = []
        removeManList = []
        fileList = []
        filterFileList = []
        extFileList = []

        srcPath = self.ids.workPathInput.text

        if len(srcPath) == 0:
            srcPath = "/"

        if "/" != srcPath[-1]:
            srcPath += "/"

        dirFileList = os.listdir(srcPath)

        for file in dirFileList:
            if "." in file and "." not in file[0]:
                fileList.append(file)

        for file in fileList:
            if self.ids.filter.text in file:
                filterFileList.append(file)

        for file in filterFileList:
            ext = file.split(".")[-1]
            if self.ids.ext.text in ext:
                extFileList.append(file)

        finalSelectionList = extFileList.copy()
        num1 = len(finalSelectionList)

        autoFilesString = "\n\n".join(finalSelectionList)
        self.ids.selectedFileList.text = autoFilesString

    def addManually(self):
        if self.ids.addMan.text in fileList:
            if self.ids.addMan.text not in finalSelectionList:
                dummy1.append(self.ids.addMan.text)
                self.ids.addMan.text = ""

        for file in dummy1:
            if file not in addManList:
                addManList.append(file)

        manAddFilesString = "\n\n".join(addManList)
        self.ids.manFileList.text = manAddFilesString


    def removeManually(self):
        if self.ids.removeMan.text in finalSelectionList:
            finalSelectionList.remove(self.ids.removeMan.text)
            self.ids.removeMan.text = ""
        if self.ids.removeMan.text in addManList:
            addManList.remove(self.ids.removeMan.text)
            self.ids.removeMan.text = ""

        num2 = len(finalSelectionList)

        if num1 > num2:
            autoFilesString = "\n\n".join(finalSelectionList)
            self.ids.selectedFileList.text = autoFilesString

        manRemoveFilesString = "\n\n".join(addManList)
        self.ids.manFileList.text = manRemoveFilesString


    def compute(self):
        global computeList
        computeList = []
        dummy2 = finalSelectionList + addManList

        for file in dummy2:
            if file not in computeList:
                computeList.append(file)

        computeFilesString = "\n\n".join(computeList)
        self.ids.finalList.text = computeFilesString

        self.ids.totalFiles.text = str(len(computeList))

    def copy(self):
        global destPath
        destPath = self.ids.destPathInput.text

        self.ids.status.text = "In Progress"
        i = 0
        for file in computeList:
            shutil.copyfile(srcPath + file, destPath + file)
            i += 1
        self.ids.success.text = "Successfully copied " + str(i) + " / " + str(len(computeList)) + " files"

    def reset(self):
        self.ids.workPathInput.text = ""
        self.ids.filter.text = ""
        self.ids.ext.text = ""
        self.ids.selectedFileList.text = ""
        self.ids.manFileList.text = ""
        self.ids.finalList.text = ""
        self.ids.addMan.text = ""
        self.ids.removeMan.text = ""
        self.ids.destPathInput.text = ""
        self.ids.totalFiles.text = ""
        self.ids.status.text = ""
        self.ids.success.text = ""
        srcPath = self.ids.workPathInput.text
        fileList = []
        finalSelectionList = []
        dummy1 = []
        dummy2 = []
        addManList = []
        removeManList = []
        computeList = []
        num1 = len(finalSelectionList)
        destPath = self.ids.destPathInput.text


#-------------------------------------------------
# Move Window
class Window4(Screen):

    def autoSelection(self):

        global srcPath, fileList, dummy1, dummy2, addManList, removeManList, finalSelectionList, num1
        dummy1 = []
        dummy2 = []
        addManList = []
        removeManList = []
        fileList = []
        filterFileList = []
        extFileList = []

        srcPath = self.ids.workPathInput.text

        if len(srcPath) == 0:
            srcPath = "/"

        if "/" != srcPath[-1]:
            srcPath += "/"

        dirFileList = os.listdir(srcPath)

        for file in dirFileList:
            if "." in file and "." not in file[0]:
                fileList.append(file)

        for file in fileList:
            if self.ids.filter.text in file:
                filterFileList.append(file)

        for file in filterFileList:
            ext = file.split(".")[-1]
            if self.ids.ext.text in ext:
                extFileList.append(file)

        finalSelectionList = extFileList.copy()
        num1 = len(finalSelectionList)

        autoFilesString = "\n\n".join(finalSelectionList)
        self.ids.selectedFileList.text = autoFilesString

    def addManually(self):
        if self.ids.addMan.text in fileList:
            if self.ids.addMan.text not in finalSelectionList:
                dummy1.append(self.ids.addMan.text)
                self.ids.addMan.text = ""

        for file in dummy1:
            if file not in addManList:
                addManList.append(file)

        manAddFilesString = "\n\n".join(addManList)
        self.ids.manFileList.text = manAddFilesString


    def removeManually(self):
        if self.ids.removeMan.text in finalSelectionList:
            finalSelectionList.remove(self.ids.removeMan.text)
            self.ids.removeMan.text = ""
        if self.ids.removeMan.text in addManList:
            addManList.remove(self.ids.removeMan.text)
            self.ids.removeMan.text = ""

        num2 = len(finalSelectionList)

        if num1 > num2:
            autoFilesString = "\n\n".join(finalSelectionList)
            self.ids.selectedFileList.text = autoFilesString

        manRemoveFilesString = "\n\n".join(addManList)
        self.ids.manFileList.text = manRemoveFilesString


    def compute(self):
        global computeList
        computeList = []
        dummy2 = finalSelectionList + addManList

        for file in dummy2:
            if file not in computeList:
                computeList.append(file)

        computeFilesString = "\n\n".join(computeList)
        self.ids.finalList.text = computeFilesString

        self.ids.totalFiles.text = str(len(computeList))

    def move(self):
        global destPath
        destPath = self.ids.destPathInput.text

        self.ids.status.text = "In Progress"
        i = 0
        for file in computeList:
            shutil.move(srcPath + file, destPath + file)
            i += 1
        self.ids.success.text = "Successfully movied " + str(i) + " / " + str(len(computeList)) + " files"

    def reset(self):
        self.ids.workPathInput.text = ""
        self.ids.filter.text = ""
        self.ids.ext.text = ""
        self.ids.selectedFileList.text = ""
        self.ids.manFileList.text = ""
        self.ids.finalList.text = ""
        self.ids.addMan.text = ""
        self.ids.removeMan.text = ""
        self.ids.destPathInput.text = ""
        self.ids.totalFiles.text = ""
        self.ids.status.text = ""
        self.ids.success.text = ""
        srcPath = self.ids.workPathInput.text
        fileList = []
        finalSelectionList = []
        dummy1 = []
        dummy2 = []
        addManList = []
        removeManList = []
        computeList = []
        num1 = len(finalSelectionList)
        destPath = self.ids.destPathInput.text


#-------------------------------------------------
# Rename Window
class Window5(Screen):

    def autoSelection(self):

        global srcPath, finalSelectionList, fileList
        fileList = []
        filterFileList = []
        extFileList = []

        srcPath = self.ids.workPathInput.text

        if len(srcPath) == 0:
            srcPath = "/"

        if "/" != srcPath[-1]:
            srcPath += "/"

        dirFileList = os.listdir(srcPath)

        for file in dirFileList:
            if "." in file and "." not in file[0]:
                fileList.append(file)

        for file in fileList:
            if self.ids.filter.text in file:
                filterFileList.append(file)

        for file in filterFileList:
            ext = file.split(".")[-1]
            if self.ids.ext.text in ext:
                extFileList.append(file)

        finalSelectionList = extFileList.copy()

        autoFilesString = "\n\n".join(finalSelectionList)
        self.ids.selectedFileList.text = autoFilesString

    def eg(self):

        pattern = self.ids.pattern.text
        prefix = self.ids.prefix.text
        suffix = self.ids.suffix.text

        if len(pattern) > 0:
            self.ids.eg.text = prefix + pattern + "001" + suffix + ".ext"
        else:
            self.ids.eg.text = prefix + suffix + ".ext"

    def preview(self):

        previewList = []

        pattern = self.ids.pattern.text
        prefix = self.ids.prefix.text
        suffix = self.ids.suffix.text

        if len(pattern) > 0:
            i = 1
            for file in finalSelectionList:
                ext = file.split(".")[-1]

                if i < 10:
                    newFile = prefix + pattern + "00" + str(i) + suffix + "." + ext
                elif i < 100:
                    newFile = prefix + pattern + "0" + str(i) + suffix + "." + ext
                else:
                    newFile = prefix + pattern + str(i) + suffix + "." + ext

                previewList.append(newFile)
                i+=1

        else:
            for file in finalSelectionList:
                ext = file.split(".")[-1]
                oldName = file.split(".")[:-1]
                oldName = "".join(oldName)

                newFile = prefix + oldName + suffix + "." + ext

                previewList.append(newFile)

        self.ids.totalFiles.text = str(len(finalSelectionList))

        previewListString = "\n\n".join(previewList)
        self.ids.preview.text = previewListString


    def generateName(self):

        pattern = self.ids.pattern.text
        prefix = self.ids.prefix.text
        suffix = self.ids.suffix.text

        if len(pattern) > 0:
            i = 1
            for file in finalSelectionList:
                ext = file.split(".")[-1]

                if i < 10:
                    newFile = prefix + pattern + "00" + str(i) + suffix + "." + ext
                elif i < 100:
                    newFile = prefix + pattern + "0" + str(i) + suffix + "." + ext
                else:
                    newFile = prefix + pattern + str(i) + suffix + "." + ext

                os.rename(srcPath + file, srcPath + newFile)
                i += 1

        else:
            i = 1
            for file in finalSelectionList:
                ext = file.split(".")[-1]
                oldName = file.split(".")[:-1]
                oldName = "".join(oldName)

                newFile = prefix + oldName + suffix + "." + ext

                os.rename(srcPath + file, srcPath + newFile)
                i += 1

        self.ids.totalFiles.text = str(len(finalSelectionList))
        self.ids.success.text = "Successfully renamed " + str(i - 1) + " / " + str(len(finalSelectionList)) + " files."

    def reset(self):

        srcPath = self.ids.workPathInput.text
        self.ids.workPathInput.text = ""
        self.ids.filter.text = ""
        self.ids.ext.text = ""
        self.ids.selectedFileList.text = ""
        self.ids.preview.text = ""
        self.ids.pattern.text = ""
        self.ids.prefix.text = ""
        self.ids.suffix.text = ""
        self.ids.totalFiles.text = ""
        self.ids.success.text = ""
        self.ids.eg.text = ""
        fileList = []
        finalSelectionList = []


#-------------------------------------------------
# Delete Window
class Window6(Screen):

    def autoSelection(self):

        global srcPath, fileList, dummy1, dummy2, addManList, removeManList, finalSelectionList, num1
        dummy1 = []
        dummy2 = []
        addManList = []
        removeManList = []
        fileList = []
        filterFileList = []
        extFileList = []

        srcPath = self.ids.workPathInput.text

        if len(srcPath) == 0:
            srcPath = "/"

        if "/" != srcPath[-1]:
            srcPath += "/"

        dirFileList = os.listdir(srcPath)

        for file in dirFileList:
            if "." in file and "." not in file[0]:
                fileList.append(file)

        for file in fileList:
            if self.ids.filter.text in file:
                filterFileList.append(file)

        for file in filterFileList:
            ext = file.split(".")[-1]
            if self.ids.ext.text in ext:
                extFileList.append(file)

        finalSelectionList = extFileList.copy()
        num1 = len(finalSelectionList)

        autoFilesString = "\n\n".join(finalSelectionList)
        self.ids.selectedFileList.text = autoFilesString

    def addManually(self):
        if self.ids.addMan.text in fileList:
            if self.ids.addMan.text not in finalSelectionList:
                dummy1.append(self.ids.addMan.text)
                self.ids.addMan.text = ""

        for file in dummy1:
            if file not in addManList:
                addManList.append(file)

        manAddFilesString = "\n\n".join(addManList)
        self.ids.manFileList.text = manAddFilesString


    def removeManually(self):
        if self.ids.removeMan.text in finalSelectionList:
            finalSelectionList.remove(self.ids.removeMan.text)
            self.ids.removeMan.text = ""
        if self.ids.removeMan.text in addManList:
            addManList.remove(self.ids.removeMan.text)
            self.ids.removeMan.text = ""

        num2 = len(finalSelectionList)

        if num1 > num2:
            autoFilesString = "\n\n".join(finalSelectionList)
            self.ids.selectedFileList.text = autoFilesString

        manRemoveFilesString = "\n\n".join(addManList)
        self.ids.manFileList.text = manRemoveFilesString


    def compute(self):
        global computeList
        computeList = []
        dummy2 = finalSelectionList + addManList

        for file in dummy2:
            if file not in computeList:
                computeList.append(file)

        computeFilesString = "\n\n".join(computeList)
        self.ids.finalList.text = computeFilesString

        self.ids.totalFiles.text = str(len(computeList))

    def delete(self):

        self.ids.status.text = "In Progress"
        i = 0
        for file in computeList:
            os.remove(srcPath + file)
            i += 1
        self.ids.success.text = "Successfully deleted " + str(i) + " / " + str(len(computeList)) + " files"

    def reset(self):
        self.ids.workPathInput.text = ""
        self.ids.filter.text = ""
        self.ids.ext.text = ""
        self.ids.selectedFileList.text = ""
        self.ids.manFileList.text = ""
        self.ids.finalList.text = ""
        self.ids.addMan.text = ""
        self.ids.removeMan.text = ""
        self.ids.totalFiles.text = ""
        self.ids.status.text = ""
        self.ids.success.text = ""
        srcPath = self.ids.workPathInput.text
        fileList = []
        finalSelectionList = []
        dummy1 = []
        dummy2 = []
        addManList = []
        removeManList = []
        computeList = []
        num1 = len(finalSelectionList)


#-------------------------------------------------
# Copy Window Info
class Window7(Screen):
    pass


#-------------------------------------------------
# Move Window Info
class Window8(Screen):
    pass


#-------------------------------------------------
# Rename Window Info
class Window9(Screen):
    pass


#-------------------------------------------------
# Delete Window Info
class Window10(Screen):
    pass


#-------------------------------------------------
# Auto-Sort Window
class Window11(Screen):

    def autoSort(self):
        # ------------------------v~Add New Extensions Here~v-------------------------

        doc = ["pdf", "doc", "docx", "ppt", "pptx", "xls", "xlsx", "odt"]
        img = ["png", "jpg", "gif", "tiff"]
        vid = ["mp4", "m4v", "avi", "mkv"]
        setup = ["deb", "exe", "AppImage"]
        comp = ["rar", "zip", "flatpakref", "7z", "gz", "xz", "whl", "appx"]

        # ---------------------v~Add New Folder Categories Here~v---------------------

        downDest = self.ids.destPath.text

        if "/" != downDest[-1]:
            downDest += "/"

        foldersReq = ["Documents", "Pictures", "Videos", "Setups", "Compressed", "Misc"]
        foldersAvail = []
        dirList = os.listdir(downDest)

        for folder in dirList:
            if "." not in folder:
                foldersAvail.append(folder)

        for folder in foldersReq:
            if folder not in foldersAvail:
                os.mkdir(downDest + folder)

        docDest = downDest + foldersReq[0]
        imgDest = downDest + foldersReq[1]
        vidDest = downDest + foldersReq[2]
        setupDest = downDest + foldersReq[3]
        compDest = downDest + foldersReq[4]
        miscDest = downDest + foldersReq[5]

        # --------------------v~Add New List For Renaming Here~v-----------------------

        docList = os.listdir(docDest)
        imgList = os.listdir(imgDest)
        vidList = os.listdir(vidDest)
        setupList = os.listdir(setupDest)
        compList = os.listdir(miscDest)

        combination = docList + imgList + vidList + setupList + compList

        # ----------------------------------------------------------------------------

        for file in dirList:

            if "." in file:

                if file in combination:
                    name = file.split(".")[:-1]
                    separator = ""
                    newName = separator.join(name) + "1" + "." + file.split(".")[-1]
                    os.rename(downDest + "/" + file, downDest + "/" + newName)

                    extList = newName.split(".")[-1]

                    if extList in doc:
                        shutil.move(downDest + "/" + newName, docDest)
                    elif extList in img:
                        shutil.move(downDest + "/" + newName, imgDest)
                    elif extList in vid:
                        shutil.move(downDest + "/" + newName, vidDest)
                    elif extList in setup:
                        shutil.move(downDest + "/" + newName, setupDest)
                    elif extList in comp:
                        shutil.move(downDest + "/" + newName, compDest)
                    else:
                        shutil.move(downDest + "/" + newName, miscDest)

                else:

                    extList = file.split(".")[-1]

                    if extList in doc:
                        shutil.move(downDest + "/" + file, docDest)
                    elif extList in img:
                        shutil.move(downDest + "/" + file, imgDest)
                    elif extList in vid:
                        shutil.move(downDest + "/" + file, vidDest)
                    elif extList in setup:
                        shutil.move(downDest + "/" + file, setupDest)
                    elif extList in comp:
                        shutil.move(downDest + "/" + file, compDest)
                    else:
                        shutil.move(downDest + "/" + file, miscDest)

        self.ids.status.text = "Done"

    def reset(self):
        self.ids.destPath.text = ""
        self.ids.status.text = ""


#-------------------------------------------------
class ScreenManagement(ScreenManager):
    pass


windows = Builder.load_file("ui.kv")


class FileHandlingApp(App):
    def build(self):
        return windows


if __name__ == "__main__":
    FileHandlingApp().run()