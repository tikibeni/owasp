# Five OWASP-10 (2021) Flaws

Here I have listed five security flaws within a Python-Django template application some of which are implicitly created
and some of which are already inside the template.

---

## [A02:2021-Cryptographic Failures](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)

*Location:* Overall backend [settings & configuration](../mysite).

*Description:* The application uses HTTP instead of HTTPS. Therefore, the data transmitted via HTTP is not encrypted
anyhow and can be seen as clear text. This enables man-in-the-middle attacks. In addition, it is not clear how up to 
date the template backend's hashing algorithms are. Using HTTPS might also prevent cases of A07:2021.

*Fix:* Switch to HTTPS, secure cookies and use up-to-date hashing algorithms. Here are some steps:

[settings.py](../mysite/settings.py):
```python
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
```

The `X_COOKIE_SECURE` marks the desired cookie as `secure` thus making it transmittable only via HTTPS.

When enabled, the `SECURE_SSL_REDIRECT` will tell the SecurityMiddleware to redirect all non-HTTPS requests
to HTTPS.

[wsgi.py](../mysite/wsgi.py):
```python
os.environ['HTTPS'] = 'on'
```

Just sets the environmental value of HTTPS to true.

---

## [A03:2021-Injection](https://owasp.org/Top10/A03_2021-Injection/)

*Location:* [views.py](../polls/views.py) lines 61-62.

*Description:* The application contains unsanitized query within the views-file. Injection can be caused by following
these steps:

1. Run the server and go to http://127.0.0.1:8000/
2. Search for `doesnotexist' union select email, username from auth_user where is_superuser = 1 --`

You should now be looking at a link, which contains the superuser's username. The actual URL contains the email address
linked to the superuser. You can also change the parameters for example from email to password. After this the resulting
url will look like the hashed version of the password.

*Fix:* Sanitize inputs, don't mix raw input vars with queries. This flaw was artificially constructed to specifically use 
Django's `raw` query.

---

## [A04:2021-Insecure Design](https://owasp.org/Top10/A04_2021-Insecure_Design/)

*Location:* [settings.py](../mysite/settings.py) lines 23-26.

*Description:* The secret key used in production is not protected in any way and this repository is
public. Also, if this application would be running in development, the debug-mode is left on. The debug-mode
could enable the visibility of private information for example through console logs. In addition, debug-mode will consume
much more memory on a production server.

*Fix:* Remove the secret key from the version control and start using some library, which handles environmental 
variables, such as [dotenv](https://pypi.org/project/python-dotenv/). Also disable debug-mode in production and leave 
the mode managing to dotenv.

---

## [A05:2021-Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)

*Location:* The database.

*Description:* One of the listed security misconfigurations is "Default accounts and their passwords are still enabled
and unchanged." This template application utilizes a superuser with default credentials, which are: username "admin" and
password "admin". Default credentials greatly increase the risk of account theft and cases of A06.

*Fix:* Never use default credentials. I forcefully created a superuser with default credentials even though the
framework said it's not a good idea. Use usernames & passwords with special characters, different capitalizations and
numbers. One efficient way of ensuring strong credentials is using a password handling program, such as F-Secure ID
Protection.

---

## [A07:2021-Identification and Authentication Failures](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)

*Location*: Overall. You can run the provided sniffing [tool](../hack/brute.py) by starting the server and:

```shell
~/owasp/hack$ python3 brute.py
```

The tool will then print the password if the login works. Therefore, it should print the value `admin` to the console.

*Description:* The backend (and of course frontend) of the application makes it possible to bruteforce passwords as it 
does not check anything else than if the strings match. I initialized a simple bruteforcing tool to sniff out the 
password inside the [hack](../hack)-directory. You might recognize that the [brute.py](../hack/brute.py) is overall the 
same tool used in [Securing Software 4-19](https://cybersecuritybase.mooc.fi/module-2.4/1-finding). It relies on the 
fact that a username with a value "admin" exists. It then attempts to log in with the common passwords provided in 
[force.txt](../hack/force.txt). The bruteforcing is made possible via not limiting the amount of attempts in any way and
using a simple "username-password-form" type of login.

*Fix:* There are many ways to prevent auth-forcing. Few examples are: 

- limiting the amount of login attempts per timespan
- initializing captcha within the login
- multi-factor-authentication (MFA)
