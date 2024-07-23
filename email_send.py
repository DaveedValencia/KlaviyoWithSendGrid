import sendgrid
from jinja2 import FileSystemLoader, Environment

creds = 'SENDGRID_API_KEY'

sg = sendgrid.SendGridAPIClient(api_key=creds)

# The full path where your template folder
loader = FileSystemLoader(searchpath="/FULL PATH/Templates")
env = Environment(loader=loader)

# The name of the template you will use
html_template = "email_template.html"
template = env.get_template(html_template)

# The From Display name and email
sender = "Sender Name <email@domain.com>"

# Subject line
subject_line = "Summer Sale Starts Today!"

# Personalization Variables
organization = "Organization Name"
full_address = "123 Street, USA"
unsubscribe = '<a href="#">Unsubscribe</a>'

# List of users to email in dictionary format
contact_list = [{
  "name":'Full Name',
  "email":'email@domain.com',
}]

for contact in contact_list:
  email_template = template.render(name=contact["name"],organization=organization,full_address=full_address,unsubscribe=unsubscribe)

  data = {
    "personalizations": [
      {
        "to": [
          {
            "email": contact['email']
          }
        ],
        "subject": subject_line,
      }
    ],
    "from": {
      "email": sender
    },
    "content": [
      {
        "type": "text/html",
        "value": email_template
      }
    ]
  }
  response = sg.client.mail.send.post(request_body=data)
  print(response.status_code)
  print(response.body)
  print(response.headers)
