$file_name = Read-Host 'Enter file name e.g. prepatch.. etc. '
Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Export-Csv $file_name -notype
