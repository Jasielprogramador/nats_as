


iptables -nL 

** Esto muestra las reglas que tenemos en el firewall.

iptables -F

** Esto borra todas las reglas que tenemos en iptables. (ya lo he hecho y no se si la he liado)


iptables -P INPUT ACCEPT 

** con esto acptamos todo el trafico, cambiamos el POLICY de DROP que sería digamos bloquear todo el tráfico, que la lista negra sea todo, a NADA.


Si ponemos:

iptables -P INPUT DROP

Con esto hacemos que se bloquee todo el tráfico, y para añadir excepciones, podemos meter por ejemplo que solo lleguen paquetes de nuetra red local, podriamos hacer lo siguiente:


iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT

-A (Append, añadir una regla.)

-j (Jump. Que salte a acetar.)

Si no tenemos esto un usuario de nuetra red local no podria ni hacernos un ping.


Ahora vamos a hacer para que solo nos llegue trafico por un puerto (el puerto 5160 protocolo tcp), sería así:



iptables -A INPUT -p tcp --dport 5160 -j ACCEPT


Como borro una regla?
	

iptables -D INPUT 3 

-D (DELETE)







If you update your firewall rules and want to save the changes, run this command: (CUIDADO)

sudo netfilter-persistent save




Allowing All Incoming SSH

To allow all incoming SSH connections run these commands:

sudo iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT


The second command, which allows the outgoing traffic of established SSH connections, is only necessary if the OUTPUT policy is not set to ACCEPT.


Allowing Incoming SSH from Specific IP address or subnet

To allow incoming SSH connections from a specific IP address or subnet, specify the source. For example, if you want to allow the entire 203.0.113.0/24 subnet, run these commands:


sudo iptables -A INPUT -p tcp -s 203.0.113.0/24 --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT



The second command, which allows the outgoing traffic of established SSH connections, is only necessary if the OUTPUT policy is not set to ACCEPT.











Bloquear ssh


sudo iptables -A INPUT -p tcp -s 35.216.188.54/24 --dport 22 -j ACCEPT



ver las reglas


sudo iptables -L


cambiar la policy 

sudo iptables -P INPUT DROP


borrar todas las reglas 


sudo iptables -F


bloquear un puerto 

$ sudo iptables -A OUTPUT -p tcp --dport 80 -j DROP




bloquear twitter 


buscamos con nslookup twitter.com


$ nslookup twitter.com



$ sudo iptables -A OUTPUT -d 104.244.42.193/24 -j DROP
