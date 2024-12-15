
# from datetime import date
# class vacation:
#     def __init__(self,title,country,start_date,end_date,price):
#         self.title=title
#         self.country=country
#         self.start_date=start_date
#         self.end_date=end_date
#         self.price=price
#         self.likes=0
#     def check_price(self):
#         return self.price<=10000 and self.price>=1000
#     def check_country(self):
#         countries = [
#             "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", 
#             "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", 
#             "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", 
#             "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", 
#             "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", 
#             "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", 
#             "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", 
#             "Cuba", "Cyprus", "Czechia (Czech Republic)", "Denmark", "Djibouti", "Dominica", 
#             "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", 
#             "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", 
#             "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", 
#             "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", 
#             "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", 
#             "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", 
#             "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", 
#             "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", 
#             "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", 
#             "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", 
#             "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", 
#             "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (formerly Burma)", 
#             "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", 
#             "Niger", "Nigeria", "North Macedonia (formerly Macedonia)", "Norway", 
#             "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", 
#             "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", 
#             "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
#             "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", 
#             "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", 
#             "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", 
#             "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland","Swaziland", "Syria", 
#             "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", 
#             "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", 
#             "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", 
#             "United States of America","USA", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", 
#             "Vietnam", "Yemen", "Zambia", "Zimbabwe"]

#         return self.country.lower() in (country.lower() for country in countries)
#     def check_start_date(self):
#         today=date.today()
#         return (self.start_date)>today 
#     def check_end_date(self):
#         return self.start_date<self.end_date
#     def totalLikes(self):
#         return self.likes

# class like:
#     def __init__(self,user,vacation):
#         self.user=user
#         self.vacation=vacation
#         self.Like=False
#     def like(self):
#         if self.Like==False:
#             self.vacation.likes=+1
#             self.Like=True
#     def unlike(self):
#         if self.Like==True:
#             self.vacation.likes=-1
#             self.Like=False
#     def viewLikes(self):
#         print(self.vacation)
# vac=vacation(title="blah",country="IsRaeL",start_date=date(2000,1,1),end_date=date(1999,1,1),price=1)
# print(vac.check_country())
# print(vac.check_start_date())
# print(vac.check_end_date())
# print(vac.check_price())
# newLike=like("sm",vac)
# print((newLike.vacation).totalLikes)

from datetime import date

class Vacation:
    def __init__(self, title, country, start_date, end_date, price):
        self.title = title
        self.country = country
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.likes = 0

    def check_price(self):
        return 1000 <= self.price <= 10000

    def check_country(self):
        countries = [
            "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", 
            "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", 
            "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", 
            "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", 
            "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", 
            "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", 
            "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", 
            "Cuba", "Cyprus", "Czechia (Czech Republic)", "Denmark", "Djibouti", "Dominica", 
            "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", 
            "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", 
            "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", 
            "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", 
            "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", 
            "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", 
            "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", 
            "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", 
            "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", 
            "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", 
            "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", 
            "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (formerly Burma)", 
            "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", 
            "Niger", "Nigeria", "North Macedonia (formerly Macedonia)", "Norway", 
            "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", 
            "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", 
            "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
            "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", 
            "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", 
            "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", 
            "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland","Swaziland", "Syria", 
            "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", 
            "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", 
            "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", 
            "United States of America","USA", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", 
            "Vietnam", "Yemen", "Zambia", "Zimbabwe"] 
        return self.country.lower() in (country.lower() for country in countries)

    def check_start_date(self):
        today = date.today()
        return self.start_date > today

    def check_end_date(self):
        return self.start_date < self.end_date

    def total_likes(self):
        return self.likes




print(vac.check_country())  # True
print(vac.check_start_date())  # True
print(vac.check_end_date())  # True
print(vac.check_price())  # True

new_like = Like("John Doe", vac)
print(new_like.view_likes())  # 0
new_like.like()
print(new_like.view_likes())  # 1
new_like.unlike()
print(new_like.view_likes())  # 0
