## The Microsoft Teams Indico plugin

This is a [Microsoft Teams](https://www.microsoft.com/en/microsoft-teams/group-chat-software) video conferencing plugin for the [Indico](https://getindico.io/).
It allows event organizers to create online meetings at Microsoft Teams platform using the interface of Indico.
It requires a Microsoft Office 365 organization with Teams and Azure services and an application registered at the [Azure Active Directory](https://portal.azure.com/).

To learn more about Indico plugins go here: https://docs.getindico.io/en/stable/plugins/getting_started/

## Installation

1. Clone the repository of the plugin to the directory where your Indico plugins are stored. Preferably rename the repository directory to `vc_ms_teams`.

2. Register an application in Azure Active Directory as described [here](https://github.com/microsoftgraph/python-sample-auth/blob/master/installation.md#configuration).
    + In the step 3. of registration provide your own `Redicrect URI` e.g. `http://localhost:8000/vc_ms_teams_authorized` where `localhost:8000` is the host address and port of your Indico instance.
    + The `client-id` and `client-secret` generated during the registration process will be used in the next step, so remember them.

3. Using the `client-id`, `client-secret` and `Redicrect URI` 
modify the [`config.py`](https://github.com/Azargaz/INZ202021-Indico-MSTeams-Plugin/blob/main/indico_vc_ms_teams/config.py) 
file (this step will be later removed - the plugin will be configured from the Indico interface instead).

4. Install the directory of plugin as Python package using `pip` inside the same `virtualenv` where your Indico instance is installed e.g. `pip install ./vc_ms_teams`.

5. (Optional) Use the `indico setup list-plugins` command to see which plugins are installed. If the plugin has been installed correctly the command should display it 
as `vc_ms_teams`.

6. Add name of the plugin (`vc_ms_teams`) to the `PLUGINS` entry in the configuration of Indico as described 
[here](https://docs.getindico.io/en/stable/installation/plugins/).

## About plugin

The plugin was developed as part of the engineering thesis project titled ["Integration of the Microsoft Teams video conferencing with the Indico service"](https://misio.fis.agh.edu.pl/media/misiofiles/5ca4898e3c4bbe0c25313cf53513d466.pdf).
