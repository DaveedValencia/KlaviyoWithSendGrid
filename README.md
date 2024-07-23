# Klaviyo with SendGrid

Continue using Klaviyo but reduce cost significantly by using SendGrid to send email campaigns.

## Dependancies 

[SendGrid](https://sendgrid.com/en-us/solutions/email-api) API Documentation

[Jinja2](https://pypi.org/project/Jinja2/) Documentation

```bash
pip install sendgrid
pip install Jinja2
```

## How it works

Use Klaviyo for flows and email collecting and management. When you are ready to send an email campaign, create it in Klaviyo like you normally would. 

Next, export the Klaviyo template HTML and save the HTML file.

Next, export the segment you will be emailing.

Update the Klaviyo variables in the footer to the ones used in this script.
```
{{ organization }}
{{ unsubscribe }}
{{ full_address }}
```

Add the emails you will be sending to by updating the script email dictionary or by reading in a csv file.

You are now ready to send email campaign.

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html#license-text)
