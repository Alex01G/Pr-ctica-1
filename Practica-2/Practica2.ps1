function nombre {
  param ([string]$nombre)
  Write-Host "Tu nombre es $nombre"
}

$valor=2
if ($valor -eq 2) {echo "El valor es 2"}

$val=0
while($val -ne 10) { $val++ ; Write-Host $val }
