#!/usr/bin/python

import sys
import plistlib
import subprocess
    
# Assume that the profile we want to modify is stored in this path:
profilePath = "/Library/Profiles/SetupAssistant.mobileconfig"

try:
    plistContent = plistlib.readPlist(profilePath)
except IOError:
    print >> sys.stderr, "Error: can't read profile at %s" % profilePath
    sys.exit(1)

cmd = ['/usr/bin/sw_vers', '-productVersion']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(productOut, productErr) = proc.communicate()

cmd = ['/usr/bin/sw_vers', '-buildVersion']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(buildOut, buildErr) = proc.communicate()
plistContent['PayloadContent'][0]['PayloadContent']['com.apple.SetupAssistant']['Set-Once'][0]['mcx_preference_settings']['LastSeenCloudProductVersion'] = productOut.strip()
plistContent['PayloadContent'][0]['PayloadContent']['com.apple.SetupAssistant']['Set-Once'][0]['mcx_preference_settings']['LastSeenBuddyBuildVersion'] = buildOut.strip()

try:
    plistlib.writePlist(plistContent, profilePath)
except IOError:
    print >> sys.stderr, "Error: can't write profile at %s" % profilePath
    sys.exit(1)

cmd = ['usr/bin/profiles', '-IvF', profilePath]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(profileOut, profileErr) = proc.communicate()

if profileErr:
    print >> sys.stderr, 'Error: %s' % profileErr
    sys.exit(1)
print profileOut
