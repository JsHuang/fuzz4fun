# Some fuzzing corpus
## find_samples.py
### about
find files with specific extention and magic  

### usage
find_samples.py extension magic_header folder isBinary urlCount

### quote
https://github.com/joxeankoret/nightmare/blob/master/runtime/find_samples.py  

## list of file signature
https://en.wikipedia.org/wiki/List_of_file_signatures

<table class="wikitable sortable">

<tbody><tr>
<th>Hex signature
</th>
<th>ISO 8859-1
</th>
<th>Offset
</th>
<th>File extension
</th>
<th>Description
</th></tr>
<tr>
<td><pre>a1 b2 c3 d4</pre>
<pre>d4 c3 b2 a1</pre>
</td>
<td><pre>¡²ÃÔ</pre>
<pre>ÔÃ²¡</pre>
</td>
<td>0
</td>
<td>pcap
</td>
<td>Libpcap File Format<sup id="cite_ref-1" class="reference"><a href="#cite_note-1">&#91;1&#93;</a></sup>
</td></tr>
<tr>
<td><pre>0a 0d 0d 0a</pre>
</td>
<td><pre>....</pre>
</td>
<td>0
</td>
<td>pcapng
</td>
<td>PCAP Next Generation Dump File Format<sup id="cite_ref-2" class="reference"><a href="#cite_note-2">&#91;2&#93;</a></sup>
</td></tr>
<tr>
<td><pre>ed ab ee db</pre>
</td>
<td><pre>í«îÛ</pre>
</td>
<td>0
</td>
<td>rpm
</td>
<td>RedHat Package Manager (RPM) package <sup id="cite_ref-3" class="reference"><a href="#cite_note-3">&#91;3&#93;</a></sup>
</td></tr>
<tr>
<td><pre>53 51 4c 69 74 65 20 66 6f 72 6d 61 74 20 33 00</pre>
</td>
<td><pre>SQLite format 3.</pre>
</td>
<td>0
</td>
<td>sqlitedb<br />sqlite<br />db
</td>
<td>SQLite Database <sup id="cite_ref-4" class="reference"><a href="#cite_note-4">&#91;4&#93;</a></sup>
</td></tr>
<tr>
<td><pre>53 50 30 31</pre>
</td>
<td><pre>SP01</pre>
</td>
<td>0
</td>
<td>bin
</td>
<td>Amazon Kindle Update Package <sup id="cite_ref-5" class="reference"><a href="#cite_note-5">&#91;5&#93;</a></sup>
</td></tr>
<tr>
<td><pre>00</pre>
</td>
<td><pre>.</pre>
</td>
<td>0
</td>
<td>PIC<br />PIF<br />SEA<br />YTR
</td>
<td>IBM Storyboard bitmap file<br />
<p>Windows <a href="/wiki/Program_information_file" title="Program information file">Program Information File</a><br />
Mac <a href="/wiki/StuffIt" title="StuffIt">Stuffit</a> Self-Extracting Archive<br />
IRIS <a href="/wiki/Optical_character_recognition" title="Optical character recognition">OCR</a> data file
</p>
</td></tr>
<tr>
<td><pre>00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00</pre>
</td>
<td><pre>........
........
........</pre>
</td>
<td>11
</td>
<td>PDB
</td>
<td><a href="/wiki/PalmPilot" title="PalmPilot">PalmPilot</a> Database/Document File
</td></tr>
<tr>
<td><pre>BE BA FE CA</pre>
</td>
<td><pre>¾ºþÊ</pre>
</td>
<td>0
</td>
<td>DBA
</td>
<td><a href="/wiki/Palm_(PDA)" title="Palm (PDA)">Palm</a> Desktop Calendar Archive
</td></tr>
<tr>
<td><pre>00 01 42 44</pre>
</td>
<td><pre>..BD</pre>
</td>
<td>0
</td>
<td>DBA
</td>
<td>Palm Desktop To Do Archive
</td></tr>
<tr>
<td><pre>00 01 44 54</pre>
</td>
<td><pre>..DT</pre>
</td>
<td>0
</td>
<td>TDA
</td>
<td>Palm Desktop Calendar Archive
</td></tr>
<tr>
<td><pre>00 01 00 00</pre>
</td>
<td><pre>....</pre>
</td>
<td>0
</td>
<td>
</td>
<td>Palm Desktop Data File (<a href="/wiki/Microsoft_Access" title="Microsoft Access">Access</a> format)
</td></tr>
<tr>
<td><pre>00 00 01 00</pre>
</td>
<td><pre>....</pre>
</td>
<td>0
</td>
<td>ico
</td>
<td><a href="/wiki/Computer_icon" class="mw-redirect" title="Computer icon">Computer icon</a> encoded in <a href="/wiki/ICO_(file_format)" title="ICO (file format)">ICO file format</a><sup id="cite_ref-6" class="reference"><a href="#cite_note-6">&#91;6&#93;</a></sup>
</td></tr>
<tr>
<td><pre>66 74 79 70 33 67</pre>
</td>
<td><pre>ftyp3g</pre>
</td>
<td>4
</td>
<td>3gp<br />3g2
</td>
<td>3rd Generation Partnership Project <a href="/wiki/3GPP" title="3GPP">3GPP</a> and <a href="/wiki/3GPP2" class="mw-redirect" title="3GPP2">3GPP2</a> multimedia files
</td></tr>
<tr>
<td><pre>1F 9D</pre>
</td>
<td><pre>..</pre>
</td>
<td>0
</td>
<td>z<br />tar.z
</td>
<td>compressed file (often <a href="/wiki/Tar_(file_format)" class="mw-redirect" title="Tar (file format)">tar</a> zip)<br />
<p>using <a href="/wiki/Lempel-Ziv-Welch" class="mw-redirect" title="Lempel-Ziv-Welch">Lempel-Ziv-Welch</a> algorithm
</p>
</td></tr>
<tr>
<td><pre>1F A0</pre>
</td>
<td><pre>.&#160;</pre>
</td>
<td>0
</td>
<td>z<br />tar.z
</td>
<td>Compressed file (often tar zip)<br />
<p>using <a href="/wiki/LHA_(file_format)" title="LHA (file format)">LZH</a> algorithm
</p>
</td></tr>
<tr>
<td><pre>42 41 43 4B 4D 49 4B 45
44 49 53 4B</pre>
</td>
<td><pre>BACKMIKE
DISK</pre>
</td>
<td>0
</td>
<td>bac
</td>
<td>File or <a href="/wiki/Magnetic_tape_data_storage" title="Magnetic tape data storage">tape</a> containing a <a href="/wiki/Backup" title="Backup">backup</a> done with <a href="/w/index.php?title=AmiBack&amp;action=edit&amp;redlink=1" class="new" title="AmiBack (page does not exist)">AmiBack</a> on an <a href="/wiki/Amiga" title="Amiga">Amiga</a>.
<p>It typically is paired with an index file (idx) with the table of contents.
</p>
</td></tr>
<tr>
<td><pre>42 5A 68</pre>
</td>
<td><pre>BZh</pre>
</td>
<td>0
</td>
<td>bz2
</td>
<td>Compressed file using <a href="/wiki/Bzip2" title="Bzip2">Bzip2</a> algorithm
</td></tr>
<tr>
<td><pre>47 49 46 38 37 61</pre>
<pre>47 49 46 38 39 61</pre>
</td>
<td><pre>GIF87a</pre>
<pre>GIF89a</pre>
</td>
<td>0
</td>
<td>gif
</td>
<td>Image file encoded in the <a href="/wiki/Graphics_Interchange_Format" class="mw-redirect" title="Graphics Interchange Format">Graphics Interchange Format</a> (GIF)<sup id="cite_ref-7" class="reference"><a href="#cite_note-7">&#91;7&#93;</a></sup>
</td></tr>
<tr>
<td><pre>49 49 2A 00</pre> (<a href="/wiki/Endianness#Little-endian" title="Endianness">little endian</a> format)<br /><pre>4D 4D 00 2A</pre> (<a href="/wiki/Endianness#Big-endian" title="Endianness">big endian</a> format)
</td>
<td><pre>II*.</pre>
<pre>MM.*</pre>
</td>
<td>0
</td>
<td>tif<br />tiff
</td>
<td><a href="/wiki/Tagged_Image_File_Format" class="mw-redirect" title="Tagged Image File Format">Tagged Image File Format</a>
</td></tr>
<tr>
<td><pre>49 49 2A 00 10 00 00 00
43 52</pre>
</td>
<td><pre>II*.....
CR</pre>
</td>
<td>0
</td>
<td>cr2
</td>
<td>Canon RAW Format Version 2<sup id="cite_ref-8" class="reference"><a href="#cite_note-8">&#91;8&#93;</a></sup><br />Canon's RAW format is based on the TIFF file format<sup id="cite_ref-9" class="reference"><a href="#cite_note-9">&#91;9&#93;</a></sup>
</td></tr>
<tr>
<td><pre>80 2A 5F D7</pre>
</td>
<td><pre>.*_.</pre>
</td>
<td>0
</td>
<td>cin
</td>
<td><a href="/wiki/Eastman_Kodak" class="mw-redirect" title="Eastman Kodak">Kodak</a> <a href="/wiki/Cineon#Cineon_file_format" title="Cineon">Cineon image</a>
</td></tr>
<tr>
<td><pre>52 4E 43 01</pre>
<pre>52 4E 43 02</pre>
</td>
<td><pre>RNC.</pre>
</td>
<td>0
</td>
<td>
</td>
<td>Compressed file using <a rel="nofollow" class="external text" href="http://segaretro.org/Rob_Northen_compression">Rob Northen Compression</a> (version 1 and 2) algorithm
</td></tr>
<tr>
<td><pre>53 44 50 58</pre> (<a href="/wiki/Endianness#Big-endian" title="Endianness">big endian</a> format)<br />
<pre>58 50 44 53</pre> (<a href="/wiki/Endianness#Little-endian" title="Endianness">little endian</a> format)
</td>
<td><pre>SDPX</pre>
<pre>XPDS</pre>
</td>
<td>0
</td>
<td>dpx
</td>
<td><a href="/wiki/SMPTE" class="mw-redirect" title="SMPTE">SMPTE</a> <a href="/wiki/Digital_Picture_Exchange" title="Digital Picture Exchange">DPX image</a>
</td></tr>
<tr>
<td><pre>76 2F 31 01</pre>
</td>
<td><pre>v/1.</pre>
</td>
<td>0
</td>
<td>exr
</td>
<td><a href="/wiki/OpenEXR" title="OpenEXR">OpenEXR image</a>
</td></tr>
<tr>
<td><pre>42 50 47 FB</pre>
</td>
<td><pre>BPGû</pre>
</td>
<td>0
</td>
<td>bpg
</td>
<td><a href="/wiki/Better_Portable_Graphics" title="Better Portable Graphics">Better Portable Graphics</a> format<sup id="cite_ref-10" class="reference"><a href="#cite_note-10">&#91;10&#93;</a></sup>
</td></tr>
<tr>
<td><pre>FF D8 FF DB</pre><br />
<pre>FF D8 FF E0 00 10 4A 46 49 46 00 01</pre><br /><code>FF D8 FF EE</code>
<pre>FF D8 FF E1&#160;??&#160;?? 45 78 69 66 00 00</pre>
</td>
<td><pre>ÿØÿÛ</pre><br />
<pre>ÿØÿà..JFIF..</pre><br /><code>ÿØÿî</code>
<pre>ÿØÿá..Exif..</pre>
</td>
<td>0
</td>
<td>jpg<br />jpeg
</td>
<td><a href="/wiki/JPEG" title="JPEG">JPEG</a> raw or in the <a href="/wiki/JFIF" class="mw-redirect" title="JFIF">JFIF</a> or <a href="/wiki/Exif" title="Exif">Exif</a> file format
</td></tr>
<tr>
<td><pre>46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 49 4C 42 4D</pre>
</td>
<td><pre>FORM....
ILBM</pre>
</td>
<td>0
<p>any
</p>
</td>
<td>ilbm<br />lbm<br />ibm<br />iff
</td>
<td><a href="/wiki/Interchange_File_Format" title="Interchange File Format">IFF</a> <a href="/wiki/ILBM" title="ILBM">Interleaved Bitmap Image</a>
</td></tr>
<tr>
<td><pre>46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 38 53 56 58</pre>
</td>
<td><pre>FORM....
8SVX</pre>
</td>
<td>0
<p>any
</p>
</td>
<td>8svx<br />8sv<br />svx<br />snd<br />iff
</td>
<td><a href="/wiki/Interchange_File_Format" title="Interchange File Format">IFF</a> <a href="/wiki/8SVX" title="8SVX">8-Bit Sampled Voice</a>
</td></tr>
<tr>
<td><pre>46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 41 43 42 4D</pre>
</td>
<td><pre>FORM....
ACBM</pre>
</td>
<td>0
<p>any
</p>
</td>
<td>acbm<br />iff
</td>
<td><a href="/w/index.php?title=Amiga_Contiguous_Bitmap&amp;action=edit&amp;redlink=1" class="new" title="Amiga Contiguous Bitmap (page does not exist)">Amiga Contiguous Bitmap</a>
</td></tr>
<tr>
<td><pre>46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 41 4E 42 4D</pre>
</td>
<td><pre>FORM....
ANBM</pre>
</td>
<td>0
<p>any
</p>
</td>
<td>anbm<br />iff
</td>
<td><a href="/wiki/Interchange_File_Format" title="Interchange File Format">IFF</a> <a href="/w/index.php?title=IFF_Animated_Bitmap&amp;action=edit&amp;redlink=1" class="new" title="IFF Animated Bitmap (page does not exist)">Animated Bitmap</a>
</td></tr>
<tr>
<td><pre>46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 
41 4E 49 4D</pre>
</td>
<td><pre>FORM....
ANIM</pre>
</td>
<td>0
<p>any
</p>
</td>
<td>anim<br />iff
</td>
<td><a href="/wiki/Interchange_File_Format" title="Interchange File Format">IFF</a> <a href="/w/index.php?title=IFF_CEL_Animation&amp;action=edit&amp;redlink=1" class="new" title="IFF CEL Animation (page does not exist)">CEL Animation</a>
</td></tr>
<tr>
<td><pre>46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 46 41 58 58</pre>
</td>
<td><pre>FORM....
FAXX</pre>
</td>
<td>0
<p>any
</p>
</td>
<td>faxx<br />fax<br />iff
</td>
<td><a href="/wiki/Interchange_File_Format" title="Interchange File Format">IFF</a> <a href="/wiki/Fax" title="Fax">Facsimile Image</a>
</td></tr>
<tr>
<td><pre>46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 46 54 58 54</pre>
</td>
<td><pre>FORM....
FTXT</pre>
</td>
<td>0
<p>any
</p>
</td>
<td>ftxt<br />iff
</td>
<td><a href="/wiki/Interchange_File_Format" title="Interchange File Format">IFF</a> <a href="/wiki/Formatted_text" title="Formatted text">Formatted Text</a>
</td></tr>
<tr>
<td><pre>46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 53 4D 55 53</pre>
</td>
<td><pre>FORM....
SMUS</pre>
</td>
<td>0
<p>any
</p>
</td>
<td>smus<br />smu<br />mus<br />iff
</td>
<td><a href="/wiki/Interchange_File_Format" title="Interchange File Format">IFF</a> <a href="/w/index.php?title=IFF_Simple_Musical_Score&amp;action=edit&amp;redlink=1" class="new" title="IFF Simple Musical Score (page does not exist)">Simple Musical Score</a>
</td></tr>
<tr>
<td><pre>46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 43 4D 55 53</pre>
</td>
<td><pre>FORM....
CMUS</pre>
</td>
<td>0
<p>any
</p>
</td>
<td>cmus<br />mus<br />iff
</td>
<td><a href="/wiki/Interchange_File_Format" title="Interchange File Format">IFF</a> <a href="/w/index.php?title=IFF_Musical_Score&amp;action=edit&amp;redlink=1" class="new" title="IFF Musical Score (page does not exist)">Musical Score</a>
</td></tr>
<tr>
<td><pre>46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 59 55 56 4E</pre>
</td>
<td><pre>FORM....
YUVN</pre>
</td>
<td>0
<p>any
</p>
</td>
<td>yuvn<br />yuv<br />iff
</td>
<td><a href="/wiki/Interchange_File_Format" title="Interchange File Format">IFF</a> <a href="/wiki/YUV" title="YUV">YUV Image</a>
</td></tr>
<tr>
<td><pre>46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 46 41 4E 54</pre>
</td>
<td><pre>FORM....
FANT</pre>
</td>
<td>0
<p>any
</p>
</td>
<td>iff
</td>
<td><a href="/wiki/Amiga" title="Amiga">Amiga</a> <a href="/wiki/Fantavision" title="Fantavision">Fantavision Movie</a>
</td></tr>
<tr>
<td><pre>46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 41 49 46 46</pre>
</td>
<td><pre>FORM....
AIFF</pre>
</td>
<td>0
<p>any
</p>
</td>
<td>aiff<br />aif<br />aifc<br />snd<br />iff
</td>
<td><a href="/wiki/Audio_Interchange_File_Format" title="Audio Interchange File Format">Audio Interchange File Format</a>
</td></tr>
<tr>
<td><pre>49 4E 44 58</pre>
</td>
<td><pre>INDX</pre>
</td>
<td>0
</td>
<td>idx
</td>
<td>Index file to a file or <a href="/wiki/Magnetic_tape_data_storage" title="Magnetic tape data storage">tape</a> containing a <a href="/wiki/Backup" title="Backup">backup</a> done with <a href="/w/index.php?title=AmiBack&amp;action=edit&amp;redlink=1" class="new" title="AmiBack (page does not exist)">AmiBack</a> on an <a href="/wiki/Amiga" title="Amiga">Amiga</a>.
</td></tr>
<tr>
<td><pre>4C 5A 49 50</pre>
</td>
<td><pre>LZIP</pre>
</td>
<td>0
</td>
<td>lz
</td>
<td><a href="/wiki/Lzip" title="Lzip">lzip</a> compressed file
</td></tr>
<tr>
<td><pre>4D 5A</pre>
</td>
<td><pre>MZ</pre>
</td>
<td>0
</td>
<td>exe
</td>
<td><a href="/wiki/DOS_MZ_executable" title="DOS MZ executable">DOS MZ executable</a> file format and its descendants (including <a href="/wiki/New_Executable" title="New Executable">NE</a> and <a href="/wiki/Portable_Executable" title="Portable Executable">PE</a>)
</td></tr>
<tr>
<td><pre>50 4B 03 04</pre><br />
<pre>50 4B 05 06</pre> (empty archive)<br />
<pre>50 4B 07 08</pre> (spanned archive)
</td>
<td><pre>PK..</pre>
</td>
<td>0
</td>
<td>zip<br />jar<br />odt<br />ods<br />odp<br />docx<br />xlsx<br />pptx<br />vsdx<br />apk<br />aar<br />
</td>
<td><a href="/wiki/ZIP_(file_format)" class="mw-redirect" title="ZIP (file format)">zip file format</a> and formats based on it, such as <a href="/wiki/JAR_(file_format)" title="JAR (file format)">JAR</a>, <a href="/wiki/OpenDocument" title="OpenDocument">ODF</a>, <a href="/wiki/Office_Open_XML" title="Office Open XML">OOXML</a>
</td></tr>
<tr>
<td><pre>52 61 72 21 1A 07 00</pre>
</td>
<td><pre>Rar!...</pre><br />
</td>
<td>0
</td>
<td>rar
</td>
<td><a href="/wiki/RAR_(file_format)" title="RAR (file format)">RAR</a> archive version 1.50 onwards<sup id="cite_ref-11" class="reference"><a href="#cite_note-11">&#91;11&#93;</a></sup>
</td></tr>
<tr>
<td><pre>52 61 72 21 1A 07 01 00</pre>
</td>
<td><pre>Rar!....</pre>
</td>
<td>0
</td>
<td>rar
</td>
<td><a href="/wiki/RAR_(file_format)" title="RAR (file format)">RAR</a> archive version 5.0 onwards<sup id="cite_ref-12" class="reference"><a href="#cite_note-12">&#91;12&#93;</a></sup>
</td></tr>
<tr>
<td><pre>7F 45 4C 46</pre>
</td>
<td><pre>.ELF</pre>
</td>
<td>0
</td>
<td>
</td>
<td><a href="/wiki/Executable_and_Linkable_Format" title="Executable and Linkable Format">Executable and Linkable Format</a>
</td></tr>
<tr>
<td><pre>89 50 4E 47 0D 0A 1A 0A</pre>
</td>
<td><pre>.PNG....</pre>
</td>
<td>0
</td>
<td>png
</td>
<td>Image encoded in the <a href="/wiki/Portable_Network_Graphics" title="Portable Network Graphics">Portable Network Graphics</a> format<sup id="cite_ref-13" class="reference"><a href="#cite_note-13">&#91;13&#93;</a></sup>
</td></tr>
<tr>
<td><pre>CA FE BA BE</pre>
</td>
<td><pre>Êþº¾</pre>
</td>
<td>0
</td>
<td>class
</td>
<td><a href="/wiki/Java_class_file" title="Java class file">Java class file</a>, <a href="/wiki/Fat_binary#Apple" title="Fat binary">Mach-O Fat Binary</a>
</td></tr>
<tr>
<td><pre>EF BB BF</pre>
</td>
<td><pre>ï»¿</pre>
</td>
<td>0
</td>
<td>
</td>
<td><a href="/wiki/UTF-8" title="UTF-8">UTF-8</a> encoded <a href="/wiki/Unicode" title="Unicode">Unicode</a> <a href="/wiki/Byte_order_mark" title="Byte order mark">byte order mark</a>, commonly seen in text files.
</td></tr>
<tr>
<td><pre>FE ED FA CE</pre>
</td>
<td><pre>........</pre>
</td>
<td>0
<p>0x1000
</p>
</td>
<td>
</td>
<td><a href="/wiki/Mach-O" title="Mach-O">Mach-O</a> binary (32-bit)
</td></tr>
<tr>
<td><pre>FE ED FA CF</pre>
</td>
<td><pre>........</pre>
</td>
<td>0
<p>0x1000
</p>
</td>
<td>
</td>
<td>Mach-O binary (64-bit)
</td></tr>
<tr>
<td><pre>FE ED FE ED</pre>
</td>
<td><pre>þíþí</pre>
</td>
<td>0
</td>
<td>
</td>
<td>JKS <a rel="nofollow" class="external text" href="http://hg.openjdk.java.net/jdk10/jdk10/jdk/file/777356696811/src/java.base/share/classes/sun/security/provider/JavaKeyStore.java">JavakeyStore</a>
</td></tr>
<tr>
<td><pre>CE FA ED FE</pre>
</td>
<td><pre>........</pre>
</td>
<td>0
</td>
<td>
</td>
<td>Mach-O binary (reverse byte ordering scheme, 32-bit)<sup id="cite_ref-apple.com_14-0" class="reference"><a href="#cite_note-apple.com-14">&#91;14&#93;</a></sup>
</td></tr>
<tr>
<td><pre>CF FA ED FE</pre>
</td>
<td><pre>........</pre>
</td>
<td>0
</td>
<td>
</td>
<td>Mach-O binary (reverse byte ordering scheme, 64-bit)<sup id="cite_ref-apple.com_14-1" class="reference"><a href="#cite_note-apple.com-14">&#91;14&#93;</a></sup>
</td></tr>
<tr>
<td><pre>FF FE</pre>
</td>
<td><pre>..</pre>
</td>
<td>0
</td>
<td>
</td>
<td>Byte-order mark for text file encoded in <a href="/wiki/Little_endian" class="mw-redirect" title="Little endian">little-endian</a> <a href="/wiki/UTF-16" title="UTF-16">16-bit Unicode Transfer Format</a>
</td></tr>
<tr>
<td><pre>FF FE 00 00</pre>
</td>
<td><pre>....</pre>
</td>
<td>0
</td>
<td>
</td>
<td>Byte-order mark for text file encoded in little-endian <a href="/wiki/UTF-32" title="UTF-32">32-bit Unicode Transfer Format</a>
</td></tr>
<tr>
<td><pre>25 21 50 53</pre>
</td>
<td><pre>%!PS</pre>
</td>
<td>0
</td>
<td>ps
</td>
<td><a href="/wiki/PostScript" title="PostScript">PostScript document</a>
</td></tr>
<tr>
<td><pre>25 50 44 46 2d</pre>
</td>
<td><pre>%PDF-</pre>
</td>
<td>0
</td>
<td>pdf
</td>
<td><a href="/wiki/Portable_Document_Format" class="mw-redirect" title="Portable Document Format">PDF document</a><sup id="cite_ref-15" class="reference"><a href="#cite_note-15">&#91;15&#93;</a></sup>
</td></tr>
<tr>
<td><pre>30 26 B2 75 8E 66 CF 11
A6 D9 00 AA 00 62 CE 6C</pre>
</td>
<td><pre>0&amp;²u.fÏ
.¦Ù.ª.bÎl</pre>
</td>
<td>0
</td>
<td>asf<br />wma<br />wmv
</td>
<td><a href="/wiki/Advanced_Systems_Format" title="Advanced Systems Format">Advanced Systems Format</a><sup id="cite_ref-16" class="reference"><a href="#cite_note-16">&#91;16&#93;</a></sup>
</td></tr>
<tr>
<td><pre>24 53 44 49 30 30 30 31</pre>
</td>
<td><pre>$SDI0001</pre>
</td>
<td>0
</td>
<td>
</td>
<td><a href="/wiki/System_Deployment_Image" title="System Deployment Image">System Deployment Image</a>, a disk image format used by <a href="/wiki/Microsoft" title="Microsoft">Microsoft</a>
</td></tr>
<tr>
<td><pre>4F 67 67 53</pre>
</td>
<td><pre>OggS</pre>
</td>
<td>0
</td>
<td>ogg<br />oga<br />ogv
</td>
<td><a href="/wiki/Ogg" title="Ogg">Ogg</a>, an <a href="/wiki/Open-source_license" title="Open-source license">open source</a> media container format
</td></tr>
<tr>
<td><pre>38 42 50 53</pre>
</td>
<td><pre>8BPS</pre>
</td>
<td>0
</td>
<td>psd
</td>
<td>Photoshop Document file, <a href="/wiki/Adobe_Photoshop" title="Adobe Photoshop">Adobe Photoshop</a>'s native file format
</td></tr>
<tr>
<td><pre>52 49 46 46&#160;??&#160;??&#160;??&#160;?? 57 41 56 45</pre>
</td>
<td><pre>RIFF....
WAVE</pre>
</td>
<td>0
</td>
<td>wav
</td>
<td><a href="/wiki/Waveform_Audio_File_Format" class="mw-redirect" title="Waveform Audio File Format">Waveform Audio File Format</a>
</td></tr>
<tr>
<td><pre>52 49 46 46&#160;??&#160;??&#160;??&#160;?? 41 56 49 20</pre>
</td>
<td><pre>RIFF....
AVI.</pre>
</td>
<td>0
</td>
<td>avi
</td>
<td><a href="/wiki/Audio_Video_Interleave" title="Audio Video Interleave">Audio Video Interleave</a> video format
</td></tr>
<tr>
<td><pre>FF FB</pre>
</td>
<td><pre>ÿû</pre>
</td>
<td>0
</td>
<td>mp3
</td>
<td><a href="/wiki/MPEG-1_Layer_3" class="mw-redirect" title="MPEG-1 Layer 3">MPEG-1 Layer 3</a> file without an <a href="/wiki/ID3" title="ID3">ID3</a> tag or with an <a href="/wiki/ID3" title="ID3">ID3v</a>1 tag (which's appended at the end of the file)
</td></tr>
<tr>
<td><pre>49 44 33</pre>
</td>
<td><pre>ID3</pre>
</td>
<td>0
</td>
<td>mp3
</td>
<td><a href="/wiki/MP3" title="MP3">MP3</a> file with an ID3v2 container
</td></tr>
<tr>
<td><pre>42 4D</pre>
</td>
<td><pre>BM</pre>
</td>
<td>0
</td>
<td>bmp<br />dib
</td>
<td><a href="/wiki/BMP_file_format" title="BMP file format">BMP</a> file, a <a href="/wiki/Bitmap" title="Bitmap">bitmap</a> format used mostly in the <a href="/wiki/Windows" class="mw-redirect" title="Windows">Windows</a> world
</td></tr>
<tr>
<td><pre>43 44 30 30 31</pre>
</td>
<td><pre>CD001</pre>
</td>
<td>0x8001<br />
<p>0x8801<br />0x9001
</p>
</td>
<td>iso
</td>
<td><a href="/wiki/ISO9660" class="mw-redirect" title="ISO9660">ISO9660</a> CD/DVD image file<sup id="cite_ref-17" class="reference"><a href="#cite_note-17">&#91;17&#93;</a></sup>
</td></tr>
<tr>
<td><pre>53 49 4D 50 4C 45 20 20</pre>
<pre>3D 20 20 20 20 20 20 20
20 20 20 20 20 20 20 20
20 20 20 20 20 54</pre>
</td>
<td><pre>SIMPLE  
=       
        
     T</pre>
</td>
<td>0
</td>
<td>fits
</td>
<td>Flexible Image Transport System (<a href="/wiki/FITS" title="FITS">FITS</a>)<sup id="cite_ref-18" class="reference"><a href="#cite_note-18">&#91;18&#93;</a></sup>
</td></tr>
<tr>
<td><pre>66 4C 61 43</pre>
</td>
<td><pre>fLaC</pre>
</td>
<td>0
</td>
<td>flac
</td>
<td><a href="/wiki/Free_Lossless_Audio_Codec" class="mw-redirect" title="Free Lossless Audio Codec">Free Lossless Audio Codec</a><sup id="cite_ref-19" class="reference"><a href="#cite_note-19">&#91;19&#93;</a></sup>
</td></tr>
<tr>
<td><pre>4D 54 68 64</pre>
</td>
<td><pre>MThd</pre>
</td>
<td>0
</td>
<td>mid<br />midi
</td>
<td><a href="/wiki/MIDI#Standard_MIDI_files" title="MIDI">MIDI sound file</a><sup id="cite_ref-20" class="reference"><a href="#cite_note-20">&#91;20&#93;</a></sup>
</td></tr>
<tr>
<td><pre>D0 CF 11 E0 A1 B1 1A E1</pre>
</td>
<td>
</td>
<td>0
</td>
<td>doc<br />xls<br />ppt<br />msg
</td>
<td><a href="/wiki/Compound_File_Binary_Format" title="Compound File Binary Format">Compound File Binary Format</a>, a container format used for document by older versions of <a href="/wiki/Microsoft_Office" title="Microsoft Office">Microsoft Office</a>.<sup id="cite_ref-21" class="reference"><a href="#cite_note-21">&#91;21&#93;</a></sup> It is however an open format used by other programs as well.
</td></tr>
<tr>
<td><pre>64 65 78 0A 30 33 35 00</pre>
</td>
<td><pre>dex.035.</pre>
</td>
<td>0
</td>
<td>dex
</td>
<td><a href="/wiki/Dalvik_(software)" title="Dalvik (software)">Dalvik</a> Executable
</td></tr>
<tr>
<td><pre>4B 44 4D</pre>
</td>
<td><pre>KDM</pre>
</td>
<td>0
</td>
<td>vmdk
</td>
<td>VMDK files<sup id="cite_ref-22" class="reference"><a href="#cite_note-22">&#91;22&#93;</a></sup><sup id="cite_ref-23" class="reference"><a href="#cite_note-23">&#91;23&#93;</a></sup>
</td></tr>
<tr>
<td><pre>43 72 32 34</pre>
</td>
<td><pre>Cr24</pre>
</td>
<td>0
</td>
<td>crx
</td>
<td><a href="/wiki/Google_Chrome" title="Google Chrome">Google Chrome</a> extension<sup id="cite_ref-24" class="reference"><a href="#cite_note-24">&#91;24&#93;</a></sup> or packaged app<sup id="cite_ref-25" class="reference"><a href="#cite_note-25">&#91;25&#93;</a></sup>
</td></tr>
<tr>
<td><pre>41 47 44 33</pre>
</td>
<td><pre>AGD3</pre>
</td>
<td>0
</td>
<td>fh8
</td>
<td><a href="/wiki/Adobe_FreeHand" title="Adobe FreeHand">FreeHand</a> 8 document<sup id="cite_ref-26" class="reference"><a href="#cite_note-26">&#91;26&#93;</a></sup><sup id="cite_ref-27" class="reference"><a href="#cite_note-27">&#91;27&#93;</a></sup><sup id="cite_ref-28" class="reference"><a href="#cite_note-28">&#91;28&#93;</a></sup>
</td></tr>
<tr>
<td><pre>05 07 00 00 42 4F 42 4F
05 07 00 00 00 00 00 00
00 00 00 00 00 01</pre>
</td>
<td><pre>....BOBO
........
....</pre>
</td>
<td>0
</td>
<td>cwk
</td>
<td><a href="/wiki/AppleWorks" title="AppleWorks">AppleWorks</a> 5 document
</td></tr>
<tr>
<td><pre>06 07 E1 00 42 4F 42 4F
06 07 E1 00 00 00 00 00
00 00 00 00 00 01</pre>
</td>
<td><pre>....BOBO
........
....</pre>
</td>
<td>0
</td>
<td>cwk
</td>
<td><a href="/wiki/AppleWorks" title="AppleWorks">AppleWorks</a> 6 document
</td></tr>
<tr>
<td><pre>45 52 02 00 00 00</pre>
<pre>8B 45 52 02 00 00 00</pre>
</td>
<td><pre>ER....</pre>
<pre>ãER....</pre>
</td>
<td>0
</td>
<td>toast
</td>
<td><a href="/wiki/Roxio" title="Roxio">Roxio</a> <a href="/wiki/Roxio_Toast" title="Roxio Toast">Toast</a> disc image file, also some .dmg-files begin with same bytes
</td></tr>
<tr>
<td><pre>78 01 73 0D 62 62 60</pre>
</td>
<td><pre>x.s.bb`</pre>
</td>
<td>0
</td>
<td>dmg
</td>
<td><a href="/wiki/Apple_Disk_Image" title="Apple Disk Image">Apple Disk Image</a> file
</td></tr>
<tr>
<td><pre>78 61 72 21</pre>
</td>
<td><pre>xar!</pre>
</td>
<td>0
</td>
<td>xar
</td>
<td><a href="/wiki/Xar_(archiver)" title="Xar (archiver)">eXtensible ARchive</a> format<sup id="cite_ref-29" class="reference"><a href="#cite_note-29">&#91;29&#93;</a></sup>
</td></tr>
<tr>
<td><pre>50 4D 4F 43 43 4D 4F 43</pre>
</td>
<td><pre>PMOCCMOC</pre>
</td>
<td>0
</td>
<td>dat
</td>
<td>Windows Files And Settings Transfer Repository<sup id="cite_ref-30" class="reference"><a href="#cite_note-30">&#91;30&#93;</a></sup>
<p>See also USMT 3.0 (Win XP)<sup id="cite_ref-31" class="reference"><a href="#cite_note-31">&#91;31&#93;</a></sup> and USMT 4.0 (Win 7)<sup id="cite_ref-32" class="reference"><a href="#cite_note-32">&#91;32&#93;</a></sup> User Guides
</p>
</td></tr>
<tr>
<td><pre>4E 45 53 1A</pre>
</td>
<td><pre>NES</pre>
</td>
<td>0
</td>
<td>nes
</td>
<td>Nintendo Entertainment System ROM file<sup id="cite_ref-33" class="reference"><a href="#cite_note-33">&#91;33&#93;</a></sup>
</td></tr>
<tr>
<td><pre>75 73 74 61 72 00 30 30</pre>
<pre>75 73 74 61 72 20 20 00</pre>
</td>
<td><pre>ustar.00</pre>
<pre>ustar  .</pre>
</td>
<td>0x101
</td>
<td>tar
</td>
<td><a href="/wiki/Tar_(computing)" title="Tar (computing)">tar archive</a><sup id="cite_ref-34" class="reference"><a href="#cite_note-34">&#91;34&#93;</a></sup>
</td></tr>
<tr>
<td><pre>74 6F 78 33</pre>
</td>
<td><pre>TOX</pre>
</td>
<td>0
</td>
<td>tox
</td>
<td>Open source portable voxel file<sup id="cite_ref-35" class="reference"><a href="#cite_note-35">&#91;35&#93;</a></sup>
</td></tr>
<tr>
<td><pre>4D 4C 56 49</pre>
</td>
<td><pre>MLVI</pre>
</td>
<td>0
</td>
<td>MLV
</td>
<td><a href="/wiki/Magic_Lantern_(firmware)" title="Magic Lantern (firmware)">Magic Lantern</a> Video file<sup id="cite_ref-36" class="reference"><a href="#cite_note-36">&#91;36&#93;</a></sup>
</td></tr>
<tr>
<td><pre>44 43 4D 01 50 41 33 30</pre>
</td>
<td><pre>DCM PA30</pre>
</td>
<td>0
</td>
<td>
</td>
<td>Windows Update <a rel="nofollow" class="external text" href="http://www.microsoft.com/en-us/download/details.aspx?id=1562">Binary Delta Compression</a><sup id="cite_ref-37" class="reference"><a href="#cite_note-37">&#91;37&#93;</a></sup>
</td></tr>
<tr>
<td><pre>37 7A BC AF 27 1C</pre>
</td>
<td><pre>7z¼¯'</pre>
</td>
<td>0
</td>
<td>7z
</td>
<td>7-Zip File Format
</td></tr>
<tr>
<td><pre>1F 8B</pre>
</td>
<td><pre>..</pre>
</td>
<td>0
</td>
<td>gz<br />tar.gz
</td>
<td><a href="/wiki/GZIP" class="mw-redirect" title="GZIP">GZIP</a> compressed file<sup id="cite_ref-38" class="reference"><a href="#cite_note-38">&#91;38&#93;</a></sup>
</td></tr>
<tr>
<td><pre>FD 37 7A 58 5A 00 00</pre>
</td>
<td><pre>²7zXZ..</pre>
</td>
<td>0
</td>
<td>xz<br />tar.xz
</td>
<td><a href="/wiki/Xz" title="Xz">XZ</a> compression utility<br /> using <a href="/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm" title="Lempel–Ziv–Markov chain algorithm">LZMA2</a> compression
</td></tr>
<tr>
<td><pre>04 22 4D 18</pre>
</td>
<td><pre>."M.</pre>
</td>
<td>0
</td>
<td>lz4
</td>
<td><a href="/wiki/LZ4_(compression_algorithm)" title="LZ4 (compression algorithm)">LZ4 Frame Format</a><sup id="cite_ref-39" class="reference"><a href="#cite_note-39">&#91;39&#93;</a></sup><br />
<p>Remark: LZ4 block format does not offer any magic bytes.<sup id="cite_ref-40" class="reference"><a href="#cite_note-40">&#91;40&#93;</a></sup>
</p>
</td></tr>
<tr>
<td><pre>4D 53 43 46</pre>
</td>
<td><pre>MSCF</pre>
</td>
<td>0
</td>
<td>cab
</td>
<td>Microsoft Cabinet file
</td></tr>
<tr>
<td><pre>53 5A 44 44 88 F0 27 33</pre>
</td>
<td><pre>SZDD....</pre>
</td>
<td>0
</td>
<td>Various. (Replacing the last character of the original file extension with an <a href="/wiki/Underscore" title="Underscore">underscore</a>, e.g. setup.exe becomes setup.ex_)
</td>
<td>Microsoft compressed file in <a href="/wiki/Quantum_compression" title="Quantum compression">Quantum</a> format, used prior to Windows XP.  File can be decompressed using Extract.exe or Expand.exe distributed with earlier versions of Windows.
</td></tr>
<tr>
<td><pre>46 4C 49 46</pre>
</td>
<td><pre>FLIF</pre>
</td>
<td>0
</td>
<td>flif
</td>
<td><a href="/wiki/Free_Lossless_Image_Format" title="Free Lossless Image Format">Free Lossless Image Format</a>
</td></tr>
<tr>
<td><pre>1A 45 DF A3</pre>
</td>
<td><pre>.Eß£</pre>
</td>
<td>0
</td>
<td>mkv<br />mka<br />mks<br />mk3d<br />webm
</td>
<td><a href="/wiki/Matroska" title="Matroska">Matroska</a> media container, including <a href="/wiki/WebM" title="WebM">WebM</a>
</td></tr>
<tr>
<td><pre>4D 49 4C 20</pre>
</td>
<td><pre>MIL </pre>
</td>
<td>0
</td>
<td>stg
</td>
<td>"SEAN&#160;: Session Analysis" Training file. Also used in compatible software "Rpw&#160;: <a href="/wiki/Rowperfect" class="mw-redirect" title="Rowperfect">Rowperfect</a> for Windows" and "RP3W&#160;: ROWPERFECT3 for Windows".
</td></tr>
<tr>
<td><pre>41 54 26 54 46 4F 52 4D&#160;??&#160;??&#160;??&#160;?? 44 4A 56</pre>
</td>
<td><pre>AT&amp;TFORM....DJV</pre>
</td>
<td>0
</td>
<td>djvu<br />djv
</td>
<td><a href="/wiki/DjVu" title="DjVu">DjVu</a> document<br />The following byte is either <code>55</code> (<code>U</code>) for single-page or <code>4D</code> (<code>M</code>) for multi-page documents.
</td></tr>
<tr>
<td><pre>30 82</pre>
</td>
<td><pre>0.</pre>
</td>
<td>0
</td>
<td>der
</td>
<td>DER encoded X.509 certificate
</td></tr>
<tr>
<td><pre>44 49 43 4D</pre>
</td>
<td><pre>DICM</pre>
</td>
<td>0x80
</td>
<td>dcm
</td>
<td><a href="/wiki/DICOM" title="DICOM">DICOM Medical File Format</a>
</td></tr>
<tr>
<td><pre>77 4F 46 46</pre>
</td>
<td><pre>wOFF</pre>
</td>
<td>0
</td>
<td>woff
</td>
<td><a rel="nofollow" class="external text" href="https://www.w3.org/TR/2012/REC-WOFF-20121213/">WOFF File Format 1.0</a>
</td></tr>
<tr>
<td><pre>77 4F 46 32</pre>
</td>
<td><pre>wOF2</pre>
</td>
<td>0
</td>
<td>woff2
</td>
<td><a rel="nofollow" class="external text" href="https://www.w3.org/TR/WOFF2/">WOFF File Format 2.0</a>
</td></tr>
<tr>
<td>
<pre>3c 3f 78 6d 6c 20
</pre>
</td>
<td>
<pre>&lt;?xml 
</pre>
</td>
<td>0
</td>
<td>XML
</td>
<td><a href="/wiki/XML" title="XML">eXtensible Markup Language</a> when using the <a href="/wiki/ASCII" title="ASCII">ASCII</a> character encoding
</td></tr>
<tr>
<td>
<pre>00 61 73 6d
</pre>
</td>
<td>
<pre>.asm
</pre>
</td>
<td>0
</td>
<td>wasm
</td>
<td><a href="/wiki/WebAssembly" title="WebAssembly">WebAssembly</a> binary format<sup id="cite_ref-41" class="reference"><a href="#cite_note-41">&#91;41&#93;</a></sup>
</td></tr>
<tr>
<td>
<pre>cf 84 01
</pre>
</td>
<td>
</td>
<td>0
</td>
<td>lep
</td>
<td><a href="/w/index.php?title=Lepton_image_compression_format&amp;action=edit&amp;redlink=1" class="new" title="Lepton image compression format (page does not exist)">Lepton</a> compressed JPEG image<sup id="cite_ref-42" class="reference"><a href="#cite_note-42">&#91;42&#93;</a></sup>
</td></tr>
<tr>
<td>
<pre>43 57 53
</pre>
<pre>46 57 53
</pre>
</td>
<td>CWS
<p>FWS
</p>
</td>
<td>0
</td>
<td>swf
</td>
<td>flash .swf
</td></tr>
<tr>
<td>
<pre>21 3C 61 72 63 68 3E
</pre>
</td>
<td>!&lt;arch&gt;.
</td>
<td>0
</td>
<td>deb
</td>
<td>linux deb file
</td></tr>
<tr>
<td>
<pre>52 49 46 46&#160;??&#160;??&#160;??&#160;?? 57 45 42 50
</pre>
</td>
<td>RIFF....
<p>WEBP
</p>
</td>
<td>0
</td>
<td>webp
</td>
<td>Google WebP image file
</td></tr>
<tr>
<td><pre>27 05 19 56</pre>
</td>
<td><pre>'..V</pre>
</td>
<td>0
</td>
<td>
</td>
<td>U-Boot / uImage. <a href="/wiki/Das_U-Boot" title="Das U-Boot">Das U-Boot</a> Universal Boot Loader.<sup id="cite_ref-43" class="reference"><a href="#cite_note-43">&#91;43&#93;</a></sup>
</td></tr>
<tr>
<td><pre>7B 5C 72 74 66 31</pre>
</td>
<td><pre>{\rtf1</pre>
</td>
<td>0
</td>
<td>rtf
</td>
<td>Rich Text Format
</td></tr>
<tr>
<td><pre>54 41 50 45</pre>
</td>
<td><pre>TAPE</pre>
</td>
<td>0
</td>
<td>
</td>
<td>Microsoft Tape Format
</td></tr>
<tr>
<td><pre>47</pre>
</td>
<td><pre>G</pre>
</td>
<td>0
<p>0xBC 
</p><p>0x178 
</p><p>...
</p><p>(every 188th byte)
</p>
</td>
<td>ts
<p>tsv
</p><p>tsa
</p>
</td>
<td>MPEG Transport Stream  (MPEG-2 Part 1)
</td></tr>
<tr>
<td><pre>00 00 01 BA</pre>
</td>
<td><pre>....</pre>
</td>
<td>0
</td>
<td>m2p
<p>vob
</p>
</td>
<td>MPEG Program Stream  (MPEG-1 Part 1 (essentially identical) and MPEG-2 Part 1)
</td></tr>
<tr>
<td><pre>00 00 01 BA</pre><pre>47</pre><pre>00 00 01 B3</pre>
</td>
<td><pre>....</pre><pre>G</pre><pre>....</pre>
</td>
<td>0
</td>
<td>mpg
<p>mpeg
</p>
</td>
<td>
<p>MPEG Program Stream
</p><p>MPEG Transport Stream
</p><p>MPEG-1 video and MPEG-2 video  (MPEG-1 Part 2 and MPEG-2 Part 2)
</p>
</td></tr>
<tr>
<td><pre>78 01</pre><pre>78 9C</pre><pre>78 DA</pre>
</td>
<td><pre>....</pre>
</td>
<td>0
</td>
<td>zlib
</td>
<td>
<p>No Compression/low
</p><p>Default Compression
</p><p>Best Compression
</p>
</td></tr>
<tr>
<td>
<pre>62 76 78 32
</pre>
</td>
<td><pre>bvx2</pre>
</td>
<td>0
</td>
<td>lzfse
</td>
<td>LZFSE - Lempel-Ziv style data compression algorithm using Finite State Entropy coding. OSS by Apple.<sup id="cite_ref-44" class="reference"><a href="#cite_note-44">&#91;44&#93;</a></sup>
</td></tr>
<tr>
<td>
<pre>4F 52 43
</pre>
</td>
<td><pre>ORC</pre>
</td>
<td>0
</td>
<td>orc
</td>
<td><a href="/wiki/Apache_ORC" title="Apache ORC">Apache ORC</a> (Optimized Row Columnar) file format
</td></tr>
<tr>
<td>
<pre>4F 62 6A 01
</pre>
</td>
<td><pre>Obj.</pre>
</td>
<td>0
</td>
<td>avro
</td>
<td><a href="/wiki/Apache_Avro" title="Apache Avro">Apache Avro</a> binary file format
</td></tr>
<tr>
<td>
<pre>53 45 51 36
</pre>
</td>
<td><pre>SEQ6</pre>
</td>
<td>0
</td>
<td>rc
</td>
<td><a href="/wiki/RCFile" title="RCFile">RCFile</a> columnar file format
</td></tr>
<tr>
<td>
<pre>65 87 78 56
</pre>
</td>
<td><pre>e.xV</pre>
</td>
<td>0
</td>
<td>
<p>p25
</p><p>obt
</p>
</td>
<td>PhotoCap Object Templates
</td></tr>
<tr>
<td>
<pre>55 55 aa aa
</pre>
</td>
<td><pre>UU¬¬</pre>
</td>
<td>0
</td>
<td>pcv
</td>
<td>PhotoCap Vector
</td></tr>
<tr>
<td>
<pre>78 56 34
</pre>
</td>
<td><pre>xV4</pre>
</td>
<td>0
</td>
<td>
<p>pbt
</p><p>pdt
</p><p>pea
</p><p>peb
</p><p>pet
</p><p>pgt
</p><p>pict
</p><p>pjt
</p><p>pkt
</p><p>pmt
</p>
</td>
<td>PhotoCap Template
</td></tr>
<tr>
<td>
<pre>50 41 52 31
</pre>
</td>
<td><pre>PAR1</pre>
</td>
<td>0
</td>
<td>
</td>
<td><a href="/wiki/Apache_Parquet" title="Apache Parquet">Apache Parquet</a> columnar file format
</td></tr>
<tr>
<td>
<pre>45 4D 58 32
</pre>
</td>
<td><pre>EMX2</pre>
</td>
<td>0
</td>
<td>ez2
</td>
<td><a href="/wiki/E-mu_Emax" title="E-mu Emax">Emulator Emaxsynth</a> samples
</td></tr>
<tr>
<td>
<pre>45 4D 55 33
</pre>
</td>
<td><pre>EMU3</pre>
</td>
<td>0
</td>
<td>ez3
<p>iso
</p>
</td>
<td><a href="/wiki/E-mu_Emulator#The_Emulator_III" title="E-mu Emulator">Emulator III</a> synth samples
</td></tr>
<tr>
<td>
<pre>1B 4C 75 61
</pre>
</td>
<td><pre>.Lua</pre>
</td>
<td>0
</td>
<td>luac
</td>
<td><a href="/wiki/Lua_(programming_language)" title="Lua (programming language)">Lua</a> <a href="/wiki/Bytecode" title="Bytecode">bytecode</a><sup id="cite_ref-45" class="reference"><a href="#cite_note-45">&#91;45&#93;</a></sup>
</td></tr>
<tr>
<td>
<pre>62 6F 6F 6B 00 00 00 00 6D 61 72 6B 00 00 00 00
</pre>
</td>
<td><pre>book....mark....</pre>
</td>
<td>0
</td>
<td>alias
</td>
<td>macOS file Alias<sup id="cite_ref-46" class="reference"><a href="#cite_note-46">&#91;46&#93;</a></sup> (<a href="/wiki/Symbolic_link" title="Symbolic link">Symbolic link</a>)
</td></tr>
<tr>
<td>
<pre>5B 5A 6F 6E 65 54 72 61 6E 73 66 65 72 5D
</pre>
</td>
<td><pre>[ZoneTransfer]</pre>
</td>
<td>0
</td>
<td>Identifier
</td>
<td>Microsoft Zone Identifier for <a rel="nofollow" class="external text" href="https://technet.microsoft.com/en-us/windows/ms537183(v=vs.60)">URL Security Zones</a><sup id="cite_ref-47" class="reference"><a href="#cite_note-47">&#91;47&#93;</a></sup>
</td></tr>
<tr>
<td>
<pre>52 65 63 65 69 76 65 64
</pre>
</td>
<td><pre>Received:</pre>
</td>
<td>0
</td>
<td>eml
</td>
<td>Email Message var5<sup id="cite_ref-48" class="reference"><a href="#cite_note-48">&#91;48&#93;</a></sup>
</td></tr>
<tr>
<td>
<pre>20 02 01 62 A0 1E AB 07 02 00 00 00
</pre>
</td>
<td>
<pre> ..b&#160;.«.....</pre>
</td>
<td>0
</td>
<td>tde
</td>
<td>Tableau Datasource
</td></tr>
<tr>
<td>
<pre>37 48 03 02 00 00 00 00 58 35 30 39 4B 45 59
</pre>
</td>
<td>
<pre>7H......X509KEY</pre>
</td>
<td>0
</td>
<td>kdb
</td>
<td>KDB file
</td></tr>
<tr>
<td>
<pre>28 B5 2F FD
</pre>
</td>
<td>
<pre>(µ/ý</pre>
</td>
<td>0
</td>
<td>zst
</td>
<td><a href="/wiki/Zstandard" title="Zstandard">Zstandard</a> compressed file<sup id="cite_ref-49" class="reference"><a href="#cite_note-49">&#91;49&#93;</a></sup><sup id="cite_ref-50" class="reference"><a href="#cite_note-50">&#91;50&#93;</a></sup>
</td></tr></tbody></table>


