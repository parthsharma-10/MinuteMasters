@echo off
echo ========================================================
echo MinuteMasters - Milestone 2 PDF Generator
echo ========================================================
echo Converting HTML documents to official PDFs using Microsoft Edge...

set EDGE="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not exist %EDGE% set EDGE="C:\Program Files\Microsoft\Edge\Application\msedge.exe"

%EDGE% --headless --disable-gpu --run-all-compositor-stages-before-draw --print-to-pdf="%~dp0docs\M2_C12_TranscriptToTasks.pdf" "%~dp0docs\M2_C12_TranscriptToTasks.html"
%EDGE% --headless --disable-gpu --run-all-compositor-stages-before-draw --print-to-pdf="%~dp0docs\MinuteMasters_BMC.pdf" "%~dp0docs\MinuteMasters_BMC.html"

echo.
echo Verification:
if exist "%~dp0docs\M2_C12_TranscriptToTasks.pdf" (
    echo [SUCCESS] Created docs\M2_C12_TranscriptToTasks.pdf
) else (
    echo [NOTE] Please open docs\M2_C12_TranscriptToTasks.html in your browser and press Ctrl+P to save as PDF.
)

if exist "%~dp0docs\MinuteMasters_BMC.pdf" (
    echo [SUCCESS] Created docs\MinuteMasters_BMC.pdf
) else (
    echo [NOTE] Please open docs\MinuteMasters_BMC.html in your browser and press Ctrl+P to save as PDF.
)

echo.
echo Complete!
pause
