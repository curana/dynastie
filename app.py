from flask import Flask
from models.dnschange import DNSchange

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_index():
	dnschange = DNSchange('example.com', '127.0.0.1')

	if dnschange.publish() == True:
		return "Done."
	else:
		return "Failed."

@app.route('/', methods=['POST'])
def post_index():
	dnschange = DNSchange('example.com', '127.0.0.1')

if __name__ == '__main__':
	app.run(
		host = '127.0.0.1',
		port = 80
	)