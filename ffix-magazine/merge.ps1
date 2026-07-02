$partsDir = 'C:\Users\Stella\Desktop\ffix-magazine\parts'
$output = 'C:\Users\Stella\Desktop\ffix-magazine\index.html'
$files = Get-ChildItem "$partsDir\*.html" | Sort-Object Name
Write-Host "Found $($files.Count) part files"
$content = ''
foreach ($f in $files) {
    $content += (Get-Content $f.FullName -Raw -Encoding UTF8)
    $content += "`n"
    Write-Host "  + $($f.Name)"
}
[System.IO.File]::WriteAllText($output, $content, [System.Text.UTF8Encoding]::new($true))
$info = Get-Item $output
Write-Host "Size: $($info.Length) bytes"
Write-Host "Chars: $($content.Length)"
Write-Host "DONE"
