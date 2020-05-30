# Notes

`nano` – szovegszerkeszto
`less` - megmutatja a szoveget uj ablakban
`cat` – shows text

`find .` – show everything below the directory (use with ‘tree’)

parancs + argumentumok (positional vs optional)
optional argumentumok kotojellel (i.e. -l, -ls)

`ln -s NEWNAME OLDNAME` (make a reference for easier use)

fajlmasolas: `cp` +fajlnev
fajlathelyezes: `mv` +fajlnev
fajlatnevezes: `mv +fajlnev
torles: `rm` +fajlnev
mappa torlese: `rm -r` +fajlnev
megnyitas: `open` +fajlnev

`echo “hello word” > output.txt` - fajlba iras felulirja az fajl tartalmat
`>> output.txt` - nem feluliras, hanem hozzaadas

`history` - command historyt tarol

`grep kep2 output.txt` - visszadobja a sorokat a txt-bol amiben szerepel kep2

`history | grep "pip install"` megkeresi a szoveget a historian

`top` - kilistazza a gepen futo folyamatokat (htop szines verzio), q-val lehet kilepni

VIM - command line szovegszerkeszto
escape+:+q+!+enter

interrupt: ctrl+C

`nano bla.sh` - bele lehet irni commandokat
`sh bla.sh` - lefuttatja a commandokat (egy kulsos ablakban futtat majd bezar)
`source bla.sh` - lefuttatja a commandokat es el is tarolja a valtozokat (a terminal ablakban futtat)

```
f=‘alma’
echo $f
```

`head`  - show the first couple line of data

details on bash part:
- CLI vs GUI
- Command-line interfaces (Terminal, Git Bash), command processors (Shell, COMMAND.COM)
- Command prompt
- Folder structure, unix mountpoints
- General command structure, positional and optional arguments
- Commands:
```
pwd
cd
mkdir
rm (-rf)
cp
mv
open
start
xdg-open
less
tail
grep – search tool
history
man
echo
htop
nano
vi (with a special focus on exiting vi and vim)
gzip
gunzip
zcat
cat
sh
source/.
```

- stdin, stdout, stderr
- redirecting stdout
- unix pipelines (just the basics, like ls -l | grep key | less )
- shell scripting basics
- basic parallel processing using & and wait
- sh vs source
- Don’t panic commands (ctrl+c, esc, q, exit, quit) 
Git + Github:- repo
- commit
- remote- commands:
git config --global user.name
git config --global user.email
git init
git status
git add
git reset HEAD
git commit
git log
git checkout
- working with remotes:
git remote add origin
git push origin master
git pull origin master
git clone
- working with multiple remotes
- using percheron1 or percheron2 as remote
- gitignore
- basics of branching
git checkout -b patch
git checkout master
git merge patch
git branch -d patch
- merge conflicts and how to deal with them: git mergetool
- forks and pull requests
python dolgok:Python framework:
- virtualenv (py3 vs py2)
- pip install form pypi, microdata pypi, github
- screenPython:
- Basics (if needed)
lists
tuples
dicts
conditionals
loops
functions
- Assertion
- Handling exceptions
- List comprehension
- Generators
- Pandas basics
read_csv
to_csv
selecting rows, columns
map and lambda functions
groupby
merge
Python for enthusiasts (after bootcamp-hours, if anyone is interested):
- argparse
- multiprocessing
- classes
class variables
class methods
instantiation
instance variables
instance methods
inheritance
open recursion
- requests
- BeautifulSoup


https://info201.github.io/command-line.html#navigating-the-command-line

Frame file:
Frame_id: fc:nincs tax id, ft:van tax id fc+cegjegyzekszam, ft+adoszam (adoszam valtozik, ha megvaltozik az adozasi formaja)
Cegjegyzek szam valtozik ha koltozik masik megyebe
Megvaltozik a cegforma (e.g. kft to bt) lekoveti
Beolvadasokat bekoveti

CPU vs RAM hasznalat

Difference between hard and soft links.
Link are of two types: soft links (symbolic links) or hard links.
Soft Links (symbolic links)
You can make links to files and directories, and you can create links (shortcuts) on different partition and with a different inode number from original.
If the real copy is deleted, the link will not work.
Hard Links
Hard links are for files only; you cannot link to a file on different partition with a different inode number.
If the real copy is deleted the link will work, because it accesses the underlying data the real copy was accessing.

Vi – szovegszerkeszto. Kilepes: “:q!”

Bootcamp

Cd /
Cd srv

Ls -a :relytett mappak

Start GIT: git init

Git status

Git add

git commit -m "add szep.txt to the animals project"
git log

Checkout at earlier version:

git checkout f1b1002cabcf027420ae144a8500361e735f0f50 –- stori.txt

Checkout at branch named patch:

git checkout -b patch

Merge conflict:
Delete file in my computer, accept merge, go back to previous version and copy the deleted file back to folder

On branch master you can merge the branch:
git merge patch

Delete branch:
git branch -d patch

Clone:
git clone https://github.com/rgyuri/ba-pre-session-2019.git

Ignore some files: Add gitignore in python repository
less .gitignore

Push and pull git:
git push
git pull

Ask for bead argument help:
bead -h

Create bead:
bead new try_bead_ruzicska

Check status:
bead status (very slow)

Set input:
bead input add “name of input”

Add new beadbox (bead folder, where beads are saved):
bead box add -h 
bead box add main /srv/dropbox_encrypted/bead-box
bead input add “name of bead”

Run shell:
sh "filename.sh"

Create file:
echo "cp input/oligarch_networks/oligarcha_color.csv output/data.csv" > main.sh

Develop: (no input, no output)
bead develop try_bead_david

Ask for output as well:
bead develop try_bead_david –x

Delete the input of bead
bead input delete “name_of_input”

Create a timestamped bead version:
bead save

Load input:
bead input load
(After loading create input, output, temp folders using mkdir)

Shut down process:
ctr-C

Delete inputs:
bead input unload

Delete bead:b
bead nuke “nameofbead”

File that contains main codes:
main.sh

Get help about python file for argument parsing:
python timemachine_mp.py -h

Create s which runs in background:
screen

Resume screen:
screen -r

Exit screen:
Ctr+A+D

Shut down (terminate) and exit screen:
Ctr+D

Create virtual environment:
virtualenv “name of virtualenv” -p python3
Ppython2: virtualenv “env”

Activate virtual environment:
. [‘name_of_environment’]/bin/activate

Here, you can install whatever you want:
e.g. pip3 install tqdm

Requirements:
less requirements.txt

Install requirements for virtual environment:
pip3 install -r requirements.txt

Install every requirement that lies in a folder (as files):
pip install -r requirements_packages.txt -f packages/

Run python:
python3 nameoffile.py

Show downloaded libraries for python:
pip freeze

Show detailed result of tests:
python3 testing.py -v

dataframe.fillna(method=ffill)
grep ‘minta’ filename

List the currently downloaded python packages:
pip freeze -> requirements.txt

Show executable paths:
echo $PATH

Percheron:
30 GB RAM
16 Mag
Pure percheron:
86 GB RAM
44 Mag
Ki mit futtat es mit zabál - alul mutatja
CPU - 1600 lehet , 16 mag miatt

Alias:”less .bash_profile (.bash_rc in linux)” -> mindig lefut terminal nyitaskor hogy
Ebbe a file-ba kell beleirni az aliast:
alias bead='/srv/dropbox_encrypted/bead-box/bead'
Now, bead is not an alias but it is on the executable paths -> shell looks for executable ‘bead’ and runs that (and not as an alias) To see executable path: $PATH (It is located in /usr/local/bin)
sudo ->rootkent (super user) es nem sima userkent akarok utasitast vegezni
Save and exit nano: Ctr-O, enter, Ctr-X
Unzip GZ files: gunzip

Frame ID -> ha egy ceg (entitas) atalakul akkor is marad a Frame ID
Tax ID atalakul -> Egy tax ID alatt lehet tobb ceg is 

Frame IDhez tobb tax ID ahhoz tobb ceg ID – legvaltozekonnyabb, akkor is valtozik ha elkoltozik
Frame ID tartalmazza az (OPTENes) adoszamot, mig a ‘source’ oszlop a cegjegyzek szamot
Scroll in screen: ctrl + a, aztán Esc, és utána lehet görgetni és újabb Esc-el kilövi a görgetést

