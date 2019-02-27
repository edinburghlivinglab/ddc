---
layout: page
title: "Using DataStore for Data Management"
permalink: "/data_store/"
---
## Overview

The University's DataStore is a central file store intended for researchers. In DDC, we will be using it as a shared place where data that is gathered by teams can be securely shared. 

This is particularly crucial since some of the research data collected by DDC teams is likely to count as personal data. At the same time, team members will need to share with each other the data they have collected. Rather than using a 3rd party cloud service for sharing, you should upload files with your collected data to DataStore. Within the filespace identified below, each team will have its own subfolder, named `team_1`,..., `team_7` as appropriate, where files can be shared amongst the team members.

## Accessing DataStore

In order to access DataStore, you must be on a machine connected to the University network, or connected to the University VPN. The University's Information Services gives [detailed instructions](http://www.ed.ac.uk/information-services/computing/desktop-personal/network-shares) on how to get network access to DataStore, but we'll give you the short version here. 

Once you have established a connection to the DataStore DDC folder, you should be able to upload and download files to a local computer. Please make sure that any computing device that you use for storing files is adequately protected, following the guidelines [Your responsibilities at work](http://www.ed.ac.uk/information-services/computing/desktop-personal/information-security/your-responsibilities).

### Windows

Use the full path to the folder on Windows when mapping the drive:

\\chss.datastore.ed.ac.uk\chss\sps\groups\DDC

You may then be asked for your login credentials. Enter your username in the format  ed\username  and your usual login password.

1. Select **Start** > **Computer** > **Map network drive**.
2. In the **Drive** list, click a drive letter. You can choose any available letter.
3. In the **Folder** box, type the following address for the DDC folder:

```
U:\Datastore\CHSS\sps\groups\DDC
```
4. Authenticate by entering ED\UUN (where 'UUN' is your University login name) and your corresponding password.

If you are using a University supported Windows desktop machine, the main network shares you have access to should automatically be connected.

### Mac OS

1. In the Finder, select **Go** from the menu bar at the top of the desktop, then select **Connect to Server**... 
2. In the **Connect to Server** window, type the following address for the DDC folder: 
```
smb://chss.datastore.ed.ac.uk/chss/sps/groups/DDC
``` 
3. Authenticate by entering your UUN (where 'UUN' is your University login name) and your corresponding password. 

<!--

https://www.wiki.ed.ac.uk/display/ecdfwiki/DataStore+service
https://www.wiki.ed.ac.uk/display/ecdfwiki/DataStore+-+General+Instructions#DataStore-GeneralInstructions-ManagingAccessPermissions



http://www.ed.ac.uk/records-management/records-management/staff-guidance/technical-guidance/storage-standards
-->

 
