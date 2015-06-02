#Setup Assistant Profiler

This tool installs a system level profile and a script for use with [Outset](https://github.com/chilcote/outset).

*NOTE: While a generic package is supplied, it is recommended to build your own. A makefile is included for use with [Luggage](https://github.com/unixorn/luggage)*

This has been tested on OS X 10.10.3 and 10.10.4. Future Yosemite upgrades should work but retesting may need to take place for OS X 10.11.

##Configuration
Open `SetupAssistant.mobileconfig` and modify the `PayloadIdentifier` with your organization's name. If desired, also change the `PayloadUUID` in each payload.


## Creating a Custom Package
Install Luggage and open the Makefile. Change the ```REVERSE_DOMAIN``` and if desired the ```PACKAGE_VERSION``` and ```TITLE```

Running the following command in the working directory

```
make pkg
```

The example Makefile will create a "Outset-SetupAssistant-1.0.pkg" package with receipt "org.company.pkg" and version 1.0. It will install `SetupAssistant.mobileconfig` into `/Library/Profiles`, and `setup_assistant_profiler.py` into `/usr/local/outset/everyboot-scripts`.

Each time the machine reboots, setup_assistant_profiler.py will modify `SetupAssistant.mobileconfig` based on the OS major/minor version and reinstall it via the profiles command.
