<h1>Register Summary</h1>

<table>
<tr>
<th>Register<br>name</th>
<th>Address<br>(hex)</th>
<th>bit<br>7</th>
<th>bit<br>6</th>
<th>bit<br>5</th>
<th>bit<br>4</th>
<th>bit<br>3</th>
<th>bit<br>2</th>
<th>bit<br>1</th>
<th>bit<br>0</th>
<th>Reset<br>value</th>
<th>Access</th>
</tr>
<tr>
<td class="reggen_name">CTRL</td>
<td class="reggen_addr">0Ah</td>
<td class="reggen_bit" colspan="2">RES</td>
<td class="reggen_bit" colspan="1">AID</td>
<td class="reggen_bit" colspan="2">RES</td>
<td class="reggen_bit" colspan="1">ITOD</td>
<td class="reggen_bit" colspan="1">ITP</td>
<td class="reggen_bit" colspan="1">RES</td>
<td class="reggen_reset">00h</td>
<td class="reggen_access">RW</td>
</tr>
</table>


<h1>Register description</h1>


<h2>CTRL - 0Ah</h2>

<p>Configuration register</p>

<p>Access: RW</p>

<p>Reset Value: 00h</p>

<table>
<tr>
<th>bit<br>7</th>
<th>bit<br>6</th>
<th>bit<br>5</th>
<th>bit<br>4</th>
<th>bit<br>3</th>
<th>bit<br>2</th>
<th>bit<br>1</th>
<th>bit<br>0</th>
</tr>
<tr><td class="reggen_bit" colspan="2">RES</td>
<td class="reggen_bit" colspan="1">AID</td>
<td class="reggen_bit" colspan="2">RES</td>
<td class="reggen_bit" colspan="1">ITOD</td>
<td class="reggen_bit" colspan="1">ITP</td>
<td class="reggen_bit" colspan="1">RES</td>
</tr>
</table>

<h3>bit 7-6 - RES</h3>

<p>Reserved, reads 0</p>

<h3>bit 5 - AID</h3>

<p>Automatic address pointer increment disable</p>
<table>
<tr>
<th>Value</th>
<th>Function</th>
</tr>
<tr>
<td class="reggen_bitval">0</td>
<td class="reggen_bitfn">Address auto increment enabled</td>
</tr><tr>
<td class="reggen_bitval">1</td>
<td class="reggen_bitfn">Address auto increment disabled</td>
</tr></table>

<h3>bit 4-3 - RES</h3>

<p>Reserved, reads 0</p>

<h3>bit 2 - ITOD</h3>

<p>Interrupt pin open-drain</p>
<table>
<tr>
<th>Value</th>
<th>Function</th>
</tr>
<tr>
<td class="reggen_bitval">0</td>
<td class="reggen_bitfn">Push-pull interrupt output</td>
</tr><tr>
<td class="reggen_bitval">1</td>
<td class="reggen_bitfn">Open-drain interrupt output (ITP ignored, active-low)</td>
</tr></table>

<h3>bit 1 - ITP</h3>

<p>Interrupt output polarity, ignored if ITOD=1</p>
<table>
<tr>
<th>Value</th>
<th>Function</th>
</tr>
<tr>
<td class="reggen_bitval">0</td>
<td class="reggen_bitfn">Active-low</td>
</tr><tr>
<td class="reggen_bitval">1</td>
<td class="reggen_bitfn">Active-high</td>
</tr></table>

<h3>bit 0 - RES</h3>

<p>Reserved, reads 0</p>
