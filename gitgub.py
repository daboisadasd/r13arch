import time
import os
device = input("Please type the device you would like to erase, usually /dev/mmcb1kx or /dev/sdx")
def rn(code):
	os.system(code)
rn("umount "+device+"*")
print("Press the letter g then press enter")
print("Press the letter w then press enter")
rn("fdisk "+device)
t = input("Press enter")
rn("cgpt create "+device)
time.sleep(.5)
rn("cgpt add -i 1 -t kernel -b 8192 -s 65536 -l Kernel -S 1 -T 5 -P 10 "+device)
rn('cgpt show '+device+' | grep "Sec GPT table"')
xxxxx = input("Type the large number you see above: ")
hmm = ("cgpt add -i 2 -t data -b 73728 -s `expr "+xxxxx+" - 73728` -l Root "+device)
rn(hmm)
rn("partx -a "+device)
rn("mkfs -t ext4 '+device+'p2")
rn("cd /tmp")
rn("curl -LO http://os.archlinuxarm.org/os/ArchLinuxARM-oak-latest.tar.gz")
rn("mkdir root")
rn("mount '+device+'p2 root")
rn("tar -xf ArchLinuxARM-oak-latest.tar.gz -C root")
rn("dd if=root/boot/vmlinux.kpart of='+device+'p1")
rn('echo "Setup commands: wifi-menu, pacman-key --init, pacman-key --init --populate archlinuxarm" > /tmp/root/home/setup.txt')
rn('unmount root')
rn('sync')
