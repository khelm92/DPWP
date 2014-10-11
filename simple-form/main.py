'''

Kasey Helm
DPW
10/10/14
Simple Form Assignment

'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = ''' <!DOCTYPE HTML>
        <html>
            <head>
                <title>Simple Form</title>
            </head>
            <body>'''
            
        page_body = '''<h3>Contest Entry</h3>
        
                        <form method="GET" action="">
                            <label>First Name: </label><input type="text" name="firstname" />
                            <label>Last Name: </label><input type="text" name="lastname" />
                            <label>Email: </label><input type="text" name="email" />
                            <label>Street Address: </label><input type="text" name="address" />
                            <label>Phone Number: </label><input type="text" name="phone" />
                            
                            <p>What gender are you?</p>
                            <input type="radio" name="gender" value="male">Male<br>
                            <input type="radio" name="gender" value="female">Female<br>
                            
                            <p>What prize(s) are you interested in?</p>
                            <input type="checkbox" name="prize" value="Car">Car<br>
                            <input type="checkbox" name="prize" value="Motorcycle">Motorcycle<br>
                            <input type="checkbox" name="prize" value="Jetski">Jetski<br>
                            
                            <input type="submit" value="Submit" />
                        </form>
                        
            </body>
        </html>'''
        
        if self.request.GET:
            firstname = self.request.GET['firstname']
            lastname = self.request.GET['lastname']
            email = self.request.GET['email']
            address = self.request.GET['address']
            phone = self.request.GET['phone']
            gender = self.request.GET['gender']
            prize = self.request.GET['prize']
            self.response.write(page_head + 'First Name: ' + firstname + ' Last Name: ' + lastname +
                                ' Email: ' + email + ' Address: ' + address + ' Phone: ' + phone +
                                ' Gender: ' + gender + ' Prizes: ' + prize)
        else:
            self.response.write(page_head + page_body)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
