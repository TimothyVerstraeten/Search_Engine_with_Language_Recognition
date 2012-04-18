"""
Cache (contains all the pages which are available to the Search Engine). (extendable)
author:		Verstraeten Timothy
date:		04/14/2012
"""



cache = {
   'http://timosenginetest.com/index.html': """<html>
<body>
<h1>Timo's Engine Test</h1>
Welcome to Timo's Engine Test. This engine is designed to be extended with more languages, so feel free to try it in your own native language.
Since the algorithm to 'guess' the language is probably the easiest I could think of, it won't always give the right answer.
Although these pages aren't long, try to make pages with a lot of text and take a big text as input for the language you want to add (like the Shakespeare script).
<p>
English:
<ul>
<li> <a href="http://timosenginetest.com/barack_obama.html">Barack Obama</a>
</ul>
Dutch:
<ul>
<li> <a href="http://timosenginetest.com/barack_obama_dutch.html">Barack Obama (Dutch Translation)</a>
<li> <a href="http://timosenginetest.com/manneken_pis.html">Manneken Pis</a>
</ul>
Italian:
<ul>
<li> <a href="http://timosenginetest.com/pizza.html">Pizza</a>
</ul>
French:
<ul>
<li> <a href="http://timosenginetest.com/tour_eiffel.html">Tour Eiffel</a>
</ul>
German:
<ul>
<li> <a href="http://timosenginetest.com/berlin_wall.html">Berlin Wall</a>
</ul>
Spanish:
<ul>
<li> <a href="http://timosenginetest.com/real_madrid.html">Real Madrid</a>
</ul>
Portuguese:
<ul>
<li> <a href="http://timosenginetest.com/porto.html">Porto</a>
</ul>
<i>Source: Wikipedia</i>
</body>
</html>





""", 
   'http://timosenginetest.com/barack_obama.html': """<html>
<body>
<h1>Yes we can</h1>
<p>
Barack Obama announced his candidacy for the presidency of the United States in Springfield, Illinois, on February 10, 2007.
On November 4, 2008, Obama won the election, making him the President-elect and the first African American elected President of the United States.

Peter tried to become president of the United States himself to get one step closer to world domination,... but failed.
</p>
</body>
</html>





""", 
   'http://timosenginetest.com/barack_obama_dutch.html': """<html>
<body>
<h1>Yes we can (Dutch Translation)</h1>
<p>
Barack Obama kondigde zijn kandidatuur voor het presidentschap van de Verenigde Staten in Springfield, Illinois, op 10 februari 2007.
Op 4 november 2008, Obama won de verkiezingen, waardoor hij de verkozen voorzitter en de eerste Afro-Amerikaanse verkozen president van de Verenigde Staten.

Peter probeerde zelf president van the United States te worden voor zijn plan voor wereld overheersing,... maar faalde.
</p>
</body>
</html>





""", 
   'http://timosenginetest.com/manneken_pis.html': """<html>
<body>
<h1>Manneken Pis</h1>
<p>
Manneken Pis is een standbeeldje in het centrum van Brussel en stelt een plassend jongetje voor. Het 58 cm grote ventje op een sokkel is geplaatst aan de hoek van de Stoofstraat en de Eikstraat, niet ver van de Grote Markt.
</p>
</body>
</html>





""", 
   'http://timosenginetest.com/pizza.html': """<html>
<body>
<h1>Pizza</h1>
<p>
La pizza e un prodotto gastronomico che ha per base un impasto di acqua farina di frumento, e lievito, che dopo una lievitazione di almeno ventiquattr'ore vienne lavorato fino a ottenere una forma piatta, cotto al forno e variamente condito.

Peter likes pizza too!
</body>
</html>





""", 
   'http://timosenginetest.com/tour_eiffel.html': """<html>
<body>
<h1>Tour Eifel</h1>
<p>
La tour Eiffel est une tour de fer puddle de 324 metres de hauteur (avec antennes) situee a Paris, a l'extremite nord-ouest du parc du Champ-de-Mars en bordure de la Seine.

Peter wanted to demolish the monument, but failed.
</p>
</body>
</html>





""", 
   'http://timosenginetest.com/berlin_wall.html': """<html>
<body>
<h1>Berlin Wall</h1>
<p>
Die Berliner Mauer war wahrend der teilung deutschlands mehr als 28 Jahre lang ein Grenzbefestigungssystem, das alle drei Westsektoren Berlins umschloss und diese von dem Ostteil der Stadt sowie der umgebenden Deutschen Demokratischen Republik.

Just like the Tour Eiffel, Peter tried to destroy it to make space for his Federated States of Peter.
</p>
</body>
</html>





""", 
   'http://timosenginetest.com/real_madrid.html': """<html>
<body>
<h1>Real Madrid</h1>
<p>
El Real Madrid Club de Futbol, mas conocido como Real Madrid, es una entidad polideportiva con sede en Madrid, Espana. Fue fundado el 6 de marzo de 1902 por los hermanos catalanes: Juan Padros y Carlos Padros, bajo el nombre de Madrid Foot Ball Club.

Peter wants to rename the club to "F.C. Real Peter".
</p>
</body>
</html>





""", 
   'http://timosenginetest.com/porto.html': """<html>
<body>
<h1>Porto</h1>
<p>
O vinho do Porto e um vinho natural e fortificado, produzido exclusivamente a partir de uvas provenientes da regiao demarcada do Douro, no norte de Portugal a cerca de 100 km a leste da cidade do Porto.
Regua e Pinhao sao os principais centros de producao, mas algumas das melhores vinhas ficam na zona mais a leste.

Peter likes porto!
</p>
</body>
</html>





""", 
}
