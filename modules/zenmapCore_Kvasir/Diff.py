#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ***********************IMPORTANT NMAP LICENSE TERMS************************
# *                                                                         *
# * The Nmap Security Scanner is (C) 1996-2013 Insecure.Com LLC. Nmap is    *
# * also a registered trademark of Insecure.Com LLC.  This program is free  *
# * software; you may redistribute and/or modify it under the terms of the  *
# * GNU General Public License as published by the Free Software            *
# * Foundation; Version 2 ("GPL"), BUT ONLY WITH ALL OF THE CLARIFICATIONS  *
# * AND EXCEPTIONS DESCRIBED HEREIN.  This guarantees your right to use,    *
# * modify, and redistribute this software under certain conditions.  If    *
# * you wish to embed Nmap technology into proprietary software, we sell    *
# * alternative licenses (contact sales@nmap.com).  Dozens of software      *
# * vendors already license Nmap technology such as host discovery, port    *
# * scanning, OS detection, version detection, and the Nmap Scripting       *
# * Engine.                                                                 *
# *                                                                         *
# * Note that the GPL places important restrictions on "derivative works",  *
# * yet it does not provide a detailed definition of that term.  To avoid   *
# * misunderstandings, we interpret that term as broadly as copyright law   *
# * allows.  For example, we consider an application to constitute a        *
# * derivative work for the purpose of this license if it does any of the   *
# * following with any software or content covered by this license          *
# * ("Covered Software"):                                                   *
# *                                                                         *
# * o Integrates source code from Covered Software.                         *
# *                                                                         *
# * o Reads or includes copyrighted data files, such as Nmap's nmap-os-db   *
# * or nmap-service-probes.                                                 *
# *                                                                         *
# * o Is designed specifically to execute Covered Software and parse the    *
# * results (as opposed to typical shell or execution-menu apps, which will *
# * execute anything you tell them to).                                     *
# *                                                                         *
# * o Includes Covered Software in a proprietary executable installer.  The *
# * installers produced by InstallShield are an example of this.  Including *
# * Nmap with other software in compressed or archival form does not        *
# * trigger this provision, provided appropriate open source decompression  *
# * or de-archiving software is widely available for no charge.  For the    *
# * purposes of this license, an installer is considered to include Covered *
# * Software even if it actually retrieves a copy of Covered Software from  *
# * another source during runtime (such as by downloading it from the       *
# * Internet).                                                              *
# *                                                                         *
# * o Links (statically or dynamically) to a library which does any of the  *
# * above.                                                                  *
# *                                                                         *
# * o Executes a helper program, module, or script to do any of the above.  *
# *                                                                         *
# * This list is not exclusive, but is meant to clarify our interpretation  *
# * of derived works with some common examples.  Other people may interpret *
# * the plain GPL differently, so we consider this a special exception to   *
# * the GPL that we apply to Covered Software.  Works which meet any of     *
# * these conditions must conform to all of the terms of this license,      *
# * particularly including the GPL Section 3 requirements of providing      *
# * source code and allowing free redistribution of the work as a whole.    *
# *                                                                         *
# * As another special exception to the GPL terms, Insecure.Com LLC grants  *
# * permission to link the code of this program with any version of the     *
# * OpenSSL library which is distributed under a license identical to that  *
# * listed in the included docs/licenses/OpenSSL.txt file, and distribute   *
# * linked combinations including the two.                                  *
# *                                                                         *
# * Any redistribution of Covered Software, including any derived works,    *
# * must obey and carry forward all of the terms of this license, including *
# * obeying all GPL rules and restrictions.  For example, source code of    *
# * the whole work must be provided and free redistribution must be         *
# * allowed.  All GPL references to "this License", are to be treated as    *
# * including the terms and conditions of this license text as well.       *
# *                                                                         *
# * Because this license imposes special exceptions to the GPL, Covered     *
# * Work may not be combined (even as part of a larger work) with plain GPL *
# * software.  The terms, conditions, and exceptions of this license must   *
# * be included as well.  This license is incompatible with some other open *
# * source licenses as well.  In some cases we can relicense portions of    *
# * Nmap or grant special permissions to use it in other open source        *
# * software.  Please contact fyodor@nmap.org with any such requests.       *
# * Similarly, we don't incorporate incompatible open source software into  *
# * Covered Software without special permission from the copyright holders. *
# *                                                                         *
# * If you have any questions about the licensing restrictions on using     *
# * Nmap in other works, are happy to help.  As mentioned above, we also    *
# * offer alternative license to integrate Nmap into proprietary            *
# * applications and appliances.  These contracts have been sold to dozens  *
# * of software vendors, and generally include a perpetual license as well  *
# * as providing for priority support and updates.  They also fund the      *
# * continued development of Nmap.  Please email sales@nmap.com for further *
# * information.                                                            *
# *                                                                         *
# * If you have received a written license agreement or contract for        *
# * Covered Software stating terms other than these, you may choose to use  *
# * and redistribute Covered Software under those terms instead of these.   *
# *                                                                         *
# * Source is provided to this software because we believe users have a     *
# * right to know exactly what a program is going to do before they run it. *
# * This also allows you to audit the software for security holes (none     *
# * have been found so far).                                                *
# *                                                                         *
# * Source code also allows you to port Nmap to new platforms, fix bugs,    *
# * and add new features.  You are highly encouraged to send your changes   *
# * to the dev@nmap.org mailing list for possible incorporation into the    *
# * main distribution.  By sending these changes to Fyodor or one of the    *
# * Insecure.Org development mailing lists, or checking them into the Nmap  *
# * source code repository, it is understood (unless you specify otherwise) *
# * that you are offering the Nmap Project (Insecure.Com LLC) the           *
# * unlimited, non-exclusive right to reuse, modify, and relicense the      *
# * code.  Nmap will always be available Open Source, but this is important *
# * because the inability to relicense code has caused devastating problems *
# * for other Free Software projects (such as KDE and NASM).  We also       *
# * occasionally relicense the code to third parties as discussed above.    *
# * If you wish to specify special license conditions of your               *
# * contributions, just say so when you send them.                          *
# *                                                                         *
# * This program is distributed in the hope that it will be useful, but     *
# * WITHOUT ANY WARRANTY; without even the implied warranty of              *
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the Nmap      *
# * license file for more details (it's in a COPYING file included with     *
# * Nmap, and also available from https://svn.nmap.org/nmap/COPYING         *
# *                                                                         *
# ***************************************************************************/

import datetime
import os
import subprocess
import sys
import tempfile
import xml.sax

from zenmapCore.Name import APP_NAME
from zenmapCore.NmapParser import NmapParserSAX
from zenmapCore.UmitConf import PathsConfig
from zenmapCore.UmitLogging import log
import zenmapCore.Paths

# The [paths] configuration from zenmap.conf, used to get ndiff_command_path.
paths_config = PathsConfig()

class NdiffParseException(Exception):
    pass

def get_path():
    """Return a value for the PATH environment variable that is appropriate
    for the current platform. It will be the PATH from the environment plus
    possibly some platform-specific directories."""
    path_env = os.getenv("PATH")
    if path_env is None:
        search_paths = []
    else:
        search_paths = path_env.split(os.pathsep)
    for path in zenmapCore.Paths.get_extra_executable_search_paths():
        if path not in search_paths:
            search_paths.append(path)
    return os.pathsep.join(search_paths)

class NdiffCommand(subprocess.Popen):
    def __init__(self, filename_a, filename_b, temporary_filenames = []):
        self.temporary_filenames = temporary_filenames

        search_paths = get_path()
        env = dict(os.environ)
        env["PATH"] = search_paths
        if getattr(sys, "frozen", None) == "macosx_app":
            # These variables are set by py2app, but they can interfere with
            # Ndiff because Ndiff is also a Python application. Without removing
            # these, Ndiff will attempt to run using the py2app-bundled Python
            # library, and may run into version or architecture mismatches.
            if env.has_key("PYTHONPATH"):
                del env["PYTHONPATH"]
            if env.has_key("PYTHONHOME"):
                del env["PYTHONHOME"]

        command_list = [paths_config.ndiff_command_path, "--verbose", "--", filename_a, filename_b]
        self.stdout_file = tempfile.TemporaryFile(mode = "rb", prefix = APP_NAME + "-ndiff-", suffix = ".xml")

        log.debug("Running command: %s" % repr(command_list))
        # See zenmapCore.NmapCommand.py for an explanation of the shell argument.
        subprocess.Popen.__init__(self, command_list, stdout = self.stdout_file, stderr = self.stdout_file, env = env, shell = (sys.platform == "win32"))

    def get_scan_diff(self):
        self.wait()
        self.stdout_file.seek(0)

        return self.stdout_file.read()

    def close(self):
        """Clean up temporary files."""
        self.stdout_file.close()
        for filename in self.temporary_filenames:
            log.debug("Remove temporary diff file %s." % filename)
            os.remove(filename)
        self.temporary_filenames = []

    def kill(self):
        self.close()

def ndiff(scan_a, scan_b):
    """Run Ndiff on two scan results, which may be filenames or NmapParserSAX
    objects, and return a running NdiffCommand object."""
    temporary_filenames = []

    if isinstance(scan_a, NmapParserSAX):
        fd, filename_a = tempfile.mkstemp(prefix = APP_NAME + "-diff-", suffix = ".xml")
        temporary_filenames.append(filename_a)
        f = os.fdopen(fd, "wb")
        scan_a.write_xml(f)
        f.close()
    else:
        filename_a = scan_a

    if isinstance(scan_b, NmapParserSAX):
        fd, filename_b = tempfile.mkstemp(prefix = APP_NAME + "-diff-", suffix = ".xml")
        temporary_filenames.append(filename_b)
        f = os.fdopen(fd, "wb")
        scan_b.write_xml(f)
        f.close()
    else:
        filename_b = scan_b

    return NdiffCommand(filename_a, filename_b, temporary_filenames)
