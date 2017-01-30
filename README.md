# Azure-Django-Template

This is a minimal template to start developing Django apps with Azure Web App service.

Follow [this](https://azure.microsoft.com/en-us/documentation/articles/web-sites-python-configure/) tutorial to get more information.

# Installing wheel Packages

When installing a `wheel` package you may encounter an error saying `vcvarsall.bat file cannot be found.`. To fix this you either need to install
`Visual Studio Build Tools` or provide the `*.whl` package yourself. You probably wouldn't want to install `Visual Studio Build Tools` to Azure Web App.
So the solution would be to download the *.whl file, say `mysqlclient-1.3.7-cp34-none-win32.whl`, to a folder where you configured your git repository and put the
downloaded file into `YOUR_PROJECT_ROOT/wheelhouse/mysqlclient-1.3.7-cp34-none-win32.whl`.

Then you need to update the `requirements.txt` file to use the downloaded wheel file like so:

```
django>=1.9
djangorestframework>=3.4
wheelhouse/mysqlclient-1.3.9-cp35-cp35m-win32.whl
```

Make sure that you are using the latest `pip`.
