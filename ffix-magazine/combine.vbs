Set objFSO = CreateObject("Scripting.FileSystemObject")
Dim arrFiles
arrFiles = Array("01_head.html", "02_hero.html", "03_overview.html", "04_development.html", "05_world.html", "06_characters.html", "07_story.html", "08_system.html", "09_review.html", "10_gallery.html", "11_footer.html")
Dim outPath
outPath = "C:\Users\Stella\Desktop\ffix-magazine\index.html"
Dim outFile
Set outFile = objFSO.CreateTextFile(outPath, True, True)
Dim i, filePath, inFile
For i = 0 To UBound(arrFiles)
    filePath = "C:\Users\Stella\Desktop\ffix-magazine\parts\" & arrFiles(i)
    If objFSO.FileExists(filePath) Then
        Set inFile = objFSO.OpenTextFile(filePath, 1, False, -1)
        outFile.Write inFile.ReadAll
        inFile.Close
    End If
Next
outFile.Close
MsgBox "Done! Built index.html from " & UBound(arrFiles) + 1 & " parts."
