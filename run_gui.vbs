Set WshShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")
scriptPath = WScript.ScriptFullName
scriptDir = FSO.GetParentFolderName(scriptPath)
pythonw = "pythonw"
app = scriptDir & "\organizer_gui.py"
cmd = pythonw & " " & chr(34) & app & chr(34)
WshShell.Run cmd, 0, False
