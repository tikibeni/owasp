# Five OWASP-10 Flaws

Here I have listed the security flaws inside the application.

---

## [A02:2021-Cryptographic Failures](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)

Using HTTP instead of HTTPS.

No cryptographic algorithms for passwords.

---

## [A03:2021-Injection](https://owasp.org/Top10/A03_2021-Injection/)

Injection info goes here. Also XSS belongs here.

---

## [A04:2021-Insecure Design](https://owasp.org/Top10/A04_2021-Insecure_Design/)

*Location:* [settings.py](../mysite/settings.py) lines 23-26.

*Description:* The secret key used in production is not protected in any way and this repository is
public. Also, if this application would be running in development, the debug-mode is left on. The debug-mode
could enable the visibility of private information for example through console logs.

*Fix:* Remove the secret key from the version control and start using some library, which handles environmental variables, 
such as [dotenv](https://pypi.org/project/python-dotenv/). Also disable debug-mode in production and leave the mode managing
to dotenv.

---

## [A05:2021-Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)

Default accounts and their passwords are still enabled and unchanged.

The software is out of date or vulnerable (A06)

---

## [A06:2021-Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)

Outdated Django e.g.

---

## [A07:2021-Identification and Authentication Failures](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)

Password bruteforcing.
