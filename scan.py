import time
import glob
import hashlib
import os
import socket
import pickle
import  re
# from idlelib.tooltip import Hovertip
import subprocess
# functions end
import time
malicious_files = []
f = open("Malicious_log.txt", "a")

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
                        # print("\033[91m {}\033[00m".format(con))
                        print("!!!!!!!! {}!!!!!!!!!!!!!!!!!".format(con))
                        malicious = True
                        malicious_files.append(filename)
                        break

            if malicious !=True:
                con = "{0} Good file".format(filename)
                # print("\033[92m {}\033[00m".format(con))
                print(con)
                print("llllllllllllll==",malicious_files)
                # f.write(malicious_files)
                # try:
                #     f.write("\n".join(str(item) for item in malicious_files))
                #     f.close()
                # except Exception as e:
                #     print(e)


            # f = open("Malicious_log.txt", "w")
            # f.write(malicious_files)
            # f.close()
        except:
            pass

def scanButtonOnClick():
    s = systemscan()
    start_time = time.time()
    s.full_scan()
    try:
        f.write("\n".join(str(item) for item in malicious_files))
        f.close()
    except Exception as e:
        print(e)
    print("--- %s seconds ---" % (time.time() - start_time))

scanButtonOnClick()