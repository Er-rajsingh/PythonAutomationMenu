import os
import getpass

password = getpass.getpass("Enter the password to access this assistant: ")
if password == 'redhat':
    print("\t\t\t Welcome to the python assistant")
    print("\t\t\t -------------------------------")
    x = input("Which system you want to run commands(local/remote): ")
    if x == 'local':
        while (True):
            os.system('clear')
            print("\t\t\t#######################################################")
            print("\t\t\t#<--You are doing Automation on your local computer-->#")
            print("\t\t\t#######################################################")
            print("\t\t\t#-------------You are in main option----------------->#")
            print("\t\t\t#######################################################")
            print("\t\t\t#               Press 0: Stop firewall                #")
            print("\t\t\t#               Press 1: Run date command             #")
            print("\t\t\t#               Press 2: Run cal command              #")
            print("\t\t\t#               Press 3: Setup http server            #")
            print("\t\t\t#               Press 4: Active http server           #")
            print("\t\t\t#               Press 5: Stop http server             #")
            print("\t\t\t#               Press 6: install Hadoop system        #")
            print("\t\t\t#               Press 7: Configure Hadoop Cluster     #")
            print("\t\t\t#               Press 8: Configure YUM                #")
            print("\t\t\t#               Press 9: Docker Options               #")
            print("\t\t\t#               Press 10: Dynamic Storage Folder      #")
            print("\t\t\t#               Press any other key to exit           #")
            print("\t\t\t#######################################################")
            key = input("Enter your choice: ")
            if int(key) == 0:
                os.system('systemctl stop firewalld')
            elif int(key) == 1:
                os.system('date')
            elif int(key) == 2:
                os.system('cal')
            elif int(key) == 3:
                os.system('yum install httpd -y')
                print("Httpd server installed successfully")
            elif int(key) == 4:
                os.system('systemctl start httpd')
                print("httpd server started successfully")
            elif int(key) == 5:
                os.system('systemctl stop httpd')
                print("httpd server stopped")
            elif int(key) == 6:
                os.system('rpm -ivh jdk-8u171-linux-x64.rpm')
                os.system('rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force')
            elif int(key) == 7:
                while (True):
                    os.system('clear')
                    print("\t\t\t#######################################################")
                    print("\t\t\t#<--You are doing Automation on your local computer-->#")
                    print("\t\t\t#######################################################")
                    print("\t\t\t#--------------You are in Hadoop Opt----------------->#")
                    print("\t\t\t#######################################################")
                    print("\t\t\t# Press 1 : To configure the Hadoop System as namenode#")
                    print("\t\t\t# Press 2 : To configure the Hadoop System as datanode#")
                    print("\t\t\t# Press 3 : To configure the hadoop System as Client  #")
                    print("\t\t\t# Press 4 : To start Hadoop Service                   #")
                    print("\t\t\t# Press 5 : To see the report of hadoop cluster       #")
                    print("\t\t\t# Press 6 : To stop the hadoop services               #")
                    print("\t\t\t# Press 7 : To exit                                   #")
                    print("\t\t\t#######################################################")
                    x = input("Enter Your choice: ")
                    if int(x) == 1:
                        foldername = input("enter the folder name you want to create for cluster: ")
                        os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
                        os.system(
                            "echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
                        os.system('echo " " >> /etc/hadoop/hdfs-site.xml')
                        os.system(
                            'echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/hdfs-site.xml')
                        os.system('echo " " >> /etc/hadoop/hdfs-site.xml')
                        os.system('echo "<configuration>" >> /etc/hadoop/hdfs-site.xml')
                        os.system('echo "<property>" >> /etc/hadoop/hdfs-site.xml')
                        os.system('echo "<name>dfs.name.dir</name>" >> /etc/hadoop/hdfs-site.xml')
                        os.system('echo "<value>%s</value>" >> /etc/hadoop/hdfs-site.xml' % foldername)
                        os.system('echo "</property>" >> /etc/hadoop/hdfs-site.xml')
                        os.system('echo "</configuration>" >>/etc/hadoop/hdfs-site.xml')
                        # core-site.xml file configuration
                        os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
                        os.system(
                            "echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
                        os.system('echo " " >> /etc/hadoop/core-site.xml')
                        os.system(
                            'echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/core-site.xml')
                        os.system('echo " " >> /etc/hadoop/core-site.xml')
                        os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
                        os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
                        os.system('echo "<name>fs.default.name</name>" >> /etc/hadoop/core-site.xml')
                        ipaddress = input(
                            "Enter the ip public ipadress and port number in this format - ipaddress:portno. : ")
                        os.system('echo "<value>hdfs://%s</value>" >> /etc/hadoop/core-site.xml' % ipaddress)
                        os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
                        os.system('echo "</configuration>" >>/etc/hadoop/core-site.xml')
                        os.mkdir(foldername)
                        os.system('hadoop namenode -format')
                        os.system('tput setaf 1')
                        print("Your namenode has been configured successfully")
                    elif int(x) == 2:
                        foldername = input("enter the folder name you want to create for cluster: ")
                        os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
                        os.system(
                            "echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
                        os.system('echo " " >> /etc/hadoop/hdfs-site.xml')
                        os.system(
                            'echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/hdfs-site.xml')
                        os.system('echo " " >> /etc/hadoop/hdfs-site.xml')
                        os.system('echo "<configuration>" >> /etc/hadoop/hdfs-site.xml')
                        os.system('echo "<property>" >> /etc/hadoop/hdfs-site.xml')
                        os.system('echo "<name>dfs.data.dir</name>" >> /etc/hadoop/hdfs-site.xml')
                        os.system('echo "<value>%s</value>" >> /etc/hadoop/hdfs-site.xml' % foldername)
                        os.system('echo "</property>" >> /etc/hadoop/hdfs-site.xml')
                        os.system('echo "</configuration>" >>/etc/hadoop/hdfs-site.xml')
                        # core-site.xml configuration
                        os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
                        os.system(
                            "echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
                        os.system('echo " " >> /etc/hadoop/core-site.xml')
                        os.system(
                            'echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/core-site.xml')
                        os.system('echo " " >> /etc/hadoop/core-site.xml')
                        os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
                        os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
                        os.system('echo "<name>fs.default.name</name>" >> /etc/hadoop/core-site.xml')
                        ipaddress = input(
                            "Enter the ip ipadress of master and port number in this format - ipaddress:portno. : ")
                        os.system('echo "<value>hdfs://%s</value>" >> /etc/hadoop/core-site.xml' % ipaddress)
                        os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
                        os.system('echo "</configuration>" >>/etc/hadoop/core-site.xml')
                        os.mkdir(foldername)
                        os.system('tput setaf 1')
                        print("Your datanode has been configured successfully")
                    elif int(x) == 3:
                        os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
                        os.system(
                            "echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
                        os.system('echo " " >> /etc/hadoop/core-site.xml')
                        os.system(
                            'echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/core-site.xml')
                        os.system('echo " " >> /etc/hadoop/core-site.xml')
                        os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
                        os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
                        os.system('echo "<name>fs.default.name</name>" >> /etc/hadoop/core-site.xml')
                        ipaddress = input(
                            "Enter the ip ipadress of master and port number in this format - ipaddress:portno. : ")
                        os.system('echo "<value>hdfs://%s</value>" >> /etc/hadoop/core-site.xml' % ipaddress)
                        os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
                        os.system('echo "</configuration>" >>/etc/hadoop/core-site.xml')
                        os.system('tput setaf 1')
                        print("Your cliet has been configured successfully...")
                    elif int(x) == 4:
                        x = input("namenode/datanode: ")
                        if x == 'namenode' or x == 'Namenode' or x == 'nameNode' or x == 'NAMENODE':
                            os.system('hadoop-daemon.sh start namenode')
                            os.system('tput setaf 3')
                            print("You namenode started successfully..")

                        else:
                            os.system('hadoop-daemon.sh start datanode')
                            os.system('tput setaf 3')
                            print("You namenode started successfully..")
                    elif int(x) == 5:
                        os.system('hadoop dfsadmin -report')
                    elif int(x) == 6:
                        x = input("namenode/datanode: ")
                        if x == 'namenode' or x == 'Namenode' or x == 'nameNode' or x == 'NAMENODE':
                            os.system('hadoop-daemon.sh stop namenode')
                            os.system('tput setaf 3')
                            print("You namenode stopped successfully..")
                        else:
                            os.system('hadoop-daemon.sh stop datanode')
                            os.system('tput setaf 3')
                            print("You namenode stopped successfully..")
                    elif int(x) == 7:
                        break
                    input("press any key to continue... ")
            elif int(key) == 8:
                os.system('echo "[AppStream]" > /etc/yum.repos.d/AppStream.repo')
                os.system('echo "name=App Stream Repo" >> /etc/yum.repos.d/AppStream.repo')
                os.system(
                    'echo "baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream" >> /etc/yum.repos.d/AppStream.repo')
                os.system('echo "enabled=1" >> /etc/yum.repos.d/AppStream.repo')
                os.system('echo "gpgcheck=1" >> /etc/yum.repos.d/AppStream.repo')
                print("Created AppStream Repo")
                os.system('echo "[BaseOS]" > /etc/yum.repos.d/BaseOS.repo')
                os.system('echo "name=BaseOS Repo" >> /etc/yum.repos.d/AppStream.repo')
                os.system(
                    'echo "baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream" >> /etc/yum.repos.d/BaseOS.repo')
                os.system('echo "enabled=1" >> /etc/yum.repos.d/BaseOS.repo')
                os.system('echo "gpgcheck=1" >> /etc/yum.repos.d/BaseOS.repo')
                print("Created AppStream Repo")
                os.system('echo "[docker]" > /etc/yum.repos.d/docker123.repo')
                os.system('echo "name=docker-ce" >> /etc/yum.repos.d/docker123.repo')
                os.system(
                    'echo "baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream" >> /etc/yum.repos.d/docker123.repo')
                os.system('echo "enabled=1" >> /etc/yum.repos.d/docker123.repo')
                os.system('echo "gpgcheck=1" >> /etc/yum.repos.d/docker123.repo')
                print("Created docker repo")
                os.system('yum repolist')
                os.system('yum clean all')
                print("Yum is successfully Configured")
            elif int(key) == 9:
                while (True):
                    os.system('clear')
                    print("\t\t\t#######################################################")
                    print("\t\t\t#<--You are doing Automation on your local computer-->#")
                    print("\t\t\t#######################################################")
                    print("\t\t\t#--------------You are in Docker Opt----------------->#")
                    print("\t\t\t#######################################################")
                    print("\t\t\t# Press 1 : To install Docker                         #")
                    print("\t\t\t# Press 2 : To run docker container                   #")
                    print("\t\t\t# Press 3 : To launch new OS                          #")
                    print("\t\t\t# Press 4 : To start and attach with existing OS      #")
                    print("\t\t\t# Press 5 : To see all the running OS                 #")
                    print("\t\t\t# Press 6 : To see all stopped os                     #")
                    print("\t\t\t# Press 7 : To list all the images you have           #")
                    print("\t\t\t# Press 8 : To stop docker Container                  #")
                    print("\t\t\t# Press 9 : To exit                                   #")
                    print("\t\t\t#######################################################")
                    z = input("Enter Your Choice: ")
                    if int(z) == 1:
                        input(
                            "Make sure that you have configure yum properly. If yes then press entre or first configure it. If you configured then press enter to continue")
                        os.system('yum install docker-ce  --nobest -y')
                    elif int(z) == 2:
                        os.system('systemctl start docker')
                    elif int(z) == 3:
                        osname = input("Enter the OS image name with version in format - osname:version")
                        os.system('docker run -it {}'.format(osname))
                    elif int(z) == 4:
                        os = input("Enter the OS name")
                        os.system('docker start -it {}'.format(os))
                    elif int(z) == 5:
                        os.system('docker ps')
                    elif int(z) == 6:
                        os.system('docker ps -a')
                    elif int(z) == 7:
                        os.system('docker images')
                    elif int(z) == 8:
                        os.system('systemctl stop docker')
                    elif int(z) == 9:
                        break
                    input("Press Entre to continue...")
            elif int(key) == 10:
                while (True):
                    os.system('clear')
                    print("\t\t\t#######################################################")
                    print("\t\t\t#<--You are doing Automation on your local computer-->#")
                    print("\t\t\t#######################################################")
                    print("\t\t\t#------------You are in Partition(LVM) Opt----------->#")
                    print("\t\t\t#######################################################")
                    print("\t\t\t# Press 1 : To list the hard disk available in pc     #")
                    print("\t\t\t# Press 2 : To create new drive                       #")
                    print("\t\t\t# Press 3 : To extend existing drive                  #")
                    print("\t\t\t# Press 4 : To attach new hard disk to the drive      #")
                    print("\t\t\t# Press 5 : To see all the mounted folder             #")
                    print("\t\t\t# Press 6 : To exit                                   #")
                    print("\t\t\t#######################################################")
                    lvm = input("Enter Your Choice: ")
                    if int(lvm) == 1:
                        os.system('fdisk  -l')
                    elif int(lvm) == 2:
                        disk = input("Enter the newly attached hard disk full name eg - /dev/sda: ")
                        os.system('pvcreate ()'.format(disk))
                        print("PV created successfully")
                        folder = input("enter the folder name: ")
                        os.system('vgcreate () {}'.format(folder, disk))
                        print("VG created successfully")
                        partition_name = input("Enter the partiton name you want to give: ")
                        print("400M is here M means MB and just like this you can give 400G/T/M/K")
                        partition_size = input("Enter the partition size in this format - 400M or 20G: ")
                        os.system('lvcreate --size {} --name {}  {}'.format(partition_size, partition_name, folder))
                        os.system('lvdisplay {}'.format(folder, partition_name))
                        os.system('mkfs.ext4 /dev/{}/{}'.formate(folder, partition_name))
                        mount = ("Enter the folder name that you want to link with this partition: ")
                        os.mkdir(mount)
                        res = os.system('mount /dev/{}/{}  /{}'.format(folder, partition_name, mount))
                        if res == o:
                            print("Your drive of {} has been created successfully".format(partition_size))
                        else:
                            print("Some internal error occure please try again")
                    elif int(lvm) == 3:
                        partition_name = input("Enter the existing partiton name you want to increase: ")
                        partition_size = input("Enter the partition size in this format - 400M or 20G: ")
                        folder = input("enter the existing folder nameyou have created before partition: ")
                        os.system('lvextend --size {}  /dev{}/{}'.format(partition_size, folder, partition_name))
                        os.system('resize2fs  /dev{}/{}'.format(partition_size, folder, partition_name))
                        print("Existing drive extended successfully")
                    elif int(lvm) == 4:
                        newdisk = input("Enter the newly attached hard disk full name eg - /dev/sda: ")
                        newfolder = input("enter the folder name: ")
                        os.system('vgextend {} {}'.format(newfolder, newdisk))
                        print("new hard disk attach successfully")
                    elif int(lvm) == 5:
                        os.system('df -l')
                    else:
                        break
                    input("Press any key to Continue...")
            else:
                break
            input("press any key to continue... ")
    elif x == 'remote':
        global y
        y = input("Enter the destination/remote IP: ")
        while (True):
            # os.system('clear')
            print("\t#########################################################################")
            print("\t#-Your Automation applied on remote computer having IP: {}-->#".format(y))
            print("\t#########################################################################")
            print("\t#-------------------You are in main option----------------------------->#")
            print("\t#########################################################################")
            print("\t#               Press 0: Stop firewall                                  #")
            print("\t#               Press 1: Run date command                               #")
            print("\t#               Press 2: Run cal command                                #")
            print("\t#               Press 3: Setup http server                              #")
            print("\t#               Press 4: Active http server                             #")
            print("\t#               Press 5: Stop http server                               #")
            print("\t#               Press 6: install Hadoop system                          #")
            print("\t#               Press 7: Configure Hadoop Cluster                       #")
            print("\t#               Press 8: Configure YUM                                  #")
            print("\t#               Press 9: Configure Docker                               #")
            print("\t#               Press any other key to exit                             #")
            print("\t#########################################################################")
            key = input("Enter your choice: ")
            if int(key) == 0:
                os.system('ssh root@{} systemctl stop firewalld'.format(y))
            elif int(key) == 1:
                os.system('ssh root@{} date'.format(y))
            elif int(key) == 2:
                os.system('ssh root@{} cal'.format(y))
            elif int(key) == 3:
                os.system('ssh root@{} yum install httpd -y'.format(y))
            elif int(key) == 4:
                os.system('ssh root@{} systemctl start httpd'.format(y))
            elif int(key) == 5:
                os.system('ssh root@{} systemctl stop httpd'.format(x))
            elif int(key) == 6:
                os.system('scp /root/jdk-8u171-linux-x64.rpm  root@{}:/root/'.format(y))
                os.system('ssh root@{} rpm -ivh jdk-8u171-linux-x64.rpm'.format(y))
                print("java software installed successfully")
                os.system('scp /root/hadoop-1.2.1-1.x86_64.rpm  root@{}:/root/'.format(y))
                os.system('ssh root@{} rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force'.format(y))
                print("java software installed successfully")
            elif int(key) == 7:
                while (True):
                    # os.system('clear')
                    print("\t#########################################################################")
                    print("\t#-Your Automation applied on remote computer having IP: {}-->#".format(y))
                    print("\t#########################################################################")
                    print("\t#-------------------You are in Hadoop Option--------------------------->#")
                    print("\t#########################################################################")
                    print("\t# Press 1 : To configure the Hadoop System as namenode                #")
                    print("\t# Press 2 : To configure the Hadoop System as datanode                #")
                    print("\t# Press 3 : To configure the hadoop System as Client                  #")
                    print("\t# Press 4 : To start Hadoop Service                                   #")
                    print("\t# Press 5 : To see the report of hadoop cluster                       #")
                    print("\t# Press 6 : To stop the hadoop services                               #")
                    print("\t# Press 7 : To exit                                                   #")
                    print("\t#########################################################################")
                    x = input("Enter Your choice: ")
                    if int(x) == 1:
                        os.system('mkdir /hdfs-site.xml')
                        foldername = input("enter the folder name you want to create for cluster: ")
                        os.system("echo '<?xml version=\"1.0\"?>' > hdfs-site.xml")
                        os.system(
                            "echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
                        os.system('echo " " >> hdfs-site.xml')
                        os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> hdfs-site.xml')
                        os.system('echo " " >> hdfs-site.xml')
                        os.system('echo "<configuration>" >> hdfs-site.xml')
                        os.system('echo "<property>" >> hdfs-site.xml')
                        os.system('echo "<name>dfs.name.dir</name>" >> hdfs-site.xml')
                        os.system('echo "<value>%s</value>" >> hdfs-site.xml' % foldername)
                        os.system('echo "</property>" >> hdfs-site.xml')
                        os.system('echo "</configuration>" >> hdfs-site.xml')
                        os.system('scp /root/hdfs-site.xml  root@{}:/etc/hadoop/hdfs-site.xml'.format(y))
                        os.system('rm -f /root/hdfs-site.xml')
                        # core-site.xml file configuration
                        os.system('mkdir /core-site.xml')
                        os.system("echo '<?xml version=\"1.0\"?>' > core-site.xml")
                        os.system(
                            "echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> core-site.xml")
                        os.system('echo " " >> core-site.xml')
                        os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> core-site.xml')
                        os.system('echo " " >> core-site.xml')
                        os.system('echo "<configuration>" >> core-site.xml')
                        os.system('echo "<property>" >> core-site.xml')
                        os.system('echo "<name>fs.default.name</name>" >> core-site.xml')
                        ipaddress = input(
                            "Enter the ip public ipadress and port number in this format - ipaddress:portno. : ")
                        os.system('echo "<value>hdfs://%s</value>" >> core-site.xml' % ipaddress)
                        os.system('echo "</property>" >> core-site.xml')
                        os.system('echo "</configuration>" >>core-site.xml')
                        os.system('scp /root/core-site.xml  root@{}:/etc/hadoop/core-site.xml'.format(y))
                        os.system('ssh root@{} mkdir {}'.format(y, foldername))
                        print("Formatting namenode")
                        os.system('ssh root@{} hadoop namenode -format'.format(y))
                        os.system('tput setaf 1')
                        print("Your namenode has been configured successfully")
                        os.system('rm -f /root/core-site.xml')
                    elif int(x) == 2:
                        os.system('mkdir /hdfs-site.xml')
                        foldername = input("enter the folder name you want to create for cluster: ")
                        os.system("echo '<?xml version=\"1.0\"?>' > hdfs-site.xml")
                        os.system(
                            "echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
                        os.system('echo " " >> hdfs-site.xml')
                        os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> hdfs-site.xml')
                        os.system('echo " " >> hdfs-site.xml')
                        os.system('echo "<configuration>" >> hdfs-site.xml')
                        os.system('echo "<property>" >> hdfs-site.xml')
                        os.system('echo "<name>dfs.data.dir</name>" >> hdfs-site.xml')
                        os.system('echo "<value>%s</value>" >> hdfs-site.xml' % foldername)
                        os.system('echo "</property>" >> hdfs-site.xml')
                        os.system('echo "</configuration>" >> hdfs-site.xml')
                        os.system('scp /root/hdfs-site.xml  root@{}:/etc/hadoop/hdfs-site.xml'.format(y))
                        os.system('rm -f /root/hdfs-site.xml')
                        # core-site.xml file configuration
                        os.system('mkdir /core-site.xml')
                        os.system("echo '<?xml version=\"1.0\"?>' > core-site.xml")
                        os.system(
                            "echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> core-site.xml")
                        os.system('echo " " >> core-site.xml')
                        os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> core-site.xml')
                        os.system('echo " " >> core-site.xml')
                        os.system('echo "<configuration>" >> core-site.xml')
                        os.system('echo "<property>" >> core-site.xml')
                        os.system('echo "<name>fs.default.name</name>" >> core-site.xml')
                        ipaddress = input(
                            "Enter the ip public ipadress and port number in this format - ipaddress:portno. : ")
                        os.system('echo "<value>hdfs://%s</value>" >> core-site.xml' % ipaddress)
                        os.system('echo "</property>" >> core-site.xml')
                        os.system('echo "</configuration>" >>core-site.xml')
                        os.mkdir(foldername)
                        os.system('hadoop namenode -format')
                        os.system('tput setaf 1')
                        os.system('scp /root/core-site.xml  root@{}:/etc/hadoop/hdfs-site.xml'.format(y))
                        print("Your datanode has been configured successfully")
                        os.system('rm -f /root/core-site.xml')
                    elif int(x) == 3:
                        os.system('mkdir /core-site.xml')
                        os.system("echo '<?xml version=\"1.0\"?>' > core-site.xml")
                        os.system(
                            "echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> core-site.xml")
                        os.system('echo " " >> core-site.xml')
                        os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> core-site.xml')
                        os.system('echo " " >> core-site.xml')
                        os.system('echo "<configuration>" >> core-site.xml')
                        os.system('echo "<property>" >> core-site.xml')
                        os.system('echo "<name>fs.default.name</name>" >> core-site.xml')
                        ipaddress = input(
                            "Enter the ip public ipadress and port number in this format - ipaddress:portno. : ")
                        os.system('echo "<value>hdfs://%s</value>" >> core-site.xml' % ipaddress)
                        os.system('echo "</property>" >> core-site.xml')
                        os.system('echo "</configuration>" >>core-site.xml')
                        os.system('tput setaf 1')
                        os.system('scp /root/core-site.xml  root@{}:/etc/hadoop/core-site.xml'.format(y))
                        os.system('rm -f /root/core-site.xml')
                        print("Your cliet has been configured successfully...")
                    elif int(x) == 4:
                        x = input("namenode/datanode: ")
                        if x == 'namenode' or x == 'Namenode' or x == 'nameNode' or x == 'NAMENODE':
                            os.system('ssh root@{} hadoop-daemon.sh start namenode'.format(y))
                            os.system('tput setaf 3')
                            print("You namenode started successfully..")

                        else:
                            os.system('ssh root@{} hadoop-daemon.sh start datanode'.format(y))
                            os.system('tput setaf 3')
                            print("You namenode started successfully..")
                    elif int(x) == 5:
                        os.system('ssh root@{} hadoop dfsadmin -report'.format(y))
                    elif int(x) == 6:
                        x = input("namenode/datanode: ")
                        if x == 'namenode' or x == 'Namenode' or x == 'nameNode' or x == 'NAMENODE':
                            os.system('ssh root@{} hadoop-daemon.sh stop namenode'.format(y))
                            os.system('tput setaf 3')
                            print("You namenode stopped successfully..")
                        else:
                            os.system('ssh root@{} hadoop-daemon.sh stop namenode'.format(y))
                            os.system('tput setaf 3')
                            print("You namenode stopped successfully..")
                    elif int(x) == 7:
                        break
                    input("Press any key to continue... ")
            elif int(key) == 8:
                os.system(
                    'scp /etc/yum.repos.d/AppStream.repo /etc/yum.repos.d/BaseOS.repo /etc/yum.repos.d/docker123.repo  root@{}:/etc/yum.repos.d'.format(
                        y))
                print("YUM configured successfully")
                os.system('ssh root@{} yum repolist'.format(y))
            elif int(key) == 9:
                while (True):
                    os.system('clear')
                    print("\t\t\t#######################################################")
                    print("\t\t\t#<--You are doing Automation on your local computer-->#")
                    print("\t\t\t#######################################################")
                    print("\t\t\t#--------------You are in Docker Opt----------------->#")
                    print("\t\t\t#######################################################")
                    print("\t\t\t# Press 1 : To install Docker                         #")
                    print("\t\t\t# Press 2 : To run docker container                   #")
                    print("\t\t\t# Press 3 : To launch new OS                          #")
                    print("\t\t\t# Press 4 : To start and attach with existing OS      #")
                    print("\t\t\t# Press 5 : To see all the running OS                 #")
                    print("\t\t\t# Press 6 : To see all stopped os                     #")
                    print("\t\t\t# Press 7 : To list all the images you have           #")
                    print("\t\t\t# Press 8 : To stop docker Container                  #")
                    print("\t\t\t# Press 9 : To exit                                   #")
                    print("\t\t\t#######################################################")
                    z = input("Enter Your Choice: ")
                    if int(z) == 1:
                        input(
                            "Make sure that you have configure yum properly. If yes then press entre or first configure it. If you configured then press enter to continue")
                        os.system('ssh root@{} yum install docker-ce  --nobest -y'.format(y))
                    elif int(z) == 2:
                        os.system('systemctl start docker')
                    elif int(z) == 3:
                        osname = input("Enter the OS image name with version in format - osname:version")
                        os.system('ssh root@{} docker run -it {}'.format(y, osname))
                    elif int(z) == 4:
                        os = input("Enter the OS name")
                        os.system('ssh root@{} docker start -it {}'.format(y, os))
                    elif int(z) == 5:
                        os.system('ssh root@{} docker ps'.format(y))
                    elif int(z) == 6:
                        os.system('ssh root@{} docker ps -a'.format(y))
                    elif int(z) == 7:
                        os.system('ssh root@{} docker images'.format(y))
                    elif int(z) == 8:
                        os.system('ssh root@{} systemctl stop docker'.format(y))
                    elif int(z) == 9:
                        break
                    input("Press Entre to continue...")
            elif int(key) == 10:
                break
            input("Press any key to continue... ")
else:
    print('try again, your password is incorrect')









