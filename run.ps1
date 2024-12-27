# Get file path as argument
$filePath = $args[0]

# Show run time in only milliseconds
$time = Measure-Command { python $filePath | Out-Default } | Select-Object -ExpandProperty TotalMilliseconds 
Write-Host "Execution time: $time ms"