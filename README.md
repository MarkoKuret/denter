<!DOCTYPE html>
<html>

<body class="stackedit">
<h1 id="denter-set-up-and-run">DENTER SET-UP AND RUN</h1>
<h2 id="upute-za-pocetak-rada">Upute za pocetak rada</h2>
<blockquote>
<p>upute su pisane s UNIX naredbama, dakle rade na Linuxu, MacOS i Windowsu s intaliranim dodatkon WSL (winows sub-system for linux). Moze se koristiti i “cisiti” Windows vecina naredba je slicna, vjerovatno je efikasnije koristiti WSL.</p>
</blockquote>
<ul>
<li><strong>Set-up Windowsa da radi s Ubuntu terminalom (optional)</strong></li>
</ul>
<ol>
<li>
<p>Prva 4 koraka s tutoriala na linku:<br>
<a href="https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview">https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview</a></p>
</li>
<li>
<p>Konfiguracija aliasa “kratice” za brzi pristup standardnim Windows<br>
folderima</p>
</li>
</ol>
<p><code>nano cd ~ /.bash_aliases</code><br>
<em>umisto mate stavit svoj user direktorij kako se zove</em></p>
<p><code>alias windows='cd /mnt/c/Users/Mate'</code><br>
<em>izades is nano s ctrl x</em></p>
<p><code>windows</code><br>
<em>nova naredba za brzi pristup folderu</em></p>
<ul>
<li><strong>Git</strong></li>
</ul>
<p>Klonirat (kopirat) git repo na lokalno racunalo</p>
<p><code>git clone [https://github.com/MarkoKuret/denter.git](https://github.com/MarkoKuret/denter.git)</code></p>
<ul>
<li><strong>Instaliranje pythona na unix-u</strong></li>
</ul>
<p><code>sudo apt update &amp;&amp; upgrade</code><br>
<code>sudo apt install python3</code><br>
<code>python3-pip ipython3</code></p>
<ul>
<li><strong>Virtualni enviroment</strong></li>
</ul>
<ol>
<li>
<p>preuzimanje<br>
<code>sudo apt install python3-venv</code></p>
</li>
<li>
<p>komanda za kreiranje venva<br>
<code>python3 -m venv venv</code></p>
</li>
<li>
<p>za aktiviranje<br>
<code>source venv/bin/activate</code></p>
</li>
</ol>
<ul>
<li><strong>preuzimanje svih requirementsa</strong></li>
</ul>
<blockquote>
<p>vitual env mora biti aktiviran, sto se vidi po zagradama s nazivom enviromenta (npr. venv) na pocetku linije u terminalu. To takoder vrijedi kod svakog buduceg pokretanja.</p>
</blockquote>
<p><code>python3 -m pip install -r requirements.txt</code></p>
<ul>
<li><strong>pokretanje</strong><br>
<code>python3 pokreni.py</code></li>
</ul>

<ul>
<li><strong>Instanciranje baze</strong><br>
<code>python3 delete_create_db.py</code></li>
</ul>

</body>

</html>
