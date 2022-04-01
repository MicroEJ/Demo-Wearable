SET BACK=%~dp0%
cd ..\packaging\content
rmdir /s/q documentation
mkdir documentation
cd %BACK%
Xcopy /E /I  _build\html  ..\packaging\content\documentation