# ...new file...
param(
    [string]$Message = "Include library URLs in pages.urls"
)

# Ensure script runs from the repository root
Set-Location $PSScriptRoot

git add -A

$changes = git status --porcelain
if (-not $changes) {
    Write-Host "No changes to commit."
    exit 0
}

git commit -m $Message

if ($LASTEXITCODE -eq 0) {
    Write-Host "Committed successfully."
} else {
    Write-Host "Commit failed. Inspect git output above."
}
