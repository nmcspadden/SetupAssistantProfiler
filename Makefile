USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make
PACKAGE_VERSION=1.0
TITLE=Outset-SetupAssistant
REVERSE_DOMAIN=org.company.pkg
PAYLOAD= \
		pack-usr-local-outset-everyboot-scripts-setup_assistant_profiler.py \
		pack-library-profiles-SetupAssistant.mobileconfig

l_usr_local_outset_everyboot_scripts: l_usr_local
	@sudo mkdir -p ${WORK_D}/usr/local/outset/everyboot-scripts
	@sudo chown -R root:wheel ${WORK_D}/usr/local/outset/everyboot-scripts
	@sudo chmod -R 755 ${WORK_D}/usr/local/outset/everyboot-scripts

pack-usr-local-outset-everyboot-scripts-%: % l_usr_local_outset_everyboot_scripts
	@sudo ${INSTALL} -m 755 -g wheel -o root "${<}" ${WORK_D}/usr/local/outset/everyboot-scripts

l_library_profiles: l_Library
	@sudo mkdir -p ${WORK_D}/Library/Profiles
	@sudo chown root:wheel ${WORK_D}/Library/Profiles
	@sudo chmod 755 ${WORK_D}/Library/Profiles

pack-library-profiles-%: % l_library_profiles
	@sudo ${INSTALL} -m 755 -g wheel -o root "${<}" ${WORK_D}/Library/Profiles
