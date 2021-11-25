
import glob
import os
import threading
import socket
import hashlib
import re
import time
# # import admin
#
import sys, os, traceback, types
import virtualbox
import win32com.client
import win32con
import win32api, win32con, win32event, win32process
import win32com.shell.shell
import shell
from win32com.shell import shellcon
from vboxapi import VirtualBoxManager
#
# malicious_files = []
# # /////////////////////////////////////////////////////////////////////////////////////////////////////
#
class sandbox:
    def start(self):
        vbox = virtualbox.VirtualBox()
        print(vbox[1])


    def stop(self):
        pass
#
#
#
# # /////////////////////////////////////////////////////////////////////////////////////////////////////
class admin_access:
    def isUserAdmin(self):
        if os.name == 'nt':
            import ctypes
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                traceback.print_exc()
                print ("Admin check failed, assuming not an admin.")
                return False
        elif os.name == 'posix':
            return os.getuid() == 0
        else:
            raise (RuntimeError, "Unsupported operating system for this module: %s" % (os.name,))

    def main_check(self):
        rc = 0
        if not admin_access.isUserAdmin(self):
            print("You're not an admin.", os.getpid())
            rc = admin_access.runAsAdmin(self)
        else:
            print("You are an admin!", os.getpid())
            rc = 0
        return rc

    def runAsAdmin(self,cmdLine=None, wait=True):
        pass
# #
#
# # /////////////////////////////////////////////////////////////////////////////////////////////////////
# import pandas as pd
# import numpy
# import seaborn as sns
# import matplotlib.pyplot
#
#
# # /////////////////////////////////////////////////////////////////////////////////////////////////////
class firewall:
    def turnOff(self):
        os.system("NetSh Advfirewall set allprofiles state off")

    def turnOn(self):
        os.system("NetSh Advfirewall set allprofiles state on")
#
# # /////////////////////////////////////////////////////////////////////////////////////////////////////
class networkscan:
    def openports(self):
        port_min = 0
        port_max = 90
        open_ports = []
        ip_add_entered = "127.0.0.1"
        for port in range(port_min, port_max + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.1)
                    s.connect((ip_add_entered, port))
                    open_ports.append(port)
                    print(port)
            except:
                pass
        for port in open_ports:
            print(f"Port {port} is open on {ip_add_entered}.")
#
# # /////////////////////////////////////////////////////////////////////////////////////////////////////
#
class systemscan:
    def list_all_file_scan(self,drive):
        a = 1
        for file_name in glob.iglob('%s/**/**'% drive, recursive=True):
            print(file_name)
            input()
         # for file_name in glob.iglob("'%s/Users/**/**'% drive, recursive=True"'C:/Users/kaush/PycharmProjects/antimalware/test/**/*.exe', recursive=True):
        # for file_name in glob.iglob('C:/Users/kaush/**/*.exe', recursive=True):
        #     Static_Analysis.file_hash(Static_Analysis,file_name)

    def list_disk_available(self):
        dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
        return drives

    def full_scan(self):
        drives = systemscan.list_disk_available(systemscan)
        for i in drives:
            systemscan.list_all_file_scan(systemscan,i)
#
# # /////////////////////////////////////////////////////////////////////////////////////////////////////
#
class Static_Analysis:
    def update_hash(self,latest_version):
        version_list = []
        for file_name in glob.iglob('./hashes/*.txt', recursive=True):
            a = ((re.findall("[0-9]+",str(file_name))))
            version_list.append(int(a[0]))
        version = (max(version_list))
        if version < latest_version:
            for i in range(version+1,latest_version+1):
                os.system("curl https://virusshare.com/hashfiles/VirusShare_0000{0}.md5 > ./hashes/hash{1}.txt".format(i,i+1))

    def file_hash(self,filename):
        try:
            file_md5 = hashlib.md5(open(filename,'rb').read()).hexdigest()
            version = open("version.txt",'r')
            ver = version.read()
            for i in range(1,int(ver)):
                f = open("./hashes/hash{}.txt".format(i),'r')
                content = f.readlines()
                file_size = (len(content))
                malicious = False
                for i in range(file_size):
                    if str(file_md5)+"\n" == str(content[i]):
                        con = "{0} Malicious file found".format(filename)
                        print("\033[91m {}\033[00m".format(con))
                        malicious = True
                        malicious_files.append(filename)
                        break

                if malicious !=True:
                    con = "{0} Good file".format(filename)
                    print("\033[92m {}\033[00m".format(con))
        except:
            pass
#
class ML_model:
    def web_url(self,url):
        sample_url = [url]
        data = pd.read_csv('urldata.csv')
        data.label.replace("good", 0, inplace=True)
        data.label.replace("bad", 1, inplace=True)
        detect = data['url']
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.feature_extraction import DictVectorizer
        cv = CountVectorizer()
        x = cv.fit_transform(detect)
        from sklearn.model_selection import train_test_split
        y = data.label
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
        from sklearn.naive_bayes import MultinomialNB
        clf = MultinomialNB()
        clf.fit(X_train, y_train)
        clf.score(X_test, y_test)
        print("Accuracy of Model", clf.score(X_test, y_test) * 100, "%")
        vect = cv.transform(sample_url).toarray()
        output = clf.predict(vect)
        if output == 0:
            return "safe"
        else:
            return "Malicious"


# # ml  = ML_model()
# # print(ml.web_url("www.radsport-voggel.de/wp-admin/includes/log.exe"))
# # /////////////////////////////////////////////////////////////////////////////////////////////////////
# s = systemscan()
# start_time = time.time()
# s.full_scan()
# print("--- %s seconds ---" % (time.time() - start_time))
# # def fullscan_button():
# #     s = systemscan()
# #     start_time = time.time()
# #     s.full_scan()
# #     print("--- %s seconds ---" % (time.time() - start_time))
#
# # def firewall_button():
# #     obj = firewall()
# #     obj.turnOn()
# #
# # def check_admin():
# #     ob = admin_access()
# #     ob.main_check()
#
# # def port_all_timeup():
# #     h = networkscan()
# #     h.openports()
# #
# # fullscan_button()
# # check_admin()
# # firewall_button()
# # port_all_timeup()
# # sand = sandbox()
# # sand.start()






#///////////////////////////////

# import admin

import sys, os, traceback, types
import virtualbox
import win32com.client
import win32con
import win32api, win32con, win32event, win32process
import win32com.shell.shell
import shell
from win32com.shell import shellcon
from vboxapi import VirtualBoxManager
import glob

malicious_files = []





class ML_model:
    pass
def count_zeroes(data):
    try:
        # newbytes' count() takes a str in Python 2
        count = data.count("\0")
    except TypeError:
        # bytes' count() takes an int in Python 3
        count = data.count(0)
    return count


fast_load = False
#
# # This will set a maximum length of a string to be retrieved from the file.
# # It's there to prevent loading massive amounts of data from memory mapped
# # files. Strings longer than 1MB should be rather rare.
# MAX_STRING_LENGTH = 0x100000  # 2^20
#
# # Maximum number of imports to parse.
# MAX_IMPORT_SYMBOLS = 0x2000
#
# # Limit maximum length for specific string types separately
MAX_IMPORT_NAME_LENGTH = 0x200
MAX_DLL_LENGTH = 0x200
MAX_SYMBOL_NAME_LENGTH = 0x200

# Lmit maximum number of sections before processing of sections will stop
MAX_SECTIONS = 0x800

# The global maximum number of resource entries to parse per file
MAX_RESOURCE_ENTRIES = 0x8000

# The maximum depth of nested resource tables
MAX_RESOURCE_DEPTH = 32

# Limit number of exported symbols
MAX_SYMBOL_EXPORT_COUNT = 0x2000

IMAGE_DOS_SIGNATURE = 0x5A4D
IMAGE_DOSZM_SIGNATURE = 0x4D5A
IMAGE_NE_SIGNATURE = 0x454E
IMAGE_LE_SIGNATURE = 0x454C
IMAGE_LX_SIGNATURE = 0x584C
IMAGE_TE_SIGNATURE = 0x5A56  # Terse Executables have a 'VZ' signature

IMAGE_NT_SIGNATURE = 0x00004550
IMAGE_NUMBEROF_DIRECTORY_ENTRIES = 16
IMAGE_ORDINAL_FLAG = 0x80000000
IMAGE_ORDINAL_FLAG64 = 0x8000000000000000
OPTIONAL_HEADER_MAGIC_PE = 0x10B
OPTIONAL_HEADER_MAGIC_PE_PLUS = 0x20B


def two_way_dict(pairs):
    return dict([(e[1], e[0]) for e in pairs] + pairs)


directory_entry_types = [
    ("IMAGE_DIRECTORY_ENTRY_EXPORT", 0),
    ("IMAGE_DIRECTORY_ENTRY_IMPORT", 1),
    ("IMAGE_DIRECTORY_ENTRY_RESOURCE", 2),
    ("IMAGE_DIRECTORY_ENTRY_EXCEPTION", 3),
    ("IMAGE_DIRECTORY_ENTRY_SECURITY", 4),
    ("IMAGE_DIRECTORY_ENTRY_BASERELOC", 5),
    ("IMAGE_DIRECTORY_ENTRY_DEBUG", 6),
    # Architecture on non-x86 platforms
    ("IMAGE_DIRECTORY_ENTRY_COPYRIGHT", 7),
    ("IMAGE_DIRECTORY_ENTRY_GLOBALPTR", 8),
    ("IMAGE_DIRECTORY_ENTRY_TLS", 9),
    ("IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG", 10),
    ("IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT", 11),
    ("IMAGE_DIRECTORY_ENTRY_IAT", 12),
    ("IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT", 13),
    ("IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR", 14),
    ("IMAGE_DIRECTORY_ENTRY_RESERVED", 15),
]
#
DIRECTORY_ENTRY = two_way_dict(directory_entry_types)

image_characteristics = [
    ("IMAGE_FILE_RELOCS_STRIPPED", 0x0001),
    ("IMAGE_FILE_EXECUTABLE_IMAGE", 0x0002),
    ("IMAGE_FILE_LINE_NUMS_STRIPPED", 0x0004),
    ("IMAGE_FILE_LOCAL_SYMS_STRIPPED", 0x0008),
    ("IMAGE_FILE_AGGRESIVE_WS_TRIM", 0x0010),
    ("IMAGE_FILE_LARGE_ADDRESS_AWARE", 0x0020),
    ("IMAGE_FILE_16BIT_MACHINE", 0x0040),
    ("IMAGE_FILE_BYTES_REVERSED_LO", 0x0080),
    ("IMAGE_FILE_32BIT_MACHINE", 0x0100),
    ("IMAGE_FILE_DEBUG_STRIPPED", 0x0200),
    ("IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP", 0x0400),
    ("IMAGE_FILE_NET_RUN_FROM_SWAP", 0x0800),
    ("IMAGE_FILE_SYSTEM", 0x1000),
    ("IMAGE_FILE_DLL", 0x2000),
    ("IMAGE_FILE_UP_SYSTEM_ONLY", 0x4000),
    ("IMAGE_FILE_BYTES_REVERSED_HI", 0x8000),
]

IMAGE_CHARACTERISTICS = two_way_dict(image_characteristics)


section_characteristics = [
    ("IMAGE_SCN_TYPE_REG", 0x00000000),  # reserved
    ("IMAGE_SCN_TYPE_DSECT", 0x00000001),  # reserved
    ("IMAGE_SCN_TYPE_NOLOAD", 0x00000002),  # reserved
    ("IMAGE_SCN_TYPE_GROUP", 0x00000004),  # reserved
    ("IMAGE_SCN_TYPE_NO_PAD", 0x00000008),  # reserved
    ("IMAGE_SCN_TYPE_COPY", 0x00000010),  # reserved
    ("IMAGE_SCN_CNT_CODE", 0x00000020),
    ("IMAGE_SCN_CNT_INITIALIZED_DATA", 0x00000040),
    ("IMAGE_SCN_CNT_UNINITIALIZED_DATA", 0x00000080),
    ("IMAGE_SCN_LNK_OTHER", 0x00000100),
    ("IMAGE_SCN_LNK_INFO", 0x00000200),
    ("IMAGE_SCN_LNK_OVER", 0x00000400),  # reserved
    ("IMAGE_SCN_LNK_REMOVE", 0x00000800),
    ("IMAGE_SCN_LNK_COMDAT", 0x00001000),
    ("IMAGE_SCN_MEM_PROTECTED", 0x00004000),  # obsolete
    ("IMAGE_SCN_NO_DEFER_SPEC_EXC", 0x00004000),
    ("IMAGE_SCN_GPREL", 0x00008000),
    ("IMAGE_SCN_MEM_FARDATA", 0x00008000),
    ("IMAGE_SCN_MEM_SYSHEAP", 0x00010000),  # obsolete
    ("IMAGE_SCN_MEM_PURGEABLE", 0x00020000),
    ("IMAGE_SCN_MEM_16BIT", 0x00020000),
    ("IMAGE_SCN_MEM_LOCKED", 0x00040000),
    ("IMAGE_SCN_MEM_PRELOAD", 0x00080000),
    ("IMAGE_SCN_ALIGN_1BYTES", 0x00100000),
    ("IMAGE_SCN_ALIGN_2BYTES", 0x00200000),
    ("IMAGE_SCN_ALIGN_4BYTES", 0x00300000),
    ("IMAGE_SCN_ALIGN_8BYTES", 0x00400000),
    ("IMAGE_SCN_ALIGN_16BYTES", 0x00500000),  # default alignment
    ("IMAGE_SCN_ALIGN_32BYTES", 0x00600000),
    ("IMAGE_SCN_ALIGN_64BYTES", 0x00700000),
    ("IMAGE_SCN_ALIGN_128BYTES", 0x00800000),
    ("IMAGE_SCN_ALIGN_256BYTES", 0x00900000),
    ("IMAGE_SCN_ALIGN_512BYTES", 0x00A00000),
    ("IMAGE_SCN_ALIGN_1024BYTES", 0x00B00000),
    ("IMAGE_SCN_ALIGN_2048BYTES", 0x00C00000),
    ("IMAGE_SCN_ALIGN_4096BYTES", 0x00D00000),
    ("IMAGE_SCN_ALIGN_8192BYTES", 0x00E00000),
    ("IMAGE_SCN_ALIGN_MASK", 0x00F00000),
    ("IMAGE_SCN_LNK_NRELOC_OVFL", 0x01000000),
    ("IMAGE_SCN_MEM_DISCARDABLE", 0x02000000),
    ("IMAGE_SCN_MEM_NOT_CACHED", 0x04000000),
    ("IMAGE_SCN_MEM_NOT_PAGED", 0x08000000),
    ("IMAGE_SCN_MEM_SHARED", 0x10000000),
    ("IMAGE_SCN_MEM_EXECUTE", 0x20000000),
    ("IMAGE_SCN_MEM_READ", 0x40000000),
    ("IMAGE_SCN_MEM_WRITE", 0x80000000),
]

SECTION_CHARACTERISTICS = two_way_dict(section_characteristics)


debug_types = [
    ("IMAGE_DEBUG_TYPE_UNKNOWN", 0),
    ("IMAGE_DEBUG_TYPE_COFF", 1),
    ("IMAGE_DEBUG_TYPE_CODEVIEW", 2),
    ("IMAGE_DEBUG_TYPE_FPO", 3),
    ("IMAGE_DEBUG_TYPE_MISC", 4),
    ("IMAGE_DEBUG_TYPE_EXCEPTION", 5),
    ("IMAGE_DEBUG_TYPE_FIXUP", 6),
    ("IMAGE_DEBUG_TYPE_OMAP_TO_SRC", 7),
    ("IMAGE_DEBUG_TYPE_OMAP_FROM_SRC", 8),
    ("IMAGE_DEBUG_TYPE_BORLAND", 9),
    ("IMAGE_DEBUG_TYPE_RESERVED10", 10),
    ("IMAGE_DEBUG_TYPE_CLSID", 11),
    ("IMAGE_DEBUG_TYPE_VC_FEATURE", 12),
    ("IMAGE_DEBUG_TYPE_POGO", 13),
    ("IMAGE_DEBUG_TYPE_ILTCG", 14),
    ("IMAGE_DEBUG_TYPE_MPX", 15),
    ("IMAGE_DEBUG_TYPE_REPRO", 16),
    ("IMAGE_DEBUG_TYPE_EX_DLLCHARACTERISTICS", 20),
]
#
DEBUG_TYPE = two_way_dict(debug_types)


subsystem_types = [
    ("IMAGE_SUBSYSTEM_UNKNOWN", 0),
    ("IMAGE_SUBSYSTEM_NATIVE", 1),
    ("IMAGE_SUBSYSTEM_WINDOWS_GUI", 2),
    ("IMAGE_SUBSYSTEM_WINDOWS_CUI", 3),
    ("IMAGE_SUBSYSTEM_OS2_CUI", 5),
    ("IMAGE_SUBSYSTEM_POSIX_CUI", 7),
    ("IMAGE_SUBSYSTEM_NATIVE_WINDOWS", 8),
    ("IMAGE_SUBSYSTEM_WINDOWS_CE_GUI", 9),
    ("IMAGE_SUBSYSTEM_EFI_APPLICATION", 10),
    ("IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER", 11),
    ("IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER", 12),
    ("IMAGE_SUBSYSTEM_EFI_ROM", 13),
    ("IMAGE_SUBSYSTEM_XBOX", 14),
    ("IMAGE_SUBSYSTEM_WINDOWS_BOOT_APPLICATION", 16),
]
#
# SUBSYSTEM_TYPE = two_way_dict(subsystem_types)
#
#
machine_types = [
    ("IMAGE_FILE_MACHINE_UNKNOWN", 0),
    ("IMAGE_FILE_MACHINE_I386", 0x014C),
    ("IMAGE_FILE_MACHINE_R3000", 0x0162),
    ("IMAGE_FILE_MACHINE_R4000", 0x0166),
    ("IMAGE_FILE_MACHINE_R10000", 0x0168),
    ("IMAGE_FILE_MACHINE_WCEMIPSV2", 0x0169),
    ("IMAGE_FILE_MACHINE_ALPHA", 0x0184),
    ("IMAGE_FILE_MACHINE_SH3", 0x01A2),
    ("IMAGE_FILE_MACHINE_SH3DSP", 0x01A3),
    ("IMAGE_FILE_MACHINE_SH3E", 0x01A4),
    ("IMAGE_FILE_MACHINE_SH4", 0x01A6),
    ("IMAGE_FILE_MACHINE_SH5", 0x01A8),
    ("IMAGE_FILE_MACHINE_ARM", 0x01C0),
    ("IMAGE_FILE_MACHINE_THUMB", 0x01C2),
    ("IMAGE_FILE_MACHINE_ARMNT", 0x01C4),
    ("IMAGE_FILE_MACHINE_AM33", 0x01D3),
    ("IMAGE_FILE_MACHINE_POWERPC", 0x01F0),
    ("IMAGE_FILE_MACHINE_POWERPCFP", 0x01F1),
    ("IMAGE_FILE_MACHINE_IA64", 0x0200),
    ("IMAGE_FILE_MACHINE_MIPS16", 0x0266),
    ("IMAGE_FILE_MACHINE_ALPHA64", 0x0284),
    ("IMAGE_FILE_MACHINE_AXP64", 0x0284),  # same
    ("IMAGE_FILE_MACHINE_MIPSFPU", 0x0366),
    ("IMAGE_FILE_MACHINE_MIPSFPU16", 0x0466),
    ("IMAGE_FILE_MACHINE_TRICORE", 0x0520),
    ("IMAGE_FILE_MACHINE_CEF", 0x0CEF),
    ("IMAGE_FILE_MACHINE_EBC", 0x0EBC),
    ("IMAGE_FILE_MACHINE_AMD64", 0x8664),
    ("IMAGE_FILE_MACHINE_M32R", 0x9041),
    ("IMAGE_FILE_MACHINE_ARM64", 0xAA64),
    ("IMAGE_FILE_MACHINE_CEE", 0xC0EE),
]

MACHINE_TYPE = two_way_dict(machine_types)


relocation_types = [
    ("IMAGE_REL_BASED_ABSOLUTE", 0),
    ("IMAGE_REL_BASED_HIGH", 1),
    ("IMAGE_REL_BASED_LOW", 2),
    ("IMAGE_REL_BASED_HIGHLOW", 3),
    ("IMAGE_REL_BASED_HIGHADJ", 4),
    ("IMAGE_REL_BASED_MIPS_JMPADDR", 5),
    ("IMAGE_REL_BASED_SECTION", 6),
    ("IMAGE_REL_BASED_REL", 7),
    ("IMAGE_REL_BASED_MIPS_JMPADDR16", 9),
    ("IMAGE_REL_BASED_IA64_IMM64", 9),
    ("IMAGE_REL_BASED_DIR64", 10),
    ("IMAGE_REL_BASED_HIGH3ADJ", 11),
]
#
RELOCATION_TYPE = two_way_dict(relocation_types)


dll_characteristics = [
    ("IMAGE_LIBRARY_PROCESS_INIT", 0x0001),  # reserved
    ("IMAGE_LIBRARY_PROCESS_TERM", 0x0002),  # reserved
    ("IMAGE_LIBRARY_THREAD_INIT", 0x0004),  # reserved
    ("IMAGE_LIBRARY_THREAD_TERM", 0x0008),  # reserved
    ("IMAGE_DLLCHARACTERISTICS_HIGH_ENTROPY_VA", 0x0020),
    ("IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE", 0x0040),
    ("IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY", 0x0080),
    ("IMAGE_DLLCHARACTERISTICS_NX_COMPAT", 0x0100),
    ("IMAGE_DLLCHARACTERISTICS_NO_ISOLATION", 0x0200),
    ("IMAGE_DLLCHARACTERISTICS_NO_SEH", 0x0400),
    ("IMAGE_DLLCHARACTERISTICS_NO_BIND", 0x0800),
    ("IMAGE_DLLCHARACTERISTICS_APPCONTAINER", 0x1000),
    ("IMAGE_DLLCHARACTERISTICS_WDM_DRIVER", 0x2000),
    ("IMAGE_DLLCHARACTERISTICS_GUARD_CF", 0x4000),
    ("IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE", 0x8000),
]
#
# DLL_CHARACTERISTICS = two_way_dict(dll_characteristics)
#
# FILE_ALIGNMENT_HARDCODED_VALUE = 0x200
#
#
# # Unwind info-related enums
#
unwind_info_flags = [
    ("UNW_FLAG_EHANDLER", 0x01),
    ("UNW_FLAG_UHANDLER", 0x02),
    ("UNW_FLAG_CHAININFO", 0x04),
]

# UNWIND_INFO_FLAGS = two_way_dict(unwind_info_flags)
#
registers = [
    ("RAX", 0),
    ("RCX", 1),
    ("RDX", 2),
    ("RBX", 3),
    ("RSP", 4),
    ("RBP", 5),
    ("RSI", 6),
    ("RDI", 7),
    ("R8", 8),
    ("R9", 9),
    ("R10", 10),
    ("R11", 11),
    ("R12", 12),
    ("R13", 13),
    ("R14", 14),
    ("R15", 15),
]
#
REGISTERS = two_way_dict(registers)

# enum _UNWIND_OP_CODES
UWOP_PUSH_NONVOL = 0
UWOP_ALLOC_LARGE = 1
UWOP_ALLOC_SMALL = 2
UWOP_SET_FPREG = 3
UWOP_SAVE_NONVOL = 4
UWOP_SAVE_NONVOL_FAR = 5
UWOP_EPILOG = 6
UWOP_SAVE_XMM128 = 8
UWOP_SAVE_XMM128_FAR = 9
UWOP_PUSH_MACHFRAME = 10


# Resource types
resource_type = [
    ("RT_CURSOR", 1),
    ("RT_BITMAP", 2),
    ("RT_ICON", 3),
    ("RT_MENU", 4),
    ("RT_DIALOG", 5),
    ("RT_STRING", 6),
    ("RT_FONTDIR", 7),
    ("RT_FONT", 8),
    ("RT_ACCELERATOR", 9),
    ("RT_RCDATA", 10),
    ("RT_MESSAGETABLE", 11),
    ("RT_GROUP_CURSOR", 12),
    ("RT_GROUP_ICON", 14),
    ("RT_VERSION", 16),
    ("RT_DLGINCLUDE", 17),
    ("RT_PLUGPLAY", 19),
    ("RT_VXD", 20),
    ("RT_ANICURSOR", 21),
    ("RT_ANIICON", 22),
    ("RT_HTML", 23),
    ("RT_MANIFEST", 24),
]

RESOURCE_TYPE = two_way_dict(resource_type)


# Language definitions
lang = [
    ("LANG_NEUTRAL", 0x00),
    ("LANG_INVARIANT", 0x7F),
    ("LANG_AFRIKAANS", 0x36),
    ("LANG_ALBANIAN", 0x1C),
    ("LANG_ARABIC", 0x01),
    ("LANG_ARMENIAN", 0x2B),
    ("LANG_ASSAMESE", 0x4D),
    ("LANG_AZERI", 0x2C),
    ("LANG_BASQUE", 0x2D),
    ("LANG_BELARUSIAN", 0x23),
    ("LANG_BENGALI", 0x45),
    ("LANG_BULGARIAN", 0x02),
    ("LANG_CATALAN", 0x03),
    ("LANG_CHINESE", 0x04),
    ("LANG_CROATIAN", 0x1A),
    ("LANG_CZECH", 0x05),
    ("LANG_DANISH", 0x06),
    ("LANG_DIVEHI", 0x65),
    ("LANG_DUTCH", 0x13),
    ("LANG_ENGLISH", 0x09),
    ("LANG_ESTONIAN", 0x25),
    ("LANG_FAEROESE", 0x38),
    ("LANG_FARSI", 0x29),
    ("LANG_FINNISH", 0x0B),
    ("LANG_FRENCH", 0x0C),
    ("LANG_GALICIAN", 0x56),
    ("LANG_GEORGIAN", 0x37),
    ("LANG_GERMAN", 0x07),
    ("LANG_GREEK", 0x08),
    ("LANG_GUJARATI", 0x47),
    ("LANG_HEBREW", 0x0D),
    ("LANG_HINDI", 0x39),
    ("LANG_HUNGARIAN", 0x0E),
    ("LANG_ICELANDIC", 0x0F),
    ("LANG_INDONESIAN", 0x21),
    ("LANG_ITALIAN", 0x10),
    ("LANG_JAPANESE", 0x11),
    ("LANG_KANNADA", 0x4B),
    ("LANG_KASHMIRI", 0x60),
    ("LANG_KAZAK", 0x3F),
    ("LANG_KONKANI", 0x57),
    ("LANG_KOREAN", 0x12),
    ("LANG_KYRGYZ", 0x40),
    ("LANG_LATVIAN", 0x26),
    ("LANG_LITHUANIAN", 0x27),
    ("LANG_MACEDONIAN", 0x2F),
    ("LANG_MALAY", 0x3E),
    ("LANG_MALAYALAM", 0x4C),
    ("LANG_MANIPURI", 0x58),
    ("LANG_MARATHI", 0x4E),
    ("LANG_MONGOLIAN", 0x50),
    ("LANG_NEPALI", 0x61),
    ("LANG_NORWEGIAN", 0x14),
    ("LANG_ORIYA", 0x48),
    ("LANG_POLISH", 0x15),
    ("LANG_PORTUGUESE", 0x16),
    ("LANG_PUNJABI", 0x46),
    ("LANG_ROMANIAN", 0x18),
    ("LANG_RUSSIAN", 0x19),
    ("LANG_SANSKRIT", 0x4F),
    ("LANG_SERBIAN", 0x1A),
    ("LANG_SINDHI", 0x59),
    ("LANG_SLOVAK", 0x1B),
    ("LANG_SLOVENIAN", 0x24),
    ("LANG_SPANISH", 0x0A),
    ("LANG_SWAHILI", 0x41),
    ("LANG_SWEDISH", 0x1D),
    ("LANG_SYRIAC", 0x5A),
    ("LANG_TAMIL", 0x49),
    ("LANG_TATAR", 0x44),
    ("LANG_TELUGU", 0x4A),
    ("LANG_THAI", 0x1E),
    ("LANG_TURKISH", 0x1F),
    ("LANG_UKRAINIAN", 0x22),
    ("LANG_URDU", 0x20),
    ("LANG_UZBEK", 0x43),
    ("LANG_VIETNAMESE", 0x2A),
    ("LANG_GAELIC", 0x3C),
    ("LANG_MALTESE", 0x3A),
    ("LANG_MAORI", 0x28),
    ("LANG_RHAETO_ROMANCE", 0x17),
    ("LANG_SAAMI", 0x3B),
    ("LANG_SORBIAN", 0x2E),
    ("LANG_SUTU", 0x30),
    ("LANG_TSONGA", 0x31),
    ("LANG_TSWANA", 0x32),
    ("LANG_VENDA", 0x33),
    ("LANG_XHOSA", 0x34),
    ("LANG_ZULU", 0x35),
    ("LANG_ESPERANTO", 0x8F),
    ("LANG_WALON", 0x90),
    ("LANG_CORNISH", 0x91),
    ("LANG_WELSH", 0x92),
    ("LANG_BRETON", 0x93),
]

LANG = two_way_dict(lang)


# Sublanguage definitions
sublang = [
    ("SUBLANG_NEUTRAL", 0x00),
    ("SUBLANG_DEFAULT", 0x01),
    ("SUBLANG_SYS_DEFAULT", 0x02),
    ("SUBLANG_ARABIC_SAUDI_ARABIA", 0x01),
    ("SUBLANG_ARABIC_IRAQ", 0x02),
    ("SUBLANG_ARABIC_EGYPT", 0x03),
    ("SUBLANG_ARABIC_LIBYA", 0x04),
    ("SUBLANG_ARABIC_ALGERIA", 0x05),
    ("SUBLANG_ARABIC_MOROCCO", 0x06),
    ("SUBLANG_ARABIC_TUNISIA", 0x07),
    ("SUBLANG_ARABIC_OMAN", 0x08),
    ("SUBLANG_ARABIC_YEMEN", 0x09),
    ("SUBLANG_ARABIC_SYRIA", 0x0A),
    ("SUBLANG_ARABIC_JORDAN", 0x0B),
    ("SUBLANG_ARABIC_LEBANON", 0x0C),
    ("SUBLANG_ARABIC_KUWAIT", 0x0D),
    ("SUBLANG_ARABIC_UAE", 0x0E),
    ("SUBLANG_ARABIC_BAHRAIN", 0x0F),
    ("SUBLANG_ARABIC_QATAR", 0x10),
    ("SUBLANG_AZERI_LATIN", 0x01),
    ("SUBLANG_AZERI_CYRILLIC", 0x02),
    ("SUBLANG_CHINESE_TRADITIONAL", 0x01),
    ("SUBLANG_CHINESE_SIMPLIFIED", 0x02),
    ("SUBLANG_CHINESE_HONGKONG", 0x03),
    ("SUBLANG_CHINESE_SINGAPORE", 0x04),
    ("SUBLANG_CHINESE_MACAU", 0x05),
    ("SUBLANG_DUTCH", 0x01),
    ("SUBLANG_DUTCH_BELGIAN", 0x02),
    ("SUBLANG_ENGLISH_US", 0x01),
    ("SUBLANG_ENGLISH_UK", 0x02),
    ("SUBLANG_ENGLISH_AUS", 0x03),
    ("SUBLANG_ENGLISH_CAN", 0x04),
    ("SUBLANG_ENGLISH_NZ", 0x05),
    ("SUBLANG_ENGLISH_EIRE", 0x06),
    ("SUBLANG_ENGLISH_SOUTH_AFRICA", 0x07),
    ("SUBLANG_ENGLISH_JAMAICA", 0x08),
    ("SUBLANG_ENGLISH_CARIBBEAN", 0x09),
    ("SUBLANG_ENGLISH_BELIZE", 0x0A),
    ("SUBLANG_ENGLISH_TRINIDAD", 0x0B),
    ("SUBLANG_ENGLISH_ZIMBABWE", 0x0C),
    ("SUBLANG_ENGLISH_PHILIPPINES", 0x0D),
    ("SUBLANG_FRENCH", 0x01),
    ("SUBLANG_FRENCH_BELGIAN", 0x02),
    ("SUBLANG_FRENCH_CANADIAN", 0x03),
    ("SUBLANG_FRENCH_SWISS", 0x04),
    ("SUBLANG_FRENCH_LUXEMBOURG", 0x05),
    ("SUBLANG_FRENCH_MONACO", 0x06),
    ("SUBLANG_GERMAN", 0x01),
    ("SUBLANG_GERMAN_SWISS", 0x02),
    ("SUBLANG_GERMAN_AUSTRIAN", 0x03),
    ("SUBLANG_GERMAN_LUXEMBOURG", 0x04),
    ("SUBLANG_GERMAN_LIECHTENSTEIN", 0x05),
    ("SUBLANG_ITALIAN", 0x01),
    ("SUBLANG_ITALIAN_SWISS", 0x02),
    ("SUBLANG_KASHMIRI_SASIA", 0x02),
    ("SUBLANG_KASHMIRI_INDIA", 0x02),
    ("SUBLANG_KOREAN", 0x01),
    ("SUBLANG_LITHUANIAN", 0x01),
    ("SUBLANG_MALAY_MALAYSIA", 0x01),
    ("SUBLANG_MALAY_BRUNEI_DARUSSALAM", 0x02),
    ("SUBLANG_NEPALI_INDIA", 0x02),
    ("SUBLANG_NORWEGIAN_BOKMAL", 0x01),
    ("SUBLANG_NORWEGIAN_NYNORSK", 0x02),
    ("SUBLANG_PORTUGUESE", 0x02),
    ("SUBLANG_PORTUGUESE_BRAZILIAN", 0x01),
    ("SUBLANG_SERBIAN_LATIN", 0x02),
    ("SUBLANG_SERBIAN_CYRILLIC", 0x03),
    ("SUBLANG_SPANISH", 0x01),
    ("SUBLANG_SPANISH_MEXICAN", 0x02),
    ("SUBLANG_SPANISH_MODERN", 0x03),
    ("SUBLANG_SPANISH_GUATEMALA", 0x04),
    ("SUBLANG_SPANISH_COSTA_RICA", 0x05),
    ("SUBLANG_SPANISH_PANAMA", 0x06),
    ("SUBLANG_SPANISH_DOMINICAN_REPUBLIC", 0x07),
    ("SUBLANG_SPANISH_VENEZUELA", 0x08),
    ("SUBLANG_SPANISH_COLOMBIA", 0x09),
    ("SUBLANG_SPANISH_PERU", 0x0A),
    ("SUBLANG_SPANISH_ARGENTINA", 0x0B),
    ("SUBLANG_SPANISH_ECUADOR", 0x0C),
    ("SUBLANG_SPANISH_CHILE", 0x0D),
    ("SUBLANG_SPANISH_URUGUAY", 0x0E),
    ("SUBLANG_SPANISH_PARAGUAY", 0x0F),
    ("SUBLANG_SPANISH_BOLIVIA", 0x10),
    ("SUBLANG_SPANISH_EL_SALVADOR", 0x11),
    ("SUBLANG_SPANISH_HONDURAS", 0x12),
    ("SUBLANG_SPANISH_NICARAGUA", 0x13),
    ("SUBLANG_SPANISH_PUERTO_RICO", 0x14),
    ("SUBLANG_SWEDISH", 0x01),
    ("SUBLANG_SWEDISH_FINLAND", 0x02),
    ("SUBLANG_URDU_PAKISTAN", 0x01),
    ("SUBLANG_URDU_INDIA", 0x02),
    ("SUBLANG_UZBEK_LATIN", 0x01),
    ("SUBLANG_UZBEK_CYRILLIC", 0x02),
    ("SUBLANG_DUTCH_SURINAM", 0x03),
    ("SUBLANG_ROMANIAN", 0x01),
    ("SUBLANG_ROMANIAN_MOLDAVIA", 0x02),
    ("SUBLANG_RUSSIAN", 0x01),
    ("SUBLANG_RUSSIAN_MOLDAVIA", 0x02),
    ("SUBLANG_CROATIAN", 0x01),
    ("SUBLANG_LITHUANIAN_CLASSIC", 0x02),
    ("SUBLANG_GAELIC", 0x01),
    ("SUBLANG_GAELIC_SCOTTISH", 0x02),
    ("SUBLANG_GAELIC_MANX", 0x03),
]

SUBLANG = two_way_dict(sublang)

# # Initialize the dictionary with all the name->value pairs
# SUBLANG = dict(sublang)
# # Now add all the value->name information, handling duplicates appropriately
# for sublang_name, sublang_value in sublang:
    if sublang_value in SUBLANG:
        SUBLANG[sublang_value].append(sublang_name)
    else:
        SUBLANG[sublang_value] = [sublang_name]

# # Resolve a sublang name given the main lang name
# #
def get_sublang_name_for_lang(lang_value, sublang_value):
    lang_name = LANG.get(lang_value, "*unknown*")
    for sublang_name in SUBLANG.get(sublang_value, []):
        # if the main language is a substring of sublang's name, then
        # return that
        if lang_name in sublang_name:
            return sublang_name
    # otherwise return the first sublang name
    return SUBLANG.get(sublang_value, ["*unknown*"])[0]

#
# # Ange Albertini's code to process resources' strings
# #
def parse_strings(data, counter, l):
    i = 0
    error_count = 0
    while i < len(data):

        data_slice = data[i : i + 2]
        if len(data_slice) < 2:
            break

        len_ = struct.unpack("<h", data_slice)[0]
        i += 2
        if len_ != 0 and 0 <= len_ * 2 <= len(data):
            try:
                l[counter] = b(data[i : i + len_ * 2]).decode("utf-16le")
            except UnicodeDecodeError:
                error_count += 1
                pass
            if error_count >= 3:
                break
            i += len_ * 2
        counter += 1


def retrieve_flags(flag_dict, flag_filter):
    """Read the flags from a dictionary and return them in a usable form.
    Will return a list of (flag, value) for all flags in "flag_dict"
    matching the filter "flag_filter".
    """

    return [
        (flag, flag_dict[flag])
        for flag in flag_dict.keys()
        if isinstance(flag, (str, bytes)) and flag.startswith(flag_filter)
    ]


def set_flags(obj, flag_field, flags):
    """Will process the flags and set attributes in the object accordingly.
    The object "obj" will gain attributes named after the flags provided in
    "flags" and valued True/False, matching the results of applying each
    flag value from "flags" to flag_field.
    """

    for flag, value in flags:
        if value & flag_field:
            obj.__dict__[flag] = True
        else:
            obj.__dict__[flag] = False


def power_of_two(val):
    return val != 0 and (val & (val - 1)) == 0


def b(x):
    if isinstance(x, (bytes, bytearray)):
        return bytes(x)
    return codecs.encode(x, "cp1252")


class UnicodeStringWrapperPostProcessor:
    """This class attempts to help the process of identifying strings
    that might be plain Unicode or Pascal. A list of strings will be
    wrapped on it with the hope the overlappings will help make the
    decision about their type."""

    def __init__(self, pe, rva_ptr):
        self.pe = pe
        self.rva_ptr = rva_ptr
        self.string = None

    def get_rva(self):
        """Get the RVA of the string."""
        return self.rva_ptr

    def __str__(self):
        """Return the escaped UTF-8 representation of the string."""
        return self.decode("utf-8", "backslashreplace_")

    def decode(self, *args):
        if not self.string:
            return ""
        return self.string.decode(*args)

    def invalidate(self):
        """Make this instance None, to express it's no known string type."""
        self = None

    def render_pascal_16(self):
        try:
            self.string = self.pe.get_string_u_at_rva(
                self.rva_ptr + 2, max_length=self.get_pascal_16_length()
            )
        except PEFormatError:
            self.pe.get_warnings().append(
                "Failed rendering pascal string, "
                "attempting to read from RVA 0x{0:x}".format(self.rva_ptr + 2)
            )

    def get_pascal_16_length(self):
        return self.__get_word_value_at_rva(self.rva_ptr)

    def __get_word_value_at_rva(self, rva):
        try:
            data = self.pe.get_data(rva, 2)
        except PEFormatError:
            return False

        if len(data) < 2:
            return False

        return struct.unpack("<H", data)[0]

    def ask_unicode_16(self, next_rva_ptr):
        """The next RVA is taken to be the one immediately following this one.
        Such RVA could indicate the natural end of the string and will be checked
        to see if there's a Unicode NULL character there.
        """
        if self.__get_word_value_at_rva(next_rva_ptr - 2) == 0:
            self.length = next_rva_ptr - self.rva_ptr
            return True

        return False

    def render_unicode_16(self):
        try:
            self.string = self.pe.get_string_u_at_rva(self.rva_ptr)
        except PEFormatError:
            self.pe.get_warnings().append(
                "Failed rendering unicode string, "
                "attempting to read from RVA 0x{0:x}".format(self.rva_ptr)
            )


class PEFormatError(Exception):
    """Generic PE format error exception."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Dump:
    """Convenience class for dumping the PE information."""

    def __init__(self):
        self.text = []

    def add_lines(self, txt, indent=0):
        """Adds a list of lines.
        The list can be indented with the optional argument 'indent'.
        """
        for line in txt:
            self.add_line(line, indent)

    def add_line(self, txt, indent=0):
        """Adds a line.
        The line can be indented with the optional argument 'indent'.
        """
        self.add(txt + "\n", indent)

    def add(self, txt, indent=0):
        """Adds some text, no newline will be appended.
        The text can be indented with the optional argument 'indent'.
        """
        self.text.append("{0}{1}".format(" " * indent, txt))

    def add_header(self, txt):
        """Adds a header element."""
        self.add_line("{0}{1}{0}\n".format("-" * 10, txt))

    def add_newline(self):
        """Adds a newline."""
        self.text.append("\n")

    def get_text(self):
        """Get the text in its current state."""
        return "".join("{0}".format(b) for b in self.text)


STRUCT_SIZEOF_TYPES = {
    "x": 1,
    "c": 1,
    "b": 1,
    "B": 1,
    "h": 2,
    "H": 2,
    "i": 4,
    "I": 4,
    "l": 4,
    "L": 4,
    "f": 4,
    "q": 8,
    "Q": 8,
    "d": 8,
    "s": 1,
}


@lru_cache(maxsize=2048)
def sizeof_type(t):
    count = 1
    _t = t
    if t[0] in string.digits:
        # extract the count
        count = int("".join([d for d in t if d in string.digits]))
        _t = "".join([d for d in t if d not in string.digits])
    return STRUCT_SIZEOF_TYPES[_t] * count


@lru_cache(maxsize=2048, copy=True)
def set_format(format):

    __format__ = "<"
    __unpacked_data_elms__ = []
    __field_offsets__ = {}
    __keys__ = []
    __format_length__ = 0

    offset = 0
    for elm in format:
        if "," in elm:
            elm_type, elm_name = elm.split(",", 1)
            __format__ += elm_type
            __unpacked_data_elms__.append(None)

            elm_names = elm_name.split(",")
            names = []
            for elm_name in elm_names:
                if elm_name in __keys__:
                    search_list = [x[: len(elm_name)] for x in __keys__]
                    occ_count = search_list.count(elm_name)
                    elm_name = "{0}_{1:d}".format(elm_name, occ_count)
                names.append(elm_name)
                __field_offsets__[elm_name] = offset

            offset += sizeof_type(elm_type)

            # Some PE header structures have unions on them, so a certain
            # value might have different names, so each key has a list of
            # all the possible members referring to the data.
            __keys__.append(names)

    __format_length__ = struct.calcsize(__format__)

    return (
        __format__,
        __unpacked_data_elms__,
        __field_offsets__,
        __keys__,
        __format_length__,
    )


class Structure:
    """Prepare structure object to extract members from data.
    Format is a list containing definitions for the elements
    of the structure.
    """

    def __init__(self, format, name=None, file_offset=None):
        # Format is forced little endian, for big endian non Intel platforms
        self.__format__ = "<"
        self.__keys__ = []
        self.__format_length__ = 0
        self.__field_offsets__ = {}
        self.__unpacked_data_elms__ = []

        d = format[1]
        # need a tuple to be hashable in set_format using lru cache
        if not isinstance(format[1], tuple):
            d = tuple(format[1])

        (
            self.__format__,
            self.__unpacked_data_elms__,
            self.__field_offsets__,
            self.__keys__,
            self.__format_length__,
        ) = set_format(d)

        self.__all_zeroes__ = False
        self.__file_offset__ = file_offset
        if name:
            self.name = name
        else:
            self.name = format[0]

    def __get_format__(self):
        return self.__format__

    def get_field_absolute_offset(self, field_name):
        """Return the offset within the field for the requested field in the structure."""
        return self.__file_offset__ + self.__field_offsets__[field_name]

    def get_field_relative_offset(self, field_name):
        """Return the offset within the structure for the requested field."""
        return self.__field_offsets__[field_name]

    def get_file_offset(self):
        return self.__file_offset__

    def set_file_offset(self, offset):
        self.__file_offset__ = offset

    def all_zeroes(self):
        """Returns true is the unpacked data is all zeros."""

        return self.__all_zeroes__

    def sizeof(self):
        """Return size of the structure."""

        return self.__format_length__

    def __unpack__(self, data):

        data = b(data)

        if len(data) > self.__format_length__:
            data = data[: self.__format_length__]

        # OC Patch:
        # Some malware have incorrect header lengths.
        # Fail gracefully if this occurs
        # Buggy malware: a29b0118af8b7408444df81701ad5a7f
        #
        elif len(data) < self.__format_length__:
            raise PEFormatError("Data length less than expected header length.")

        if count_zeroes(data) == len(data):
            self.__all_zeroes__ = True

        self.__unpacked_data_elms__ = struct.unpack(self.__format__, data)
        for idx, val in enumerate(self.__unpacked_data_elms__):
            for key in self.__keys__[idx]:
                setattr(self, key, val)

    def __pack__(self):

        new_values = []

        for idx, val in enumerate(self.__unpacked_data_elms__):

            for key in self.__keys__[idx]:
                new_val = getattr(self, key)

                # In the case of unions, when the first changed value
                # is picked the loop is exited
                if new_val != val:
                    break

            new_values.append(new_val)

        return struct.pack(self.__format__, *new_values)

    def __str__(self):
        return "\n".join(self.dump())

    def __repr__(self):
        return "<Structure: %s>" % (
            " ".join([" ".join(s.split()) for s in self.dump()])
        )

    def dump(self, indentation=0):
        """Returns a string representation of the structure."""

        dump = []

        dump.append("[{0}]".format(self.name))

        printable_bytes = [
            ord(i) for i in string.printable if i not in string.whitespace
        ]

        # Refer to the __set_format__ method for an explanation
        # of the following construct.
        for keys in self.__keys__:
            for key in keys:

                val = getattr(self, key)
                if isinstance(val, (int, long)):
                    if key.startswith("Signature_"):
                        val_str = "{:<8X}".format(val)
                    else:
                        val_str = "0x{:<8X}".format(val)
                    if key == "TimeDateStamp" or key == "dwTimeStamp":
                        try:
                            val_str += " [%s UTC]" % time.asctime(time.gmtime(val))
                        except ValueError:
                            val_str += " [INVALID TIME]"
                else:
                    val_str = bytearray(val)
                    if key.startswith("Signature"):
                        val_str = "".join(
                            ["{:02X}".format(i) for i in val_str.rstrip(b"\x00")]
                        )
                    else:
                        val_str = "".join(
                            [
                                chr(i)
                                if (i in printable_bytes)
                                else "\\x{0:02x}".format(i)
                                for i in val_str.rstrip(b"\x00")
                            ]
                        )

                dump.append(
                    "0x%-8X 0x%-3X %-30s %s"
                    % (
                        self.__field_offsets__[key] + self.__file_offset__,
                        self.__field_offsets__[key],
                        key + ":",
                        val_str,
                    )
                )

        return dump

    def dump_dict(self):
        """Returns a dictionary representation of the structure."""

        dump_dict = {}

        dump_dict["Structure"] = self.name

        # Refer to the __set_format__ method for an explanation
        # of the following construct.
        for keys in self.__keys__:
            for key in keys:

                val = getattr(self, key)
                if isinstance(val, (int, long)):
                    if key == "TimeDateStamp" or key == "dwTimeStamp":
                        try:
                            val = "0x%-8X [%s UTC]" % (
                                val,
                                time.asctime(time.gmtime(val)),
                            )
                        except ValueError:
                            val = "0x%-8X [INVALID TIME]" % val
                else:
                    val = "".join(
                        chr(d) if chr(d) in string.printable else "\\x%02x" % d
                        for d in [ord(c) if not isinstance(c, int) else c for c in val]
                    )

                dump_dict[key] = {
                    "FileOffset": self.__field_offsets__[key] + self.__file_offset__,
                    "Offset": self.__field_offsets__[key],
                    "Value": val,
                }

        return dump_dict


class SectionStructure(Structure):
    """Convenience section handling class."""

    def __init__(self, *argl, **argd):
        if "pe" in argd:
            self.pe = argd["pe"]
            del argd["pe"]

        Structure.__init__(self, *argl, **argd)
        self.PointerToRawData_adj = None
        self.VirtualAddress_adj = None

    def get_PointerToRawData_adj(self):
        if self.PointerToRawData_adj is None:
            if self.PointerToRawData is not None:
                self.PointerToRawData_adj = self.pe.adjust_FileAlignment(
                    self.PointerToRawData, self.pe.OPTIONAL_HEADER.FileAlignment
                )
        return self.PointerToRawData_adj

    def get_VirtualAddress_adj(self):
        if self.VirtualAddress_adj is None:
            if self.VirtualAddress is not None:
                self.VirtualAddress_adj = self.pe.adjust_SectionAlignment(
                    self.VirtualAddress,
                    self.pe.OPTIONAL_HEADER.SectionAlignment,
                    self.pe.OPTIONAL_HEADER.FileAlignment,
                )
        return self.VirtualAddress_adj

    def get_data(self, start=None, length=None):
        """Get data chunk from a section.
        Allows to query data from the section by passing the
        addresses where the PE file would be loaded by default.
        It is then possible to retrieve code and data by their real
        addresses as they would be if loaded.
        Returns bytes() under Python 3.x and set() under Python 2.7
        """

        if start is None:
            offset = self.get_PointerToRawData_adj()
        else:
            offset = (
                start - self.get_VirtualAddress_adj()
            ) + self.get_PointerToRawData_adj()

        if length is not None:
            end = offset + length
        else:
            end = offset + self.SizeOfRawData
        # PointerToRawData is not adjusted here as we might want to read any possible
        # extra bytes that might get cut off by aligning the start (and hence cutting
        # something off the end)
        if end > self.PointerToRawData + self.SizeOfRawData:
            end = self.PointerToRawData + self.SizeOfRawData
        return self.pe.__data__[offset:end]

    def __setattr__(self, name, val):

        if name == "Characteristics":
            section_flags = retrieve_flags(SECTION_CHARACTERISTICS, "IMAGE_SCN_")

            # Set the section's flags according to the Characteristics member
            set_flags(self, val, section_flags)

        elif "IMAGE_SCN_" in name and hasattr(self, name):
            if val:
                self.__dict__["Characteristics"] |= SECTION_CHARACTERISTICS[name]
            else:
                self.__dict__["Characteristics"] ^= SECTION_CHARACTERISTICS[name]

        self.__dict__[name] = val

    def get_rva_from_offset(self, offset):
        return offset - self.get_PointerToRawData_adj() + self.get_VirtualAddress_adj()

    def get_offset_from_rva(self, rva):
        return rva - self.get_VirtualAddress_adj() + self.get_PointerToRawData_adj()

    def contains_offset(self, offset):
        """Check whether the section contains the file offset provided."""

        if self.PointerToRawData is None:
            # bss and other sections containing only uninitialized data must have 0
            # and do not take space in the file
            return False
        PointerToRawData_adj = self.get_PointerToRawData_adj()
        return (
            PointerToRawData_adj <= offset < PointerToRawData_adj + self.SizeOfRawData
        )

    def contains_rva(self, rva):
        """Check whether the section contains the address provided."""

        VirtualAddress_adj = self.get_VirtualAddress_adj()
        # Check if the SizeOfRawData is realistic. If it's bigger than the size of
        # the whole PE file minus the start address of the section it could be
        # either truncated or the SizeOfRawData contains a misleading value.
        # In either of those cases we take the VirtualSize
        #
        if len(self.pe.__data__) - self.get_PointerToRawData_adj() < self.SizeOfRawData:
            # PECOFF documentation v8 says:
            # VirtualSize: The total size of the section when loaded into memory.
            # If this value is greater than SizeOfRawData, the section is zero-padded.
            # This field is valid only for executable images and should be set to zero
            # for object files.
            #
            size = self.Misc_VirtualSize
        else:
            size = max(self.SizeOfRawData, self.Misc_VirtualSize)

        # Check whether there's any section after the current one that starts before
        # the calculated end for the current one. If so, cut the current section's size
        # to fit in the range up to where the next section starts.
        if (
            self.next_section_virtual_address is not None
            and self.next_section_virtual_address > self.VirtualAddress
            and VirtualAddress_adj + size > self.next_section_virtual_address
        ):
            size = self.next_section_virtual_address - VirtualAddress_adj

        return VirtualAddress_adj <= rva < VirtualAddress_adj + size

    def contains(self, rva):
        return self.contains_rva(rva)

    def get_entropy(self):
        """Calculate and return the entropy for the section."""

        return self.entropy_H(self.get_data())

    def get_hash_sha1(self):
        """Get the SHA-1 hex-digest of the section's data."""

        if sha1 is not None:
            return sha1(self.get_data()).hexdigest()

    def get_hash_sha256(self):
        """Get the SHA-256 hex-digest of the section's data."""

        if sha256 is not None:
            return sha256(self.get_data()).hexdigest()

    def get_hash_sha512(self):
        """Get the SHA-512 hex-digest of the section's data."""

        if sha512 is not None:
            return sha512(self.get_data()).hexdigest()

    def get_hash_md5(self):
        """Get the MD5 hex-digest of the section's data."""

        if md5 is not None:
            return md5(self.get_data()).hexdigest()

    def entropy_H(self, data):
        """Calculate the entropy of a chunk of data."""

        if not data:
            return 0.0

        occurences = Counter(bytearray(data))

        entropy = 0
        for x in occurences.values():
            p_x = float(x) / len(data)
            entropy -= p_x * math.log(p_x, 2)

        return entropy


@lru_cache(maxsize=2048, copy=False)
def set_bitfields_format(format):
    class Accumulator:
        def __init__(self, fmt, comp_fields):
            self._subfields = []
            # add a prefix to distinguish the artificially created compoud field
            # from regular fields
            self._name = "~"
            self._type = None
            self._bits_left = 0
            self._comp_fields = comp_fields
            self._format = fmt

        def wrap_up(self):
            if self._type == None:
                return
            self._format.append(self._type + "," + self._name)
            self._comp_fields[len(self._format) - 1] = (self._type, self._subfields)
            self._name = "~"
            self._type = None
            self._subfields = []

        def new_type(self, tp):
            self._bits_left = STRUCT_SIZEOF_TYPES[tp] * 8
            self._type = tp

        def add_subfield(self, name, bitcnt):
            self._name += name
            self._bits_left -= bitcnt
            self._subfields.append((name, bitcnt))

        def get_type(self):
            return self._type

        def get_name(self):
            return self._name

        def get_bits_left(self):
            return self._bits_left

    old_fmt = []
    comp_fields = {}
    ac = Accumulator(old_fmt, comp_fields)

    for elm in format[1]:
        if not ":" in elm:
            ac.wrap_up()
            old_fmt.append(elm)
            continue

        elm_type, elm_name = elm.split(",", 1)

        if "," in elm_name:
            raise NotImplementedError(
                "Structures with bitfields do not support unions yet"
            )

        elm_type, elm_bits = elm_type.split(":", 1)
        elm_bits = int(elm_bits)
        if elm_type != ac.get_type() or elm_bits > ac.get_bits_left():
            ac.wrap_up()
            ac.new_type(elm_type)

        ac.add_subfield(elm_name, elm_bits)
    ac.wrap_up()

    format_str, _, field_offsets, keys, format_length = set_format(tuple(old_fmt))

    extended_keys = []
    for idx, val in enumerate(keys):
        if not idx in comp_fields:
            extended_keys.append(val)
            continue
        _, sbf = comp_fields[idx]
        bf_names = [[f[StructureWithBitfields.BTF_NAME_IDX]] for f in sbf]
        extended_keys.extend(bf_names)
        for n in bf_names:
            field_offsets[n[0]] = field_offsets[val[0]]

    return (format_str, format_length, field_offsets, keys, extended_keys, comp_fields)






/////////////////////////////////////////////////////////////////////////////////////////////////////

class sandbox:
    def start(self):
        vbox = virtualbox.VirtualBox()
        print(vbox[1])


    def stop(self):
        pass



/////////////////////////////////////////////////////////////////////////////////////////////////////
class admin_access:
    def isUserAdmin(self):
        if os.name == 'nt':
            import ctypes
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                traceback.print_exc()
                print ("Admin check failed, assuming not an admin.")
                return False
        elif os.name == 'posix':
            return os.getuid() == 0
        else:
            raise (RuntimeError, "Unsupported operating system for this module: %s" % (os.name,))

    def main_check(self):
        rc = 0
        if not admin_access.isUserAdmin(self):
            print("You're not an admin.", os.getpid())
            rc = admin_access.runAsAdmin(self)
        else:
            print("You are an admin!", os.getpid())
            rc = 0
        return rc

    def runAsAdmin(self,cmdLine=None, wait=True):
        pass


# /////////////////////////////////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////////////////////////////////////////////////////////
# class firewall:
#     def turnOff(self):
#         os.system("NetSh Advfirewall set allprofiles state off")
#
#     def turnOn(self):
#         os.system("NetSh Advfirewall set allprofiles state on")

# /////////////////////////////////////////////////////////////////////////////////////////////////////
class networkscan:
    def openports(self):
        port_min = 0
        port_max = 90
        open_ports = []
        ip_add_entered = "127.0.0.1"
        for port in range(port_min, port_max + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.1)
                    s.connect((ip_add_entered, port))
                    open_ports.append(port)
                    print(port)
            except:
                pass
        for port in open_ports:
            print(f"Port {port} is open on {ip_add_entered}.")

# /////////////////////////////////////////////////////////////////////////////////////////////////////

class systemscan:
    def list_all_file_scan(self):
        a = 1
        for file_name in glob.iglob('/home/kali/PycharmProjects/antimalware/virus/**/**', recursive=True):
        #for file_name in glob.iglob("'%s/Users/**/**'% drive, recursive=True"'C:/Users/kaush/PycharmProjects/antimalware/test/**/**', recursive=True):
        # for file_name in glob.iglob('C:/Users/kaush/**/*.exe', recursive=True):
            Static_Analysis.file_hash(Static_Analysis,file_name)

    # def list_disk_available(self):
    #     dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #     drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    #     return drives

    def full_scan(self):
        # drives = systemscan.list_disk_available(systemscan)
        # for i in drives:
        systemscan.list_all_file_scan(systemscan)

# /////////////////////////////////////////////////////////////////////////////////////////////////////

class Static_Analysis:
    def update_hash(self,latest_version):
        version_list = []
        for file_name in glob.iglob('./hashes/*.txt', recursive=True):
            a = ((re.findall("[0-9]+",str(file_name))))
            version_list.append(int(a[0]))
        version = (max(version_list))
        if version < latest_version:
            for i in range(version+1,latest_version+1):
                os.system("curl https://virusshare.com/hashfiles/VirusShare_0000{0}.md5 > ./hashes/hash{1}.txt".format(i,i+1))

    def file_hash(self,filename):
        try:
            file_md5 = hashlib.md5(open(filename,'rb').read()).hexdigest()
            version = open("/home/kali/PycharmProjects/antimalware/version.txt",'r')
            ver = version.read()
            for i in range(1,int(ver)):
                f = open("/home/kali/PycharmProjects/antimalware/hashes/hash{}.txt".format(i),'r')
                content = f.readlines()
                file_size = (len(content))
                malicious = False
                for i in range(file_size):
                    if str(file_md5)+"\n" == str(content[i]):
                        con = "{0} Malicious file found".format(filename)
                        print("\033[91m {}\033[00m".format(con))
                        malicious = True
                        malicious_files.append(filename)
                        break

            if malicious !=True:
                con = "{0} Good file".format(filename)
                print("\033[92m {}\033[00m".format(con))
        except:
            pass

# /////////////////////////////////////////////////////////////////////////////////////////////////////
# s = systemscan()
# start_time = time.time()
# s.full_scan()
# print("--- %s seconds ---" % (time.time() - start_time))
# def fullscan_button():
#     s = systemscan()
#     start_time = time.time()
#     s.full_scan()
#     print("--- %s seconds ---" % (time.time() - start_time))

# def firewall_button():
#     obj = firewall()
#     obj.turnOn()
#
# def check_admin():
#     ob = admin_access()
#     ob.main_check()

# def port_all_timeup():
#     h = networkscan()
#     h.openports()
#
# fullscan_button()
# check_admin()
# firewall_button()
# port_all_timeup()
# sand = sandbox()
# sand.start()





import hashlib
import os
import socket
# from idlelib.tooltip import Hovertip
import subprocess
# functions end
import time
from tkinter import *
from tkinter.ttk import *

from pandas import read_csv
from selenium import webdriver

from tkinter_custom_button import *


# /////////////////////////////////////////////////////////////////////////////////////////////////////


class ML_model:
    def web_url(self,url):
        sample_url = [url]
        data = read_csv('/home/kali/PycharmProjects/antimalware/urldata.csv')
        data.label.replace("good", 0, inplace=True)
        data.label.replace("bad", 1, inplace=True)
        detect = data['url']
        from sklearn.feature_extraction.text import CountVectorizer
        cv = CountVectorizer()
        x = cv.fit_transform(detect)
        from sklearn.model_selection import train_test_split
        y = data.label
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
        from sklearn.naive_bayes import MultinomialNB
        clf = MultinomialNB()
        clf.fit(X_train, y_train)
        clf.score(X_test, y_test)
        print("Accuracy of Model", clf.score(X_test, y_test) * 100, "%")
        vect = cv.transform(sample_url).toarray()
        output = clf.predict(vect)
        if output == 0:
            # print("not malicious")
            return 0
        else:
            # print("malicious")
            return 1












def spawn_program_and_die(program, exit_code=0):
    # Start the external program
    subprocess.Popen(program)
    # We have started the program, and can suspend this interpreter
    sys.exit(exit_code)


def donothing():
   filewin = Toplevel(des)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def newProgramOpen():
    spawn_program_and_die(['python', 'loginGUI.py'])


def payementsButtonOnClick():
    print("lka")

def privacyButtonOnClick():
    print("lka")

def webButtonOnClick():
    driver = webdriver.Chrome("/home/kali/PycharmProjects/antimalware/chromedriver")
    url = "https://google.com/"
    driver.get(url)
    ml = ML_model()
    while True:
        url_visited = driver.current_url
        url_visited = url_visited.replace("https://www.", "")
        url_visited = url_visited.replace("https://", "")
        url_visited = url_visited.replace("http://", "")
        print(url_visited)
        time.sleep(2)
        if ml.web_url(url_visited) == 0:
            print(url_visited, "not malicious")
        else:
            driver.get("http://malsmart.com")
            print(url_visited, "malicious")

def scanButtonOnClick():
    s = systemscan()
    start_time = time.time()
    s.full_scan()
    print("--- %s seconds ---" % (time.time() - start_time))


# def bar():
#     import time
#     from tkinter import *
#     from tkinter.ttk import *
#     progress = Progressbar(tk, orient=HORIZONTAL, length=100, mode='determinate')
#     progress['value']=20
#     tk.update_idletasks()
#     time.sleep(1)
#     progress['value']=50
#     tk.update_idletasks()
#     time.sleep(1)
#     progress['value']=80
#     tk.update_idletasks()
#     time.sleep(1)
#     progress['value']=100

des = Tk()
des.title("Home Page")
# des.maxsize(width=1050, height=500)
# des.minsize(width=1050, height=500)
des.title("MalSmart Dashboard")
des.geometry("1050x500")

menubar = Menu(des)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Close & New", command=newProgramOpen)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=des.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_separator()
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
des.config(menu=menubar)
label_0 = Label(des, text="You have basic protection",width=20,font=("bold", 20))
label_0.place(x=370,y=23)
label_0.configure(foreground="green")

payementsCustomButton = TkinterCustomButton(master=des,command=payementsButtonOnClick,text='Payments',width=150,height=150).place(x=750,y=170)


privacyCustomButton = TkinterCustomButton(master=des,command=privacyButtonOnClick,text='Privacy',width=150,height=150).place(x=450,y=170)


webCustomButton = TkinterCustomButton(master=des,command=webButtonOnClick,text='Web and Email',width=150,height=150).place(x=150,y=170)


scanCustomButton = TkinterCustomButton(master=des,command=scanButtonOnClick,text='Scan',width=150,height=50).place(x=449,y=410)

def window():
    tk = Tk()
    # progress = Progressbar(tk, orient=HORIZONTAL, length=100, mode='determinate')
    # progress.pack()
    # Button(tk, text='foo', command=bar).pack()
    # mainloop()




framewindow = Button(des, text="Window", command=window)


framewindow.pack()

des.mainloop()
scanButtonOnClick()
