Dim fso, outFile, parts, f, ts, content
Set fso = CreateObject("Scripting.FileSystemObject")
parts = Array("f01_head.html", "02_overview.html", "03_development.html", "04_world.html", "05_characters_a.html", "05b_characters_b.html", "06_story_a.html", "06b_story_b.html", "07_systems.html", "07b_systems_b.html", "08_review.html", "09_gallery.html", "f99_footer.html")
Set outFile = fso.CreateTextFile("C:\Users\Stella\Desktop\ffix-magazine\index.html", True, True)
For Each f In parts
    Set ts = fso.OpenTextFile("C:\Users\Stella\Desktop\ffix-magazine\parts\" & f, 1, False, -1)
    content = ts.ReadAll
    outFile.Write content
    outFile.Write vbCrLf
    ts.Close
    WScript.Echo "  + " & f
Next
outFile.Close
WScript.Echo "DONE"
