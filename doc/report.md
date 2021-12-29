# Six OWASP-10 (2021) Flaws

Here I have listed six security flaws inside the application.

---

## [A02:2021-Cryptographic Failures](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)

*Location:* Overall backend [settings & configuration](../mysite).

*Description:* The application uses HTTP instead of HTTPS. Therefore, the data transmitted via HTTP is not encrypted
anyhow and can be seen as clear text. In addition, it is not clear if the backend uses any hashing algorithms for the
user credentials. Using HTTPS might also prevent cases of A07:2021.

*Fix:* Switch to HTTPS, secure cookies and use up-to-date hashing algorithms. Here are some steps:

[settings.py](../mysite/settings.py):
```python
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
```

The `x_COOKIE_SECURE` marks the desired cookie as `secure` thus making it transmittable only via HTTPS.

When enabled, the `SECURE_SSL_REDIRECT` will tell the SecurityMiddleware to redirect all non-HTTPS requests
to HTTPS.

[wsgi.py](../mysite/wsgi.py):
```python
os.environ['HTTPS'] = 'on'
```

Just sets the environmental value of HTTPS to true.

---

## [A03:2021-Injection](https://owasp.org/Top10/A03_2021-Injection/)

Injection info goes here. Also XSS belongs here.

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

Default accounts and their passwords are still enabled and unchanged.

The software is out of date or vulnerable (A06)

---

## [A06:2021-Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)

Outdated Django e.g.

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
