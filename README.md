#bashplotlib
*plotting in the terminal*

<p>Why I wrote it. What you can use it for.</p>

#installation
<h5>install with pip</h5>
<pre>
	$ pip install bashplotlib
</pre>
<h5>install from source</h5>
<pre>
	$ git clone git@github.com:glamp/bashplotlib.git
	$ cd bashplotlib
	$ python setup.py install
</pre>

<p>This will install the bashplotlib python package and will also add <code>hist</code> and <code>scatter</code> 
to your python scripts folder. This folder should be on your path (add it if it's not).</p>

#examples
<pre>scatter -f data/texas.txt --pch .</pre>
    ------------------------------------------
	|             . . . . . .                 |
	|             .         .                 |
	|             .         .                 |
	|             .         . .               |
	|             .           . . . . . . .   |
	|             .                 . . . . . |
	|             .                           |
	|             .                           |
	| . .   .   . .                           |
	|   . .                                   |
	|     . .                                 |
	|       . .                               |
	|       . .     . . .                 . . |
	|         . . .     . .               . . |
	|           . .       .           . . .   |
	|                     . .       . .       |
	|                       .     . .         |
	|                       . .   . .         |
	|                         .   . .         |
	|                         . . . .         |
	------------------------------------------


<pre>hist data/exp.txt</pre>
	461 | o                
	438 | o                
	415 | o                
	392 | o                
	369 | o                
	346 | o                
	323 | o                
	300 | o                
	277 | o                
	254 | o o              
	231 | o o              
	208 | o o              
	185 | o o              
	162 | o o              
	139 | o o              
	116 | o o o            
	93  | o o o            
	70  | o o o o          
	47  | o o o o          
	24  | o o o o o        
	1   | o o o o o o o o  
	     ------------------


<pre>scatter -x data/x_test.txt -y data/y_test.txt</pre>
	--------------------------------------------
	|       x           |                       |
	|                   |                       |
	|                   |         x             |
	|                   |                       |
	|                   |                       |
	| x               x |                       |
	|                   |                       |
	| - - - - - - - - - o - - - - - - - - - - - |
	|                   |                       |
	|                   |                       |
	|                   |                       |
	|           x       |                       |
	|                   |       x               |
	|                   |                       |
	|                   |                       |
	|                   |                       |
	|                   |                       |
	|                   |                       |
	|                   |                       |
	|                   |                 x     |
	|                   |                     x |
	--------------------------------------------
<pre>scatter -f data/lower48.txt -s 40 --pch .</pre>
	----------------------------------------------------------------------------------
	|     . .   . . . . . . . . . . . . . . . . .                                     |
	|   . .         .               .         . . . . .   .                           |
	| . . .       . .               .         .     . . . .                           |
	|   . .       . .               .         .       .                             . |
	|   .         . . .             .         .     . .                           .   |
	|   . . . . . .   .             . . . . . .     . . . .                       .   |
	|   . . . .   .   .             .         .     .     .                     . .   |
	|   .         .   . . . . . . . .         .     .     .                 . . . . . |
	|   .         .     . .         .         .     . .   .               .   . . . . |
	|   .         .       .         .         . . . . .   .             . .   . . . . |
	|   .                 .         . . . . . .       .   .           . . .   . . .   |
	|   .                 .         .         .       . . .           .       .   .   |
	|   . . . . . . . . . .         .         .       .   . . . . . . . . . . . . .   |
	|   .     .       .   . . . . . . .       . .     .   .   . . . .       . . . .   |
	|   .                   .         .       . . . . .   .   .     .       . .       |
	|   .     .       .     .         . . . . . .     .   .   .     . . . . . .       |
	|   .     .       .     .         .         .     .   .   .   . . . . . .         |
	|   .     .       .     .         .         .     .   .   . . .   . . . .         |
	|     . . . .     .     .         .         .     . . . . .   . . . . . .         |
	|     .     .     .     .         .         .       . . .     . .     .           |
	|     . .     .   . . . . . . . . . . . . . .       . . .   . . .     .           |
	|     . .       . .               . . .     . . . . . . . . . . . . . .           |
	|       .       . .     .         .   .     .     . .       . .     . .           |
	|       .       . .     .         .   .     .     . . . . . . . .   . .           |
	|       . .       .     .         .   .     .     .   .   . . . . . . .           |
	|         . .     .     .         .   . . . .     .   .   .   .   . .             |
	|           . . . .     .         .         . . . .   .   .   .   .               |
	|             . . .     .         .           .   .   .   .   . . .               |
	|                 .         . . . .           .   .   .   .     .                 |
	|                     . . . .                 . . .   .   .   . .                 |
	|                             .               . . . . . . . . . .                 |
	|                             .               .   . . . . . . .                   |
	|                             . . . .       . . . . .     . .   .                 |
	|                               . . .     . .     . .       . . .                 |
	|                                   .     . .                 . .                 |
	|                                     . . .                   . .                 |
	|                                     . .                     . .                 |
	|                                     . .                     . .                 |
	|                                       . .                   . .                 |
	|                                                               .                 |
	----------------------------------------------------------------------------------

#todos
	- colors for individual points
	- line charts
	- trendlines

