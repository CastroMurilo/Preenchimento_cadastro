$exclude = @("venv", "Preenchedor_de_cadastro.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Preenchedor_de_cadastro.zip" -Force