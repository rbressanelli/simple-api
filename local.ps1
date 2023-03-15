Clear-Host
if ( -not ($env:VIRTUAL_ENV_PROMPT -eq 'venv')) {
    Write-host '      --> Ativando ambiente virtual <--' -ForegroundColor red
    .\venv\Scripts\activate 
}
Write-host "Valor atual da variavel de ambiente --> $env:DEV_AMBIENTE" -ForegroundColor green
$env:DEV_AMBIENTE = 'local'
Write-host "Iniciando o Django na porta 8080" -ForegroundColor yellow
Write-Output ''


python manage.py runserver 8080
