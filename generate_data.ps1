$data = 
    "123.456`r`n",
    "2`r`n",
    "7 5`r`n",
    "456.789`r`n",
    "2.357 6.819`r`n",
    "88010000`r`n",
    "33`r`n",
    "5 5 5 5 5`r`n",
    "6 7 8 9 8 10`r`n"
$in_file = "1.in"
$out_file = "1.out"
$dir = "test\"

$path = ".\" + $dir
if (!(test-path $path)) {
    New-Item -ItemType Directory -Force -Path $path
}

for ($i = 1; $i -le $data.count; $i++) {
    $p = $path + $i.ToString() + "\"
    New-Item -ItemType Directory -Force -Path $p
    New-Item -ItemType File -Force -Path $p -Name $in_file -Value $data[$i-1]
    
    $exe_file = ".\" + $i.ToString() + ".exe"
    if(test-path $exe_file){
        get-content ($p+$in_file) | &$exe_file > ($p+"tmp")
        Get-Content ($p+"tmp") -Encoding Unicode | Set-Content -Encoding UTF8 ($p+$out_file)
        Remove-Item ($p+"tmp")
    }
}