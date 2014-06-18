class DNSchange:
	import dns.query
	import dns.tsigkeyring
	import dns.update

	hostname = ''
	myip = '127.0.0.1'
	offline = False

	def __init__(self, hostname, myip = '127.0.0.1', offline = False):
		self.hostname = hostname
		self.myip 	  = myip
		self.offline  = offline

	def publish(self):
		#
		# Replace the keyname and secret with appropriate values for your
		# configuration.
		#	
		keyring = dns.tsigkeyring.from_text({
		    'host-example.' : 'XXXXXXXXXXXXXXXXXXXXXX=='
		})

		#
		# Replace "example.com" with your domain, and "MY_HOSTNAME" with your hostname.
		#
		update = dns.update.Update('example.com', keyring=keyring)
		update.replace('MY_HOSTNAME', 300, 'A', self.myip)


		#
		# Replace "127.0.0.1" with the IP address of your master server.
		#
		response = dns.query.tcp(update, '127.0.0.1', timeout=10)