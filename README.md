# **Password Check**

## **Overview**

PasswordCheck is a Python-based application that allows users to verify whether their passwords have been compromised in known data breaches. By utilizing the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3), the application hashes the user's password using the SHA-1 algorithm and checks if the hash appears in the database of breached passwords.

## **Features**

* Securely hashes user-provided passwords using SHA-1.  
* Implements the k-Anonymity model to maintain user privacy during API queries.  
* Checks the hashed password against the Have I Been Pwned database to determine if it has been compromised.  
* Provides clear feedback on the password's breach status.

## **How It Works**

1. **Hashing**: The application takes the user's password input and hashes it using the SHA-1 algorithm.  
2. **k-Anonymity**: Only the first five characters of the hashed password are sent to the Have I Been Pwned API, ensuring that the full password hash is never exposed.  
3. **API Query**: The API returns a list of hash suffixes that match the provided prefix.  
4. **Comparison**: The application checks if the full hash of the user's password is present in the returned list.  
5. **Feedback**: The user is informed whether their password has been found in any known data breaches.

## **Future Enhancements**

* Integrate a graphical user interface (GUI) for improved user experience.  
* Implement batch processing to check multiple passwords simultaneously.  
* Add support for checking passwords against local breach databases for offline verification.

## **🙌 Acknowledgements**

* [Have I Been Pwned](https://haveibeenpwned.com/) for providing the API and breach data.  
* [Requests Library](https://docs.python-requests.org/en/latest/) for handling HTTP requests.