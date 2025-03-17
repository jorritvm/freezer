Get-Process | Where-Object { $_.ProcessName -eq "python" } | Stop-Process -Force
reflex run --loglevel debug