#Setup Assistant Profiler

This tool installs a system level profile and a script for use with [Outset](https://github.com/chilcote/outset).  This profile is designed to skip the Setup Assistant that launches every time a new build of OS X is installed, and the script modifies the profile to match the currently installed version and build of OS X.

*NOTE: A makefile is included for use with [Luggage](https://github.com/unixorn/luggage)*

This has been tested on OS X 10.10.3 and 10.10.4. Future Yosemite upgrades should work but retesting may need to take place for OS X 10.11.

##Usage
Open `SetupAssistant.mobileconfig` and modify the `PayloadIdentifier` with your organization's name. If desired, also change the `PayloadUUID` in each payload (use `/usr/bin/uuidgen` to generate new ones).

Place the `SetupAssistant.mobileconfig` profile into `/Library/Profiles/`.

Place the `setup_assistant_profiler.py` script into `/usr/local/outset/everyboot-scripts`.

On boot, the profile will be dynamically modified to match the current OS version and build, and then reinstalled, thus permanently bypassing the Setup Assistant that shows up with new versions.


## Creating a Custom Package with pkgbuild:
Change the identifier below to match your organization:

```
/bin/mkdir -p SetupAssistantProfiler/Library/Profiles
/bin/mkdir -p SetupAssistantProfiler/usr/local/outset/everyboot-scripts
/usr/bin/pkgbuild --root SetupAssistantProfiler --identifier com.github.nmcspadden.outset.setupassistantprofiler --version 1.0 Outset-SetupAssistantProfiler.pkg
```

## Creating a Custom Package with the Luggage:
Install Luggage and open the Makefile. Change the ```REVERSE_DOMAIN``` and if desired the ```PACKAGE_VERSION``` and ```TITLE```

Running the following command in the working directory

```
make pkg
```

The example Makefile will create a "Outset-SetupAssistant-1.0.pkg" package with receipt "org.company.pkg" and version 1.0. It will install `SetupAssistant.mobileconfig` into `/Library/Profiles`, and `setup_assistant_profiler.py` into `/usr/local/outset/everyboot-scripts`.

Each time the machine reboots, setup_assistant_profiler.py will modify `SetupAssistant.mobileconfig` based on the OS major/minor version and reinstall it via the profiles command.
