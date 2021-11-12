#Se recomiendo utilizar de antemano el comando "netsh wlan show profiles" para saber el nombre de su red

#Info del wifi
$i = $true
while ($i -eq ($true)){
    $op = Read-Host -prompt "¿Qué opción desea realizar?`n[1] Mostrar Contraseñas`n[2] Prender/Apagar wifi`n[3] Borrar red`n[4] Salir"
    switch($op){
        1{ 
            show-passwd
        }2{
            on-off
        }3{
            delete
        }4{
            exit
        }default{
            Write-Host "Ingreso un valor inválido"
        }
    }
}