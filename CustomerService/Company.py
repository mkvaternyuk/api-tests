import unittest
import requests
import time, sys


class BaseTest(unittest.TestCase):
	def setUp(self):
		self.startTime = time.time()

	def tearDown(self):
		t = time.time() - self.startTime
		#print "%s: %.3f" % (self.id(), t)
		sys.stdout.write("%.3fs " % t)
		sys.stdout.flush()


#class CalcTest(BaseTest):	
#	def test_add(self):
#		time.sleep(1)
#		self.assertEqual(calc.add(1, 2), 3)
        
#	def test_sub(self):
#		self.assertEqual(calc.sub(4, 2), 2)
        
#	def test_mul(self):
#		time.sleep(0.5)
#		self.assertEqual(calc.mul(2, 5), 10)
        
#	def test_div(self):
#		self.assertEqual(calc.div(8, 4), 2)


class AccountTest(BaseTest):
	URL = 'http://localhost:8080/api/v0.5'
	cookies = None
	def setUp(self):		
		self.logout()
		self.login()
		super(AccountTest, self).setUp()
				
	def logout(self):
		r = requests.get(self.URL+'/logout')
		#print r.status_code
		#print r.headers['content-type']

		#print r.encoding
		#print r.text
		#resp = r.json()
		#print resp
		#print resp['response']['message']

	def login(self):
		data = {
			'email': 'szhitansky@gmail.com',
			'password': 'password'
		}
		r = requests.post(self.URL + '/login', data=data)
		self.cookies = r.cookies
		#print r.text

	def test_getCompanies(self):
		r = requests.get(self.URL+'/customer_service/companies', cookies=self.cookies)
		
		self.assertEqual(r.status_code, 200)
		
		e = True if len(r.text) > 0 else False 
		self.assertEqual(e, True)
		#print len(r.text)
	
	def test_getCompaniesFilter(self):
		r = requests.get(self.URL+'/customer_service/companies/filter/list?company_type=PARTNER', cookies=self.cookies)
		
		self.assertEqual(r.status_code, 200)
		
		resp = r.json()
		e = True if len(resp['response']) > 0 else False 
		self.assertEqual(e, True)


        
if __name__ == '__main__':
    unittest.main()

# easy_install pyrg
# python -m unittest -v Company |& pyrg

