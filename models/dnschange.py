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
		keyring = dns.tsigkeyring.from_text({
		    'host-example.' : 'XXXXXXXXXXXXXXXXXXXXXX=='
		})

		update = dns.update.Update(self.hostname, keyring=keyring)
		update.replace('host', 300, 'a', self.myip)
		response = dns.query.tcp(update, '127.0.0.1')